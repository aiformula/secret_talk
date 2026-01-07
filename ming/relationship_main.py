#!/usr/bin/env python3

import asyncio
import json
import os
from pathlib import Path
import sys
import datetime
import traceback
from openai import OpenAI

# Import the new relationship modules
from relationship_content_generator import (
    generate_relationship_title_content,
    generate_relationship_story_content,
    generate_short_relationship_content,  # New short content function
    generate_relationship_conclusion_content,
    generate_instagram_caption,
    load_story_ideas_from_file,
    get_random_story_scenario,
    generate_varied_relationship_content,
    RELATIONSHIP_STORY_TEMPLATES
)

# Import the simple story generator with mock fallback
try:
    from simple_story_generator import generate_simple_story
except ImportError as e:
    print(f"⚠️ 故事生成器導入錯誤：{e}")
    generate_simple_story = None

# Import custom story reader
try:
    from custom_story_reader import read_custom_story, validate_custom_story_format
except ImportError as e:
    print(f"⚠️ 自定義故事讀取器導入錯誤：{e}")
    read_custom_story = None
    validate_custom_story_format = None
from relationship_template_generator import (
    generate_relationship_title_template,
    generate_relationship_story_template,
    generate_short_relationship_content_template,  # New short content template
    generate_relationship_conclusion_template,
    generate_relationship_end_template,
    generate_exact_custom_template  # NEW: Exact content preservation template
)
from image_generator import generate_images_from_templates
from telegram_sender import send_telegram_photos
from config import setup_environment
import os
from openai import OpenAI
from ig_optimization import InstagramOptimizer, create_optimized_caption  # 新增優化系統

def generate_fancy_ig_caption(story_data):
    """
    🎯 生成 fancy Instagram caption 格式（無 Dcard、無 Tag 朋友 CTA、無獨立句點分隔）
    """
    
    # 從故事提取情感關鍵詞
    title = story_data['title']
    content = story_data['content']
    conclusion = story_data['conclusion']
    
    # 情感 emoji 組合
    emotion_emojis = ["😳", "🌀", "💧", "⛈", "‼️", "💔", "💢", "😞", "😓", "😍", "⚡️", "⚽️", "🔍", "🌙", "⭐️", "🗣️", "😩", "💜"]
    
    # 根據內容選擇適合的 emoji
    selected_emojis = emotion_emojis[:4]  # 用少啲，保持清爽
    
    # 分割內容為段落
    content_paragraphs = content.split('\n\n')
    if len(content_paragraphs) < 3:
        # 如果段落不夠，按長度分割
        words = content.split('。')
        content_paragraphs = []
        current_paragraph = ""
        for sentence in words:
            if sentence.strip():
                current_paragraph += sentence.strip() + "。"
                if len(current_paragraph) > 100:
                    content_paragraphs.append(current_paragraph)
                    current_paragraph = ""
        if current_paragraph:
            content_paragraphs.append(current_paragraph)
    
    # 構建 caption（不用獨立句點行分隔）
    caption_parts = [
        f"{title} {' '.join(selected_emojis)}",
        f"是咁的，{content_paragraphs[0][:160]}{'...' if len(content_paragraphs[0]) > 160 else ''}",
        f"{content_paragraphs[1][:160] if len(content_paragraphs) > 1 else ''}{'...' if len(content_paragraphs) > 1 and len(content_paragraphs[1]) > 160 else ''}",
        f"{content_paragraphs[2][:160] if len(content_paragraphs) > 2 else ''}{'...' if len(content_paragraphs) > 2 and len(content_paragraphs[2]) > 160 else ''}",
        f"{conclusion}",
        "你點睇？歡迎留言分享你嘅意見，一齊傾下。",
        "#香港愛情 #感情問題 #拍拖煩惱 #戀愛日常 #香港情侶 #愛情故事 #分手 #香港女仔 #香港男仔 #情感分享 #愛情煩惱 #戀愛心得 #情侶問題 #復合 #感情困擾 #愛情討論 #戀愛經驗 #感情諮詢 #愛情解答 #戀愛故事分享 #情感療癒 #愛情成長 #關係經營 #感情心理學"
    ]
    
    # 移除空字串行
    caption_parts = [part for part in caption_parts if part.strip()]
    
    return "\n\n".join(caption_parts)

