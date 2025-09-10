#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import sys
import os

# Add the current directory to the path so we can import the module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from relationship_content_generator import (
    load_story_ideas_from_file,
    generate_relationship_story_content,
    generate_relationship_title_content
)
from config import setup_environment

async def test_story_following():
    """Test if generated content follows the original story"""
    print("=== 測試故事跟隨功能 ===")
    
    # Setup environment
    clients = setup_environment()
    
    # Load stories
    scenarios = load_story_ideas_from_file()
    print(f"📊 載入到 {len(scenarios)} 個故事場景")
    
    if not scenarios:
        print("❌ 冇載入到故事")
        return
    
    # Test with first story
    test_scenario = scenarios[0]
    base_story = test_scenario['story_template']
    
    print(f"\n📝 測試故事：{base_story}")
    print(f"🎭 主題：{test_scenario['theme']}")
    print(f"👤 視角：{test_scenario['perspective']}")
    
    # Generate title
    print("\n=== 生成標題 ===")
    try:
        title_content = await generate_relationship_title_content(
            clients['openai_client'], base_story, test_scenario
        )
        print(f"📰 生成標題：{title_content['title']}")
        print(f"🏷️ 關鍵詞：{title_content['keywords']}")
    except Exception as e:
        print(f"❌ 標題生成失敗：{e}")
    
    # Generate story content
    print("\n=== 生成故事內容 ===")
    try:
        story_content = await generate_relationship_story_content(
            clients['openai_client'], base_story, test_scenario
        )
        
        print(f"🎣 鉤子：{story_content['hook']}")
        print(f"📖 故事要點數量：{len(story_content['story_points'])}")
        
        for i, point in enumerate(story_content['story_points'], 1):
            print(f"\n{i}. {point['title']}")
            print(f"   描述：{point['description'][:100]}...")
        
        print(f"🏷️ 關鍵詞：{story_content['keywords']}")
        
        # Check if content follows original story
        print("\n=== 內容跟隨檢查 ===")
        original_keywords = ['ChatGPT', '出軌', '隱瞞', 'AI']
        generated_text = " ".join([point['description'] for point in story_content['story_points']])
        
        found_keywords = []
        for keyword in original_keywords:
            if keyword.lower() in generated_text.lower():
                found_keywords.append(keyword)
        
        print(f"✅ 原始故事關鍵詞：{original_keywords}")
        print(f"✅ 生成內容包含關鍵詞：{found_keywords}")
        
        if len(found_keywords) >= 2:
            print("✅ 生成內容成功跟隨原始故事")
        else:
            print("❌ 生成內容偏離原始故事")
            
    except Exception as e:
        print(f"❌ 故事內容生成失敗：{e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_story_following()) 