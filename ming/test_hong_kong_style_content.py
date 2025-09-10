#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import sys
import os

# Add the current directory to the path so we can import the module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from relationship_content_generator import (
    load_story_ideas_from_file,
    generate_varied_relationship_content
)
from config import setup_environment

async def test_hong_kong_style_content():
    """Test the improved content generation with Hong Kong style, focusing on facts over feelings"""
    print("=== 測試香港風格內容生成（重點：講事情唔講感受，避免尷尬用詞）===")
    
    # Setup environment
    clients = setup_environment()
    
    # Load stories
    scenarios = load_story_ideas_from_file()
    print(f"📊 載入到 {len(scenarios)} 個故事場景")
    
    if not scenarios:
        print("❌ 冇載入到故事")
        return
    
    # Show first story
    first_story = scenarios[0]
    print(f"\n📝 第1個故事：{first_story['story_template']}")
    print(f"🎭 主題：{first_story['theme']}")
    print(f"👤 視角：{first_story['perspective']}")
    
    # Generate content using first story
    print("\n=== 生成香港風格內容 ===")
    try:
        content_data = await generate_varied_relationship_content(
            clients['openai_client'], story_index=0
        )
        
        print(f"📰 標題：{content_data['title_content']['title']}")
        print(f"🎣 鉤子：{content_data['story_content']['hook']}")
        print(f"📖 故事要點數量：{len(content_data['story_content']['story_points'])}")
        
        # Check content for Hong Kong style and fact-based approach
        awkward_phrases = [
            "個心落到好低", "驚慌之中揭露", "但一切都冇影冇蹤", "旺角嘅晚",
            "內心深處", "靈魂深處", "心靈創傷", "情感漩渦", "心碎的聲音",
            "淚水模糊了雙眼", "心如刀割", "痛徹心扉", "撕心裂肺"
        ]
        
        feeling_words = [
            "覺得", "感覺", "感受", "心情", "情緒", "內心", "心裡", "心中",
            "心痛", "心碎", "心酸", "心累", "心煩", "心亂", "心慌", "心驚"
        ]
        
        fact_words = [
            "發生", "做咗", "講咗", "去咗", "返咗", "買咗", "食咗", "瞓咗",
            "見到", "聽到", "睇到", "搵到", "搵唔到", "有", "冇", "係", "唔係"
        ]
        
        total_content = " ".join([
            content_data['title_content']['title'],
            content_data['story_content']['hook'],
            " ".join([point['description'] for point in content_data['story_content']['story_points']]),
            content_data['conclusion_content']['conclusion'],
            content_data['ig_caption']
        ])
        
        print("\n=== 香港風格檢查 ===")
        
        # Check for awkward phrases
        found_awkward = []
        for phrase in awkward_phrases:
            if phrase in total_content:
                found_awkward.append(phrase)
        
        if found_awkward:
            print(f"❌ 發現尷尬用詞：{found_awkward}")
        else:
            print("✅ 冇發現尷尬用詞")
        
        # Check feeling vs fact ratio
        feeling_count = sum(1 for word in feeling_words if word in total_content)
        fact_count = sum(1 for word in fact_words if word in total_content)
        
        print(f"📊 感受詞數量：{feeling_count}")
        print(f"📊 事實詞數量：{fact_count}")
        
        if fact_count > feeling_count:
            print("✅ 內容偏向講事實，符合要求")
        else:
            print("⚠️ 內容仍然太多感受描寫")
        
        # Check Hong Kong style words
        hk_style_words = [
            "佢", "嚟", "咗", "唔", "點", "乜", "嗰", "啲", "俾", "喺", "嘅", "咁",
            "先", "都", "成日", "真係", "好似", "點解", "點算", "冇", "有", "係",
            "唔係", "嘅時候", "嗰陣", "而家", "依家", "咁樣", "搞到", "跟住",
            "之後", "不過", "但係", "雖然"
        ]
        
        hk_style_count = sum(1 for word in hk_style_words if word in total_content)
        print(f"📊 香港風格詞彙數量：{hk_style_count}")
        
        if hk_style_count > 20:
            print("✅ 香港風格詞彙豐富")
        else:
            print("⚠️ 香港風格詞彙不足")
        
        # Display content with analysis
        print("\n=== 生成內容分析 ===")
        for i, point in enumerate(content_data['story_content']['story_points'], 1):
            print(f"\n{i}. {point['title']}")
            print(f"   描述：{point['description']}")
            
            # Check if this point focuses on facts or feelings
            point_feeling_count = sum(1 for word in feeling_words if word in point['description'])
            point_fact_count = sum(1 for word in fact_words if word in point['description'])
            
            if point_fact_count > point_feeling_count:
                print(f"   ✅ 重點講事實（事實詞：{point_fact_count}，感受詞：{point_feeling_count}）")
            else:
                print(f"   ⚠️ 仍然太多感受（事實詞：{point_fact_count}，感受詞：{point_feeling_count}）")
        
        print(f"\n💭 結論：{content_data['conclusion_content']['conclusion']}")
        print(f"📱 IG Caption：{content_data['ig_caption'][:100]}...")
        
        # Overall assessment
        print("\n=== 整體評估 ===")
        if not found_awkward and fact_count > feeling_count and hk_style_count > 20:
            print("✅ 內容符合香港風格要求")
        else:
            print("⚠️ 內容仍需改善")
        
        # Save results to file
        with open('test_hong_kong_style_result.txt', 'w', encoding='utf-8') as f:
            f.write("=== 香港風格內容生成結果 ===\n\n")
            f.write(f"原始故事：{first_story['story_template']}\n\n")
            f.write(f"標題：{content_data['title_content']['title']}\n")
            f.write(f"鉤子：{content_data['story_content']['hook']}\n\n")
            
            for i, point in enumerate(content_data['story_content']['story_points'], 1):
                f.write(f"{i}. {point['title']}\n")
                f.write(f"   {point['description']}\n\n")
            
            f.write(f"結論：{content_data['conclusion_content']['conclusion']}\n\n")
            f.write(f"IG Caption：\n{content_data['ig_caption']}\n\n")
            f.write(f"香港風格詞彙數量：{hk_style_count}\n")
            f.write(f"事實詞數量：{fact_count}\n")
            f.write(f"感受詞數量：{feeling_count}\n")
            f.write(f"尷尬用詞：{found_awkward}\n")
        
        print("💾 結果已保存到 test_hong_kong_style_result.txt")
            
    except Exception as e:
        print(f"❌ 內容生成失敗：{e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_hong_kong_style_content()) 