async def generate_relationship_content():
    """主要功能：生成關係故事內容，使用 story_ideas.txt 天條第一誡，包含完整優化"""
    try:
        # Setup environment and get clients
        print("\n=== 🚀 設定環境 ===")
        clients = setup_environment()
        
        # 初始化 Instagram 優化器
        ig_optimizer = InstagramOptimizer()
        print("✅ Instagram 優化系統已啟動")
        
        # Generate content using story_ideas.txt approach (天條第一誡)
        print("\n=== 🎯 使用 story_ideas.txt 天條第一誡生成內容 ===")
        
        # Load story ideas or use default concept
        story_ideas = load_story_ideas_from_file()
        if story_ideas:
            selected_idea = story_ideas[0]  # Use first story
            story_concept = selected_idea.get('content', selected_idea.get('story_template', ''))
        else:
            story_concept = "我發現我24歲嘅男朋友派帽俾我，影響到我 final year 嘅學業。"
        
        print(f"📖 使用故事概念：{story_concept[:100]}...")
        print("⏳ 正在用天條第一誡生成...")
        
        # Generate content using simple method with fallback
        if generate_simple_story is None:
            print("❌ 故事生成器不可用，使用 Mock 模式")
            from mock_story_generator import generate_mock_story
            simple_result = await generate_mock_story(story_concept)
        else:
            simple_result = generate_simple_story(story_concept)
        
        # Process simple_result to create templates
        scenario = get_random_story_scenario()
        perspective = scenario.get('perspective', 'female')
        
        # Extract content from simple result and add missing fields
        title_content = {
            'title': simple_result.get('標題', '感情故事分享'),
            'keywords': ['感情', '關係', '香港', 'final year']
        }
        story_content_text = simple_result.get('內容', '')
        conclusion_text = simple_result.get('結論', '大家覺得我應該點做？')
        
        # Split story content into 3 parts for image generation
        sentences = story_content_text.split('。')
        if len(sentences) < 3:
            # If not enough sentences, pad with empty ones
            sentences.extend([''] * (3 - len(sentences)))
        
        part_size = max(1, len(sentences) // 3)
        
        story_points = []
        for i in range(3):
            start_idx = i * part_size
            if i == 2:  # Last part gets remaining sentences
                end_idx = len(sentences)
            else:
                end_idx = (i + 1) * part_size
            
            part_content = '。'.join(sentences[start_idx:end_idx])
            if part_content and not part_content.endswith('。'):
                part_content += '。'
            
            # Ensure each part has some content
            if not part_content.strip():
                part_content = f"故事內容第{i+1}部分。"
            
            story_points.append({
                'title': f'故事第{i+1}部分',
                'description': part_content
            })
        
        story_content = {
            'story_points': story_points,
            'keywords': ['感情', '關係', '香港', 'final year']
        }
        
        conclusion_content = {
            'conclusion': conclusion_text,
            'keywords': ['感情', '關係', '香港', 'final year']
        }
        
        # Generate Instagram caption based on story_ideas.txt style
        ig_caption = f"{simple_result.get('標題', '')}\n\n{story_content_text[:200]}...\n\n{conclusion_text}"
        
        # Content already extracted above from simple_result
        scenario = scenario
        # title_content, story_content, conclusion_content, ig_caption already defined
        
        # 📊 內容分析和優化建議
        print("\n=== 📊 內容優化分析 ===")
        story_text = " ".join([point['description'][:100] for point in story_content['story_points']])
        performance_analysis = ig_optimizer.analyze_content_performance(story_text)
        optimal_time = ig_optimizer.get_optimal_posting_time()
        hashtag_strategy = ig_optimizer.generate_hashtag_strategy(scenario['theme'])
        
        print(f"📈 內容評分: {performance_analysis['score']}/100 ({performance_analysis['rating']})")
        print(f"⏰ 最佳發布時間: {optimal_time}")
        print(f"🏷️ 標籤策略: {len(sum(hashtag_strategy.values(), []))} 個精準標籤")
        print(f"💡 優化建議: {', '.join(performance_analysis['feedback'])}")
        
        print(f"\n=== 📝 生成內容摘要 ===")
        print(f"🎭 主題：{scenario['theme']}")
        print(f"📰 標題: {title_content['title']}")
        print(f"📖 故事要點: {len(story_content['story_points'])} 個")
        print(f"💭 結論: {conclusion_content['conclusion'][:50]}...")
        print(f"📱 IG Caption 預覽: {ig_caption[:100]}...")
        print(f"🎯 生成方法: story_ideas.txt 天條第一誡")
        
        # Save the Instagram caption to file with optimization info
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        caption_filename = 'generated_ig_caption.txt'
        with open(caption_filename, 'w', encoding='utf-8') as f:
            f.write(f"🎭 主題：{scenario['theme']}\n")
            f.write(f"⏰ 生成時間：{timestamp}\n")
            f.write(f"📈 內容評分：{performance_analysis['score']}/100\n")
            f.write(f"🕐 最佳發布時間：{optimal_time}\n")
            f.write(f"🏷️ 標籤數量：{len(sum(hashtag_strategy.values(), []))} 個\n\n")
            f.write("=== 優化建議 ===\n")
            for tip in performance_analysis['feedback']:
                f.write(f"• {tip}\n")
            f.write(f"\n=== Instagram Caption ===\n")
            f.write(ig_caption)
            f.write(f"\n\n=== 標籤策略明細 ===\n")
            for category, tags in hashtag_strategy.items():
                f.write(f"{category}: {' '.join(tags)}\n")
        print(f"📄 Instagram標題已保存到：{caption_filename}")
        
        # Generate HTML templates
        print("\n=== 🎨 生成 HTML 模板 ===")
        
        # Get perspective from scenario
        perspective = scenario.get('perspective', 'female')
        print(f"👤 使用視角：{perspective} ({'男性' if perspective == 'male' else '女性'})")
        
        # Check if story_points is empty or has less than 3 points
        if not story_content.get('story_points') or len(story_content['story_points']) < 3:
            print(f"❌ 故事內容解析失敗，只有 {len(story_content.get('story_points', []))} 個要點")
            print(f"📝 原始回應：{story_content}")
            raise Exception("故事內容解析失敗，請檢查AI回應格式")
        
        templates = {
            'title': generate_relationship_title_template(
                title_content, 
                title_content['keywords'],
                perspective=perspective
            ),
            'story1': generate_relationship_story_template(
                story_content['story_points'][0], 
                story_content['keywords'],
                page_number=1,
                perspective=perspective
            ),
            'story2': generate_relationship_story_template(
                story_content['story_points'][1], 
                story_content['keywords'],
                page_number=2,
                perspective=perspective
            ),
            'story3': generate_relationship_story_template(
                story_content['story_points'][2], 
                story_content['keywords'],
                page_number=3,
                perspective=perspective
            ),
            'conclusion': generate_relationship_conclusion_template(
                conclusion_content, 
                story_content['keywords'],
                perspective=perspective
            ),
            'end': generate_relationship_end_template(perspective=perspective)
        }
        
        # Generate images from templates
        print("\n=== 🖼️ 生成圖片 ===")
        png_paths = await generate_images_from_templates(templates, f"relationship_{timestamp}")
        
        # Send to Telegram if images were generated successfully
        if png_paths:
            print("\n=== 📱 發送到 Telegram ===")
            
            # 創建增強版 Telegram 標題，包含優化信息
            telegram_caption = f"""🎭 {scenario['theme']} 故事
⏰ 生成時間：{timestamp}
📈 內容評分：{performance_analysis['score']}/100
🕐 建議發布：{optimal_time}
🏷️ 標籤策略：{len(sum(hashtag_strategy.values(), []))} 個精準標籤

{ig_caption}"""
            
            success = await send_telegram_photos(
                clients['telegram_bot'], 
                clients['telegram_chat_id'], 
                png_paths, 
                telegram_caption
            )
            if not success:
                print("❌ Telegram 發送失敗，但內容已生成完成")
        else:
            print("❌ 無圖片生成，跳過 Telegram 上傳")
        
        # 📅 生成發布時間表
        schedule = ig_optimizer.get_posting_schedule(7)
        print(f"\n=== 📅 一週發布時間表 ===")
        for day_plan in schedule[:3]:  # 顯示前3天
            print(f"📅 {day_plan['date']} ({day_plan['day']}) - {day_plan['time']} - {day_plan['reason']}")
        
        return {
            'scenario': scenario,
            'title_content': title_content,
            'story_content': story_content,
            'conclusion_content': conclusion_content,
            'ig_caption': ig_caption,
            'templates': templates,
            'png_paths': png_paths,
            'timestamp': timestamp,
            'optimization': {
                'performance': performance_analysis,
                'optimal_time': optimal_time,
                'hashtag_strategy': hashtag_strategy,
                'schedule': schedule
            }
        }
        
    except Exception as e:
        print(f"❌ 發生錯誤: {str(e)}")
        raise

async def generate_simple_content(story_concept: str = None):
    """使用超簡易指令清單生成內容"""
    try:
        # Setup environment
        print("\n=== 🎯 story_ideas.txt 天條第一誡 ===")
        print("100% 跟足您嘅故事概念！")
        
        # Get story concept
        if not story_concept:
            # Load from story ideas or use default
            story_ideas = load_story_ideas_from_file()
            if story_ideas:
                selected_idea = story_ideas[0]  # Use first story
                story_concept = selected_idea.get('content', selected_idea.get('story_template', ''))
            else:
                story_concept = "我發現我24歲嘅男朋友派帽俾我，影響到我 final year 嘅學業。"
        
        print(f"📖 故事概念：{story_concept}")
        print("\n⏳ 正在用天條第一誡生成...")
        
        # Generate content using simple method with fallback
        if generate_simple_story is None:
            print("❌ 故事生成器不可用")
            return None
        
        result = generate_simple_story(story_concept)
        
        print("✅ 生成完成！")
        print("\n=== 📋 內容摘要 ===")
        print(f"📰 標題：{result.get('標題', 'N/A')}")
        print(f"📄 內容長度：{len(result.get('內容', ''))} 字")
        print(f"❓ 結論：{result.get('結論', 'N/A')}")
        
        # Save to file
        output_file = "generated_simple_content.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 內容已保存到：{output_file}")
        print("\n=== 📋 最終JSON輸出 ===")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
        return result
        
    except Exception as e:
        print(f"❌ 發生錯誤: {str(e)}")
        raise

