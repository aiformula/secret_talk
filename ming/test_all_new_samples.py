#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import sys
import os

# Add the current directory to the path so we can import the module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from relationship_content_generator import (
    load_story_ideas_from_file,
    generate_varied_relationship_content,
    STORY_SCENARIOS
)
from config import setup_environment

async def test_all_new_samples():
    """Test all the newly added story samples"""
    print("=== 測試所有新加入嘅故事樣本 ===")
    
    # Setup environment
    clients = setup_environment()
    
    # Show all available scenarios
    print(f"📊 總共有 {len(STORY_SCENARIOS)} 個故事樣本")
    
    # Show all new samples (from the second batch)
    new_samples_batch2 = [
        "交友app現實落差",
        "通訊隱私問題", 
        "追蹤KOL",
        "朋友關係變化",
        "心理健康困擾",
        "網絡爭議",
        "交友app詐騙",
        "性慾困擾",
        "物質比較",
        "家庭歧視"
    ]
    
    print(f"\n🆕 第二批新加入嘅樣本：{len(new_samples_batch2)} 個")
    for i, theme in enumerate(new_samples_batch2, 1):
        print(f"{i}. {theme}")
    
    # Find the indices of new samples in STORY_SCENARIOS
    new_sample_indices = []
    for i, scenario in enumerate(STORY_SCENARIOS):
        if scenario['theme'] in new_samples_batch2:
            new_sample_indices.append(i)
    
    print(f"\n📍 新樣本在STORY_SCENARIOS中的索引：{new_sample_indices}")
    
    # Test a few new samples
    test_count = min(3, len(new_sample_indices))  # Test first 3 new samples
    
    for i in range(test_count):
        sample_index = new_sample_indices[i]
        sample = STORY_SCENARIOS[sample_index]
        print(f"\n=== 測試樣本 {sample_index + 1}: {sample['theme']} ===")
        print(f"📝 故事：{sample['story_template'][:100]}...")
        print(f"🎭 主題：{sample['theme']}")
        print(f"👤 視角：{sample.get('perspective', 'female')}")
        
        try:
            # Generate content using this sample
            content_data = await generate_varied_relationship_content(
                clients['openai_client'], story_index=sample_index
            )
            
            print(f"📰 標題：{content_data['title_content']['title']}")
            print(f"🎣 鉤子：{content_data['story_content']['hook']}")
            print(f"📖 故事要點數量：{len(content_data['story_content']['story_points'])}")
            
            # Show first story point
            if content_data['story_content']['story_points']:
                first_point = content_data['story_content']['story_points'][0]
                print(f"📝 第一個要點：{first_point['title']}")
                print(f"   描述：{first_point['description'][:100]}...")
            
            print(f"💭 結論：{content_data['conclusion_content']['conclusion']}")
            print(f"📱 IG Caption：{content_data['ig_caption'][:100]}...")
            
            print("✅ 生成成功")
            
        except Exception as e:
            print(f"❌ 生成失敗：{e}")
    
    # Test loading from story_ideas.txt
    print(f"\n=== 測試從 story_ideas.txt 載入 ===")
    try:
        scenarios = load_story_ideas_from_file()
        print(f"📊 從檔案載入到 {len(scenarios)} 個故事場景")
        
        if scenarios:
            print("📝 第一個故事：")
            print(scenarios[0]['story_template'][:200] + "...")
            
            # Show some new stories from file
            new_stories_in_file = [
                "交友app現實落差",
                "通訊隱私問題",
                "追蹤KOL",
                "朋友關係變化",
                "心理健康困擾",
                "網絡爭議",
                "交友app詐騙",
                "性慾困擾",
                "物質比較",
                "家庭歧視"
            ]
            
            print(f"\n📋 檔案中的新故事：")
            for i, story in enumerate(scenarios):
                if any(new_story in story['story_template'] for new_story in new_stories_in_file):
                    print(f"{i+1}. {story['theme']} - {story['story_template'][:50]}...")
            
    except Exception as e:
        print(f"❌ 載入失敗：{e}")
    
    # Summary
    print(f"\n=== 總結 ===")
    print(f"📊 總樣本數量：{len(STORY_SCENARIOS)}")
    print(f"🆕 第二批新增樣本：{len(new_samples_batch2)}")
    print(f"📈 樣本增長：從20+個增加到{len(STORY_SCENARIOS)}個")
    
    # Save summary to file
    with open('test_all_new_samples_result.txt', 'w', encoding='utf-8') as f:
        f.write("=== 所有新樣本測試結果 ===\n\n")
        f.write(f"總樣本數量：{len(STORY_SCENARIOS)}\n")
        f.write(f"第二批新增樣本：{len(new_samples_batch2)}\n")
        f.write(f"樣本增長：從20+個增加到{len(STORY_SCENARIOS)}個\n\n")
        
        f.write("新增樣本列表：\n")
        for i, theme in enumerate(new_samples_batch2, 1):
            f.write(f"{i}. {theme}\n")
        
        f.write(f"\n測試完成時間：{asyncio.get_event_loop().time()}\n")
    
    print("💾 結果已保存到 test_all_new_samples_result.txt")
    print("\n=== 測試完成 ===")

if __name__ == "__main__":
    asyncio.run(test_all_new_samples()) 