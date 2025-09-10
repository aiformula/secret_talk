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

async def test_improved_focused_content():
    """Test the improved content generation with focus on conciseness and story adherence"""
    print("=== 測試改善後嘅內容生成（重點：簡潔、直接、跟隨故事）===")
    
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
    print("\n=== 生成改善後內容 ===")
    try:
        content_data = await generate_varied_relationship_content(
            clients['openai_client'], story_index=0
        )
        
        print(f"📰 標題：{content_data['title_content']['title']}")
        print(f"🎣 鉤子：{content_data['story_content']['hook']}")
        print(f"📖 故事要點數量：{len(content_data['story_content']['story_points'])}")
        
        # Check content length and focus
        total_content_length = 0
        for i, point in enumerate(content_data['story_content']['story_points'], 1):
            description_length = len(point['description'])
            total_content_length += description_length
            print(f"\n{i}. {point['title']}")
            print(f"   描述長度：{description_length}字")
            print(f"   描述：{point['description'][:100]}...")
            
            # Check if content is too long
            if description_length > 250:
                print(f"   ⚠️ 描述仍然過長（超過250字）")
            elif description_length < 100:
                print(f"   ⚠️ 描述可能過短（少於100字）")
            else:
                print(f"   ✅ 描述長度適中")
        
        print(f"\n💭 結論：{content_data['conclusion_content']['conclusion']}")
        print(f"📱 IG Caption長度：{len(content_data['ig_caption'])}字")
        
        # Check if content follows original story
        print("\n=== 內容跟隨檢查 ===")
        original_story = first_story['story_template']
        generated_text = " ".join([
            content_data['title_content']['title'],
            content_data['story_content']['hook'],
            " ".join([point['description'] for point in content_data['story_content']['story_points']]),
            content_data['conclusion_content']['conclusion'],
            content_data['ig_caption']
        ])
        
        # Extract key concepts from original story
        original_keywords = []
        if '做愛' in original_story or '無力' in original_story:
            original_keywords.extend(['做愛', '無力', '性', '問題'])
        if '工作' in original_story or '壓力' in original_story:
            original_keywords.extend(['工作', '壓力', '壓力大'])
        if '唔得' in original_story:
            original_keywords.extend(['唔得', '失敗', '問題'])
        
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
        
        # Overall assessment
        print("\n=== 改善效果評估 ===")
        print(f"📊 總內容長度：{total_content_length}字")
        print(f"📊 平均每點長度：{total_content_length // len(content_data['story_content']['story_points'])}字")
        
        if total_content_length < 600:
            print("✅ 內容長度適中，避免過份詳細")
        else:
            print("⚠️ 內容仍然過長，需要進一步縮短")
        
        # Save results to file
        with open('test_improved_focused_result.txt', 'w', encoding='utf-8') as f:
            f.write("=== 改善後內容生成結果 ===\n\n")
            f.write(f"原始故事：{original_story}\n\n")
            f.write(f"標題：{content_data['title_content']['title']}\n")
            f.write(f"鉤子：{content_data['story_content']['hook']}\n\n")
            
            for i, point in enumerate(content_data['story_content']['story_points'], 1):
                f.write(f"{i}. {point['title']}\n")
                f.write(f"   {point['description']}\n\n")
            
            f.write(f"結論：{content_data['conclusion_content']['conclusion']}\n\n")
            f.write(f"IG Caption：\n{content_data['ig_caption']}\n\n")
            f.write(f"總字數：{total_content_length}字\n")
            f.write(f"跟隨故事程度：{len(found_keywords)}/{len(original_keywords)} 關鍵詞匹配\n")
        
        print("💾 結果已保存到 test_improved_focused_result.txt")
            
    except Exception as e:
        print(f"❌ 內容生成失敗：{e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_improved_focused_content()) 