async def main_short_content():
    """短版內容生成：包含完整 IG 優化"""
    try:
        # Initialize OpenAI client and IG optimizer
        print("\n=== 🚀 初始化系統 ===")
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            # Load from .env file
            from dotenv import load_dotenv
            load_dotenv()
            openai_api_key = os.getenv("OPENAI_API_KEY")
        
        openai_client = OpenAI(api_key=openai_api_key)
        ig_optimizer = InstagramOptimizer()
        print("✅ Instagram 優化系統已啟動")
        
        # Load story ideas from file
        story_ideas = load_story_ideas_from_file()
        
        if not story_ideas:
            print("📝 使用預設故事...")
            story_content = "我同男朋友一齊咗好耐，但最近覺得佢對我越來越冷淡..."
        else:
            story_content = story_ideas[0]['content']
            print(f"📖 使用故事: {story_content[:100]}...")
        
        # Generate scenario
        scenario = get_random_story_scenario()
        perspective = scenario.get('perspective', 'female')
        
        print(f"👤 生成{perspective}視角內容...")
        
        # 📊 預先分析內容
        performance_analysis = ig_optimizer.analyze_content_performance(story_content)
        optimal_time = ig_optimizer.get_optimal_posting_time()
        
        print(f"📈 內容評分: {performance_analysis['score']}/100")
        print(f"⏰ 最佳發布時間: {optimal_time}")
        
        # Generate title content
        print("🎯 生成標題內容...")
        title_content = await generate_relationship_title_content(openai_client, story_content, scenario)
        
        # Generate SHORT content (instead of long story points)
        print("✂️ 生成短版內容...")
        short_content = await generate_short_relationship_content(openai_client, story_content, scenario)
        
        # Generate conclusion
        print("💭 生成結論...")
        mock_story = {
            'hook': title_content['title'],
            'story_points': [{'title': 'Summary', 'description': short_content['content']}],
            'scenario': scenario
        }
        conclusion_content = await generate_relationship_conclusion_content(openai_client, mock_story)
        
        # Generate OPTIMIZED Instagram caption
        print("📱 生成優化版 Instagram caption...")
        instagram_caption = await generate_instagram_caption(openai_client, mock_story)
        
        # 🏷️ 生成標籤策略
        hashtag_strategy = ig_optimizer.generate_hashtag_strategy(scenario['theme'])
        
        # Save comprehensive report
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        with open('generated_ig_caption.txt', 'w', encoding='utf-8') as f:
            f.write(f"🎭 短版模式 - {scenario['theme']}\n")
            f.write(f"⏰ 生成時間：{timestamp}\n")
            f.write(f"📈 內容評分：{performance_analysis['score']}/100 ({performance_analysis['rating']})\n")
            f.write(f"🕐 最佳發布時間：{optimal_time}\n")
            f.write(f"🏷️ 標籤數量：{len(sum(hashtag_strategy.values(), []))} 個\n\n")
            
            f.write("=== 📊 優化建議 ===\n")
            for tip in performance_analysis['feedback']:
                f.write(f"• {tip}\n")
            
            f.write(f"\n=== 📱 Instagram Caption ===\n")
            f.write(instagram_caption['caption'])
            
            f.write(f"\n\n=== 🏷️ 標籤策略 ===\n")
            for category, tags in hashtag_strategy.items():
                f.write(f"📌 {category}: {' '.join(tags)}\n")
        
        # Create optimized templates
        print("🎨 創建優化模板...")
        templates = []
        
        # Title template
        title_template = generate_relationship_title_template(
            title_content, 
            title_content.get('keywords', []), 
            perspective
        )
        templates.append(('title.html', title_template))
        
        # Short content template (only one page)
        short_template = generate_short_relationship_content_template(
            short_content['content'],
            short_content.get('keywords', []),
            perspective
        )
        templates.append(('content_page1.html', short_template))
        
        # Conclusion template
        conclusion_template = generate_relationship_conclusion_template(
            conclusion_content,
            short_content.get('keywords', []),
            perspective
        )
        templates.append(('conclusion.html', conclusion_template))
        
        # End template
        end_template = generate_relationship_end_template(perspective)
        templates.append(('end.html', end_template))
        
        # Create images
        print("🖼️ 生成圖片...")
        template_dict = {}
        for filename, template_content in templates:
            template_name = filename.replace('.html', '')
            if template_name == 'content_page1':
                template_name = 'story1'
            template_dict[template_name] = template_content
        
        png_paths = await generate_images_from_templates(template_dict, f"short_{timestamp}")
        
        # Send to Telegram with optimization info
        if png_paths:
            print("📱 發送到 Telegram...")
            
            import telegram
            telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
            telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
            
            if not telegram_bot_token or not telegram_chat_id:
                # Load from .env file
                from dotenv import load_dotenv
                load_dotenv()
                telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
                telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
            
            bot = telegram.Bot(token=telegram_bot_token)
            
            # 增強版 caption 包含優化資訊
            enhanced_caption = f"""📱 短版感情故事分享 | {scenario['theme']} 主題
📈 內容評分：{performance_analysis['score']}/100
⏰ 建議發布：{optimal_time}
🏷️ {len(sum(hashtag_strategy.values(), []))} 個精準標籤

{instagram_caption['caption']}

💡 優化提示：{' | '.join(performance_analysis['feedback'][:2])}"""
            
            success = await send_telegram_photos(
                bot,
                telegram_chat_id,
                png_paths,
                enhanced_caption
            )
            if not success:
                print("❌ Telegram 發送失敗，但內容已生成完成")
        else:
            print("❌ 無圖片生成，跳過 Telegram 上傳")
        
        # 📅 顯示發布時間表
        schedule = ig_optimizer.get_posting_schedule(3)
        print(f"\n=== 📅 建議發布時間 ===")
        for day_plan in schedule:
            print(f"📅 {day_plan['date']} - {day_plan['time']} ({day_plan['reason']})")
        
        print("✅ 短版內容生成完成！")
        
    except Exception as e:
        print(f"❌ 短版內容生成錯誤: {e}")
        import traceback
        traceback.print_exc()

