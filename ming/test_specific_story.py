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

async def test_specific_story():
    """Test the first story specifically"""
    print("=== 測試第1個故事（ChatGPT出軌故事）===")
    
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
    print("\n=== 生成內容 ===")
    try:
        content_data = await generate_varied_relationship_content(
            clients['openai_client'], story_index=0
        )
        
        print(f"📰 標題：{content_data['title_content']['title']}")
        print(f"🎣 鉤子：{content_data['story_content']['hook']}")
        print(f"📖 故事要點數量：{len(content_data['story_content']['story_points'])}")
        
        for i, point in enumerate(content_data['story_content']['story_points'], 1):
            print(f"\n{i}. {point['title']}")
            print(f"   描述：{point['description'][:100]}...")
        
        print(f"💭 結論：{content_data['conclusion_content']['conclusion'][:100]}...")
        print(f"📱 IG Caption：{content_data['ig_caption'][:100]}...")
        
        # Check if content follows original story
        print("\n=== 內容跟隨檢查 ===")
        original_keywords = ['ChatGPT', '出軌', '隱瞞', 'AI', '蠢']
        generated_text = " ".join([
            content_data['title_content']['title'],
            content_data['story_content']['hook'],
            " ".join([point['description'] for point in content_data['story_content']['story_points']]),
            content_data['conclusion_content']['conclusion'],
            content_data['ig_caption']
        ])
        
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
        print(f"❌ 內容生成失敗：{e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_specific_story()) 