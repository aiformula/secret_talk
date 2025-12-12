#!/usr/bin/env python3
"""
🎯 直接運行自定義故事生成（不使用 OpenAI）
Direct custom story generation without OpenAI
"""

import os
import sys
import datetime
import asyncio
from custom_story_reader import read_custom_story, validate_custom_story_format
from relationship_template_generator import generate_exact_custom_template
from image_generator import generate_images_from_templates
from telegram_sender import send_telegram_photos
from config import setup_environment

async def generate_custom_story_images():
    """
    直接生成自定義故事圖片，不使用 OpenAI，並發送到 Telegram
    """
    print("\n=== 📝 自定義故事圖片生成（無需 OpenAI） ===")
    
    # 🔍 智能路徑檢測：先檢查當前目錄，再檢查父目錄
    filename = "my_custom_story.txt"
    possible_paths = [
        filename,  # 當前目錄
        os.path.join("..", filename),  # 父目錄
        os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)  # 腳本父目錄
    ]
    
    # 找到第一個存在的檔案
    actual_file = None
    for path in possible_paths:
        if os.path.exists(path):
            actual_file = path
            print(f"✅ 找到故事檔案：{os.path.abspath(path)}")
            break
    
    if not actual_file:
        print(f"❌ 找唔到 {filename} 檔案")
        print(f"💡 已搜尋以下位置:")
        for path in possible_paths:
            print(f"   - {os.path.abspath(path)}")
        print(f"💡 請確保 {filename} 檔案存在並包含你嘅故事內容")
        return False
    
    filename = actual_file  # 使用找到的檔案路徑
    
    # 初始化環境變量和 Telegram
    try:
        clients = setup_environment()
        print("✅ Telegram 環境初始化成功")
    except Exception as e:
        print(f"⚠️ Telegram 環境初始化錯誤：{e}")
        print("📝 將跳過 Telegram 發送，只生成圖片")
        clients = None
    
    try:
        # 驗證故事格式
        print("🔍 驗證故事格式...")
        is_valid, message = validate_custom_story_format(filename)
        if not is_valid:
            print(f"❌ 故事格式錯誤: {message}")
            print(f"💡 請檢查 {filename} 的格式")
            return False
        
        # 讀取故事內容
        print(f"📖 讀取故事內容 ({filename})...")
        story_data = read_custom_story(filename)
        
        if 'error' in story_data:
            print(f"❌ 讀取錯誤: {story_data['error']}")
            print(f"💡 建議: {story_data['suggestion']}")
            return False
        
        # 顯示讀取到的內容摘要
        print("✅ 成功讀取故事")
        print(f"📰 標題: {story_data['title']}")
        print(f"📄 內容長度: {len(story_data['content'])} 字符")
        print(f"❓ 結論: {story_data['conclusion']}")
        print(f"🏷️ 關鍵詞: {', '.join(story_data['keywords'])}")
        print("🎯 模式: 100% 原文保留，不做任何修改")
        
        # 使用故事數據中的視角信息
        perspective = story_data.get('perspective', 'female')
        
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
        
        # 準備所有內容部分
        content_parts = story_data['content_parts']
        
        templates = {
            'title': generate_exact_custom_template(
                story_data['title'], 
                template_type="title",
                perspective=perspective
            )
        }
        
        # 為每個內容部分生成模板
        for i, content_part in enumerate(content_parts, 1):
            if content_part.strip():  # 只處理非空內容
                templates[f'story{i}'] = generate_exact_custom_template(
                    content_part, 
                    template_type="content",
                    perspective=perspective
                )
        
        # 結論模板
        templates['conclusion'] = generate_exact_custom_template(
            story_data['conclusion'], 
            template_type="conclusion",
            perspective=perspective
        )
        
        # 結尾模板
        templates['end'] = generate_exact_custom_template(
            "完", 
            template_type="end",
            perspective=perspective
        )
        
        # 生成圖片
        print("\n=== 🖼️ 生成圖片 ===")
        
        # 使用 await 運行圖片生成
        image_files = await generate_images_from_templates(templates, perspective)
        
        if image_files:
            print(f"✅ 成功生成 {len(image_files)} 張圖片")
            for i, img_file in enumerate(image_files, 1):
                print(f"  📄 {i}. {os.path.abspath(img_file)}")
            
            # 嘗試發送到 Telegram
            if clients:
                print("\n=== 📱 發送到 Telegram ===")
                try:
                    # 創建 Telegram 標題
                    telegram_caption = f"📱 自定義故事分享\n📰 {story_data['title']}\n🎯 100% 原文保留，不做任何修改"
                    
                    success = await send_telegram_photos(
                        clients['telegram_bot'], 
                        clients['telegram_chat_id'], 
                        image_files, 
                        telegram_caption
                    )
                    if success:
                        print("✅ 已發送到 Telegram")
                    else:
                        print("⚠️ Telegram 發送失敗，但圖片已成功生成")
                except Exception as e:
                    print(f"⚠️ Telegram 發送錯誤: {e}")
                    print("💡 圖片已成功生成，可手動發送")
            else:
                print("\n=== 📱 圖片生成完成 ===")
                print("💡 圖片已成功生成，Telegram 未配置")
            
            # 記錄生成信息
            story_data['generation_method'] = "用戶自定義故事（原文不變）"
            story_data['generated_files'] = image_files
            story_data['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"\n📄 生成方法: {story_data['generation_method']}")
            print("✅ 自定義故事處理完成！")
            return True
        else:
            print("❌ 沒有成功生成任何圖片")
            return False
            
    except Exception as e:
        print(f"❌ 生成過程發生錯誤: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    asyncio.run(generate_custom_story_images())