async def test_template_generation():
    """測試模板生成功能"""
    print("\n=== 🧪 測試模板生成 ===")
    
    # 添加 IG 優化器到測試
    ig_optimizer = InstagramOptimizer()
    
    # Use the predefined template
    template_data = RELATIONSHIP_STORY_TEMPLATES["superstition_plastic_surgery"]
    
    # 分析測試內容
    test_content = template_data['story_points'][0]['description'][:200]
    performance = ig_optimizer.analyze_content_performance(test_content)
    optimal_time = ig_optimizer.get_optimal_posting_time()
    
    print(f"📊 測試內容評分: {performance['score']}/100")
    print(f"⏰ 建議發布時間: {optimal_time}")
    
    templates = {
        'title': generate_relationship_title_template(
            {'title': template_data['title']}, 
            template_data['keywords']
        ),
        'story1': generate_relationship_story_template(
            template_data['story_points'][0], 
            template_data['keywords'],
            page_number=1
        ),
        'story2': generate_relationship_story_template(
            template_data['story_points'][1], 
            template_data['keywords'],
            page_number=2
        ),
        'story3': generate_relationship_story_template(
            template_data['story_points'][2], 
            template_data['keywords'],
            page_number=3
        ),
        'conclusion': generate_relationship_conclusion_template(
            {'conclusion': '大家覺得我應該點做？'}, 
            template_data['keywords']
        ),
        'end': generate_relationship_end_template()
    }
    
    # Generate images from templates
    print("\n=== 🖼️ 生成測試圖片 ===")
    png_paths = await generate_images_from_templates(templates, "test_optimized")
    
    if png_paths:
        print(f"✅ 成功生成 {len(png_paths)} 張圖片:")
        for path in png_paths:
            print(f"  📄 {path}")
    else:
        print("❌ 圖片生成失敗")
    
    return templates, png_paths

