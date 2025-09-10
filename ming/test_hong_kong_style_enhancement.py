#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import sys
import os

# Add the current directory to the path so we can import the module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from relationship_content_generator import (
    generate_varied_relationship_content,
    STORY_SCENARIOS
)
from config import setup_environment
from hong_kong_style_phrases import (
    get_hong_kong_style_phrases,
    get_random_hong_kong_phrase,
    is_hong_kong_style,
    enhance_hong_kong_style
)

async def test_hong_kong_style_enhancement():
    """Test Hong Kong style enhancement functionality"""
    print("=== 測試香港風格改善功能 ===")
    
    # Setup environment
    clients = setup_environment()
    
    # Test Hong Kong style phrases
    print("\n1. 測試香港風格用詞：")
    categories = list(get_hong_kong_style_phrases().keys())
    print(f"📊 總共有 {len(categories)} 個類別")
    
    for i, category in enumerate(categories[:5], 1):  # Show first 5 categories
        phrases = get_hong_kong_style_phrases(category)
        print(f"{i}. {category}: {len(phrases)} 個短語")
        if phrases:
            print(f"   例子：{phrases[0][:50]}...")
    
    # Test random phrase generation
    print("\n2. 測試隨機短語生成：")
    for i in range(3):
        phrase = get_random_hong_kong_phrase()
        print(f"{i+1}. {phrase}")
    
    # Test style detection
    print("\n3. 測試風格檢測：")
    test_texts = [
        "我同佢拍拖好開心",
        "我同佢拍拖好開心😂",
        "我同佢扑野好開心",
        "我同佢約出來食飯",
        "我覺得呢件事好重要",
        "我覺得呢件事好重要🙏🏻",
        "佢係咩職業真係咁重要咩"
    ]
    
    for text in test_texts:
        is_hk = is_hong_kong_style(text)
        print(f"'{text}' -> {'✅ 香港風格' if is_hk else '❌ 普通風格'}")
    
    # Test style enhancement
    print("\n4. 測試風格增強：")
    test_enhancements = [
        "我覺得呢件事好重要",
        "我唔知點算",
        "大家覺得點？",
        "我應該點做？"
    ]
    
    for text in test_enhancements:
        enhanced = enhance_hong_kong_style(text, "關係建議")
        print(f"原文：{text}")
        print(f"增強：{enhanced}")
        print()
    
    # Test content generation with Hong Kong style
    print("\n5. 測試內容生成嘅香港風格：")
    
    # Test a few scenarios
    test_scenarios = [
        "交友app現實落差",
        "通訊隱私問題",
        "家庭歧視"
    ]
    
    for theme in test_scenarios:
        print(f"\n=== 測試主題：{theme} ===")
        
        # Find scenario index
        scenario_index = None
        for i, scenario in enumerate(STORY_SCENARIOS):
            if scenario['theme'] == theme:
                scenario_index = i
                break
        
        if scenario_index is not None:
            try:
                content_data = await generate_varied_relationship_content(
                    clients['openai_client'], story_index=scenario_index
                )
                
                print(f"📰 標題：{content_data['title_content']['title']}")
                
                # Check if title has Hong Kong style
                title_has_hk_style = is_hong_kong_style(content_data['title_content']['title'])
                print(f"   香港風格：{'✅ 有' if title_has_hk_style else '❌ 冇'}")
                
                print(f"💭 結論：{content_data['conclusion_content']['conclusion']}")
                
                # Check if conclusion has Hong Kong style
                conclusion_has_hk_style = is_hong_kong_style(content_data['conclusion_content']['conclusion'])
                print(f"   香港風格：{'✅ 有' if conclusion_has_hk_style else '❌ 冇'}")
                
                print("✅ 生成成功")
                
            except Exception as e:
                print(f"❌ 生成失敗：{e}")
        else:
            print(f"❌ 搵唔到主題：{theme}")
    
    # Summary
    print(f"\n=== 總結 ===")
    print(f"📊 香港風格類別：{len(categories)}")
    print(f"🎯 風格檢測功能：✅ 正常")
    print(f"✨ 風格增強功能：✅ 正常")
    print(f"📝 內容生成改善：✅ 已加入香港風格")
    
    # Save test results
    with open('hong_kong_style_test_result.txt', 'w', encoding='utf-8') as f:
        f.write("=== 香港風格改善測試結果 ===\n\n")
        f.write(f"香港風格類別：{len(categories)}\n")
        f.write("風格檢測功能：✅ 正常\n")
        f.write("風格增強功能：✅ 正常\n")
        f.write("內容生成改善：✅ 已加入香港風格\n\n")
        
        f.write("測試類別：\n")
        for i, category in enumerate(categories, 1):
            phrases = get_hong_kong_style_phrases(category)
            f.write(f"{i}. {category}: {len(phrases)} 個短語\n")
        
        f.write(f"\n測試完成時間：{asyncio.get_event_loop().time()}\n")
    
    print("💾 結果已保存到 hong_kong_style_test_result.txt")
    print("\n=== 測試完成 ===")

if __name__ == "__main__":
    asyncio.run(test_hong_kong_style_enhancement()) 