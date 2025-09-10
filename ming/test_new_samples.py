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

async def test_new_samples():
    """Test the newly added story samples"""
    print("=== 測試新加入嘅故事樣本 ===")
    
    # Setup environment
    clients = setup_environment()
    
    # Show all available scenarios
    print(f"📊 總共有 {len(STORY_SCENARIOS)} 個故事樣本")
    
    # Show new samples
    new_samples = [
        "工作被炒",
        "網絡發現秘密", 
        "健身後性行為",
        "婚前性行為觀念",
        "朋友窺探隱私",
        "女朋友無理取鬧",
        "女朋友過度反應",
        "性癖困擾"
    ]
    
    print(f"\n🆕 新加入嘅樣本：{len(new_samples)} 個")
    for i, theme in enumerate(new_samples, 1):
        print(f"{i}. {theme}")
    
    # Test a few new samples
    test_samples = [8, 9, 10, 11]  # Index of new samples in STORY_SCENARIOS
    
    for sample_index in test_samples:
        if sample_index < len(STORY_SCENARIOS):
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
            
    except Exception as e:
        print(f"❌ 載入失敗：{e}")
    
    print("\n=== 測試完成 ===")

if __name__ == "__main__":
    asyncio.run(test_new_samples()) 