async def show_optimization_report():
    """顯示完整優化報告"""
    print("\n=== 📊 Instagram 優化報告 ===")
    
    ig_optimizer = InstagramOptimizer()
    
    # 測試內容
    test_content = "我同男朋友一齊咗12年，但佢為咗21歲既妹妹仔同我講分手。我真係好無奈，唔知點算好。"
    
    # 生成完整分析
    performance = ig_optimizer.analyze_content_performance(test_content)
    optimal_time = ig_optimizer.get_optimal_posting_time()
    hashtag_strategy = ig_optimizer.generate_hashtag_strategy(test_content)
    engagement = ig_optimizer.generate_engagement_content(test_content)
    schedule = ig_optimizer.get_posting_schedule(7)
    
    print(f"📈 內容評分: {performance['score']}/100 ({performance['rating']})")
    print(f"⏰ 最佳發布時間: {optimal_time}")
    print(f"🏷️ 標籤策略: {len(sum(hashtag_strategy.values(), []))} 個標籤")
    print(f"💡 優化建議:")
    for tip in performance['feedback']:
        print(f"  • {tip}")
    
    print(f"\n📅 一週發布時間表:")
    for day in schedule:
        print(f"  {day['date']} ({day['day']}) - {day['time']} - {day['reason']}")
    
    print(f"\n🎯 互動策略: {engagement['call_to_action']}")
    
    print(f"\n🏷️ 標籤分佈:")
    for category, tags in hashtag_strategy.items():
        print(f"  📌 {category} ({len(tags)}個): {' '.join(tags[:3])}...")

async def generate_custom_story_content():
    """
    📝 自定義故事內容生成（原文不變）
    讀取用戶自定義故事檔案，生成圖片，唔改動任何文字內容
    """
    print("\n=== 📝 自定義故事圖片生成 ===")
    
    # 檢查功能是否可用
    if read_custom_story is None:
        print("❌ 自定義故事讀取器未能正確導入")
        print("💡 請確保 custom_story_reader.py 檔案存在")
        return
    
    # 初始化環境變量
    try:
        clients = setup_environment()
        print("✅ 環境變數設置成功，將會發送到 Telegram")
    except Exception as e:
        print(f"⚠️ 環境初始化錯誤：{e}")
        print("📝 將跳過 Telegram 發送，只生成圖片")
        print("💡 如需發送到 Telegram，請參考：ming/TELEGRAM_SETUP_GUIDE.md")
        print("🔧 或者手動創建 ming/.env 檔案並填入你嘅 API keys")
        clients = None
    
    # 顯示使用說明
    print("📖 使用說明:")
    print("1. ⚠️  重要：編輯 my_custom_story.txt 檔案")
    print("   可放在：專案根目錄 或 ming/ 子目錄")
    print("2. 按格式填寫：標題、內容、結尾")
    print("3. 系統會自動生成圖片，唔會改動你嘅內容")
    print("4. 系統會自動檢測故事視角（男/女）")
    print("📍 檔案搜尋順序：")
    print("   1️⃣ 根目錄/my_custom_story.txt")
    print("   2️⃣ ming/my_custom_story.txt")
    print()
    
    # 使用新的共用函數處理自定義故事
    await generate_custom_story_with_file("my_custom_story.txt")

async def generate_custom_boy_story_content():
    """
    📝 男性視角自定義故事內容生成（原文不變）
    專門處理男仔模板的自定義故事生成
    """
    print("\n=== 👨 男性視角自定義故事圖片生成 ===")
    
    # 檢查男仔故事檔案是否存在
    boy_story_file = "my_custom_story_boy.txt"
    if not os.path.exists(boy_story_file):
        print(f"⚠️ 找唔到 {boy_story_file} 檔案")
        print("💡 已為你創建男性視角模板檔案，請編輯後再試")
        print(f"📍 檔案位置：ming/{boy_story_file}")
        return
    
    # 使用男仔故事檔案生成內容
    await generate_custom_story_with_file(boy_story_file)

async def generate_custom_story_with_file(filename):
    """
    📝 使用指定檔案生成自定義故事內容
    
    Args:
        filename: 故事檔案名稱
    """
    print(f"\n=== 📝 使用 {filename} 生成自定義故事圖片 ===")
    
    # 檢查功能是否可用
    if read_custom_story is None:
        print("❌ 自定義故事讀取器未能正確導入")
        print("💡 請確保 custom_story_reader.py 檔案存在")
        return
    
    # 初始化環境變量
    try:
        clients = setup_environment()
    except Exception as e:
        print(f"⚠️ 環境初始化錯誤：{e}")
        print("📝 將跳過 Telegram 發送，只生成圖片")
        clients = None
    
    # 🔍 智能路徑檢測：先檢查當前目錄，再檢查父目錄
    # 擴展搜尋路徑，包括更多可能的位置
    script_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    root_dir = os.path.dirname(os.path.dirname(script_dir)) if os.path.dirname(script_dir) else current_dir
    
    possible_paths = [
        filename,  # 當前目錄
        os.path.join("..", filename),  # 父目錄
        os.path.join(current_dir, filename),  # 當前工作目錄
        os.path.join(parent_dir, filename),  # 父目錄（絕對路徑）
        os.path.join(root_dir, filename),  # 根目錄
        os.path.join(script_dir, filename),  # 腳本所在目錄
        os.path.join(script_dir, "..", filename),  # 腳本父目錄
        os.path.join(os.path.dirname(os.path.dirname(__file__)), filename) if __file__ else filename  # 腳本父目錄
    ]
    
    # 去重並找到第一個存在的檔案（優先使用最新修改的）
    existing_paths = []
    for path in possible_paths:
        abs_path = os.path.abspath(path)
        if os.path.exists(abs_path) and abs_path not in [p[0] for p in existing_paths]:
            mtime = os.path.getmtime(abs_path)
            existing_paths.append((abs_path, mtime))
    
    if not existing_paths:
        print(f"⚠️ 找唔到 {filename} 檔案")
        print(f"💡 已搜尋以下位置:")
        for path in possible_paths[:5]:  # 只顯示前5個
            print(f"   - {os.path.abspath(path)}")
        print(f"💡 請確保 {filename} 檔案存在並包含你嘅故事內容")
        return
    
    # 選擇最新修改的檔案
    existing_paths.sort(key=lambda x: x[1], reverse=True)
    actual_file = existing_paths[0][0]
    
    print(f"✅ 找到故事檔案：{actual_file}")
    print(f"📅 檔案修改時間：{datetime.datetime.fromtimestamp(existing_paths[0][1]).strftime('%Y-%m-%d %H:%M:%S')}")
    
    filename = actual_file  # 使用找到的檔案路徑
    
    try:
        # 驗證故事格式
        print("🔍 驗證故事格式...")
        is_valid, message = validate_custom_story_format(filename)
        if not is_valid:
            print(f"❌ 故事格式錯誤: {message}")
            print(f"💡 請檢查 {filename} 的格式")
            return
        
        # 讀取故事內容
        print(f"📖 讀取故事內容 ({filename})...")
        story_data = read_custom_story(filename)
        
        if 'error' in story_data:
            print(f"❌ 讀取錯誤: {story_data['error']}")
            print(f"💡 建議: {story_data['suggestion']}")
            return
        
        # 顯示讀取到的內容摘要
        print("\n✅ 成功讀取故事")
        print("=" * 60)
        print(f"📰 標題: {story_data['title']}")
        print(f"📄 內容長度: {len(story_data['content'])} 字符")
        print(f"📝 內容部分數: {len(story_data.get('content_parts', []))} 頁")
        print(f"❓ 結論: {story_data['conclusion']}")
        print(f"🏷️ 關鍵詞: {', '.join(story_data['keywords']) if story_data['keywords'] else '無'}")
        print("🎯 模式: 100% 原文保留，不做任何修改")
        print("=" * 60)
        
        # 顯示內容預覽（前200字符）
        content_preview = story_data['content'][:200]
        if len(story_data['content']) > 200:
            content_preview += "..."
        print(f"\n📖 內容預覽:\n{content_preview}\n")
        
        # 生成時間戳
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 使用故事數據中的視角信息
        perspective = story_data.get('perspective', 'female')  # 從故事數據獲取視角
        
        # 顯示視角檢測結果
        print(f"\n🎭 視角檢測結果:")
        if 'perspective_detection' in story_data:
            detection = story_data['perspective_detection']
            print(f"   📁 檔案名稱檢測: {detection['filename']} ({'👨 男' if detection['filename'] == 'male' else '👩 女'})")
            print(f"   📝 內容檢測: {detection['content']} ({'👨 男' if detection['content'] == 'male' else '👩 女'})")
            print(f"   ✅ 最終選擇: {detection['final']} ({'👨‍💼 男性視角 (Boy View)' if detection['final'] == 'male' else '👩‍💼 女性視角 (Girl View)'})")
        else:
            print(f"   ✅ 使用預設: {perspective} ({'👨‍💼 男性視角 (Boy View)' if perspective == 'male' else '👩‍💼 女性視角 (Girl View)'})")
        
        # 額外驗證：顯示關鍵證據
        if '男朋友' in story_data['content'] or '男朋友' in story_data['title']:
            print(f"   🔍 證據: 發現「男朋友」→ 確認為女性視角 ✓")
        elif '女朋友' in story_data['content'] or '女朋友' in story_data['title']:
            print(f"   🔍 證據: 發現「女朋友」→ 確認為男性視角 ✓")
        
        # 生成 HTML 模板（使用原文不變模板）
        print(f"\n=== 🎨 生成 HTML 模板（100% 原文保留，{perspective} 視角） ===")
        # 動態生成模板，支援不同數量嘅內容頁
        templates = {
            'title': generate_exact_custom_template(
                story_data['title'], 
                template_type="title",
                perspective=perspective
            )
        }
        
        # 動態添加內容頁
        content_parts = story_data['content_parts']
        for i, part in enumerate(content_parts):
            if part.strip():  # 只添加非空內容
                story_key = f'story{i+1}'
                templates[story_key] = generate_exact_custom_template(
                    part, 
                    template_type="content",
                    perspective=perspective
                )
        
        # 添加結論和結束頁
        templates.update({
            'conclusion': generate_exact_custom_template(
                story_data['conclusion'], 
                template_type="conclusion",
                perspective=perspective
            ),
            'end': generate_relationship_end_template(perspective=perspective)
        })
        
        # 生成圖片
        print("\n=== 🖼️ 生成圖片 ===")
        file_prefix = filename.replace('.txt', '').replace('my_custom_story', 'custom')
        png_paths = await generate_images_from_templates(templates, f"{file_prefix}_{timestamp}")
        
        if png_paths:
            print(f"✅ 成功生成 {len(png_paths)} 張圖片")
            
            # 顯示生成的圖片
            for i, path in enumerate(png_paths):
                print(f"  📄 {i+1}. {path}")
            
            # 發送到 Telegram
            print("\n=== 📱 發送到 Telegram ===")
            
            if clients:
                # 創建 fancy Instagram 標題
                ig_caption = generate_fancy_ig_caption(story_data)
                
                # 發送到 Telegram
                await send_telegram_photos(
                    clients['telegram_bot'], 
                    clients['telegram_chat_id'],
                    png_paths, 
                    ig_caption
                )
                print("✅ 已發送到 Telegram")
            else:
                print("⚠️ 跳過 Telegram 發送（環境變量未設置）")
                print("💡 如需發送到 Telegram，請參考：ming/TELEGRAM_SETUP_GUIDE.md")
                print("🔧 創建 ming/.env 檔案並填入你嘅 Telegram Bot Token 同 Chat ID")
                
            # 生成 Instagram 標題並保存
            print("\n=== 📱 生成 Instagram 標題 ===")
            try:
                # 使用 OpenAI 客戶端生成 Instagram 標題
                if clients and 'openai_client' in clients:
                    ig_caption = await generate_instagram_caption(clients['openai_client'], story_data)
                    
                    # 保存 Instagram 標題到檔案
                    timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    ig_filename = f"generated_ig_caption_{file_prefix}_{timestamp_str}.txt"
                    
                    with open(ig_filename, 'w', encoding='utf-8') as f:
                        f.write(ig_caption)
                    
                    print(f"📝 Instagram 標題已保存到: {ig_filename}")
                    print(f"📄 標題內容預覽: {ig_caption[:100]}...")
                else:
                    print("⚠️ 跳過 Instagram 標題生成（OpenAI 客戶端未設置）")
            except Exception as ig_error:
                print(f"⚠️ Instagram 標題生成失敗: {ig_error}")
        else:
            print("❌ 圖片生成失敗")
            
        print(f"\n📄 生成方法: {story_data['generation_method']}")
        print("✅ 自定義故事處理完成！")
        
    except Exception as e:
        print(f"❌ 生成過程發生錯誤: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "short":
            # 短版內容生成（包含完整優化）
            asyncio.run(main_short_content())
        elif sys.argv[1] == "simple":
            # 超簡易指令生成
            if len(sys.argv) > 2:
                # 使用提供的故事概念
                story_concept = " ".join(sys.argv[2:])
                asyncio.run(generate_simple_content(story_concept))
            else:
                # 使用預設故事概念
                asyncio.run(generate_simple_content())
        elif sys.argv[1] == "test":
            # 測試模式（包含優化分析）
            asyncio.run(test_template_generation())
        elif sys.argv[1] == "report":
            # 顯示優化報告
            asyncio.run(show_optimization_report())
        else:
            # 完整內容生成（包含完整優化）
            asyncio.run(generate_relationship_content()) 
    else:
        # 互動模式
        try:
            print("🎭 選擇模式：")
            print("1. 完整內容生成（包括圖片和Telegram發送）")
            print("2. 短版內容生成（純文字，適合快速測試）") 
            print("3. story_ideas.txt 天條第一誡（新！100% 跟足故事概念）")
            print("4. 測試模式")
            print("5. 優化報告")
            print("6. 自定義故事圖片生成（用你自己嘅故事內容，原文不變）")
            
            choice = input("請選擇 (1-6): ").strip()
            
            if choice == "1":
                asyncio.run(generate_relationship_content())
            elif choice == "2":
                asyncio.run(main_short_content())
            elif choice == "3":
                print("\n=== 🎯 天條第一誡模式 ===")
                print("您可以：")
                print("A. 使用預設故事概念")
                print("B. 輸入自定義故事概念")
                
                sub_choice = input("請選擇 (A 或 B): ").strip().upper()
                
                if sub_choice == "B":
                    print("\n請輸入您的【故事概念】：")
                    custom_story = input().strip()
                    if custom_story:
                        asyncio.run(generate_simple_content(custom_story))
                    else:
                        print("❌ 故事概念不能為空，使用預設概念")
                        asyncio.run(generate_simple_content())
                else:
                    asyncio.run(generate_simple_content())
            elif choice == "4":
                asyncio.run(test_template_generation())
            elif choice == "5":
                asyncio.run(show_optimization_report())
            elif choice == "6":
                asyncio.run(generate_custom_story_content())
            else:
                print("❌ 無效選擇，使用完整內容生成")
                asyncio.run(generate_relationship_content())
                
        except KeyboardInterrupt:
            print("\n👋 操作已取消")
        except Exception as e:
            print(f"❌ 發生錯誤: {str(e)}")
            traceback.print_exc() 