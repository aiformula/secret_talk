#!/usr/bin/env python3
"""
超簡易生成器測試
Test script for Simple Story Generator
"""

import asyncio
import json
from simple_story_generator import generate_simple_story

async def test_with_examples():
    """用示例故事測試"""
    
    examples = [
        "我發現我24歲嘅男朋友派帽俾我，影響到我 final year 嘅學業。",
        "我沉迷社交媒體，日日都要影相打卡，但我男朋友覺得我哋個relationship變咗好假。",
        "我最近網購成癮，每個月信用卡賬單都好誇張，我男朋友開始擔心。",
        "我男朋友成日打機，連約會都唔肯放低手機，我覺得好無奈。",
        "我女朋友太完美主義，咩都要criticize，搞到我好大壓力。"
    ]
    
    print("=== 🎯 story_ideas.txt 天條第一誡測試 ===")
    print("測試跟足 story_ideas.txt 嘅詳細指令！\n")
    
    for i, story in enumerate(examples, 1):
        print(f"📖 測試 {i}: {story}")
        print("⏳ 生成中...")
        
        try:
            result = await generate_simple_story(story)
            
            print("✅ 成功！")
            print(f"📰 標題：{result.get('標題', 'N/A')}")
            print(f"📄 內容：{result.get('內容', 'N/A')[:100]}...")
            print(f"❓ 結論：{result.get('結論', 'N/A')}")
            print(f"🔧 方法：{result.get('生成方法', 'N/A')}")
            
            # 保存結果
            with open(f'test_simple_result_{i}.json', 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"💾 已保存到：test_simple_result_{i}.json")
            
        except Exception as e:
            print(f"❌ 失敗：{str(e)}")
        
        print("-" * 60)
    
    print("🎉 測試完成！")

async def test_interactive():
    """互動測試"""
    print("=== 🎯 互動測試模式 ===")
    print("請輸入您的【故事概念】（會 100% 跟足）：")
    
    story = input().strip()
    
    if not story:
        print("❌ 請提供故事概念")
        return
    
    print(f"\n📖 故事概念：{story}")
    print("⏳ 使用天條第一誡生成...")
    
    try:
        result = await generate_simple_story(story)
        
        print("✅ 完成！")
        print("\n=== 📋 最終結果 ===")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
        # 保存結果
        with open('test_interactive_result.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print("\n💾 已保存到：test_interactive_result.json")
        
    except Exception as e:
        print(f"❌ 失敗：{str(e)}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        # 互動模式
        asyncio.run(test_interactive())
    else:
        # 預設測試模式
        asyncio.run(test_with_examples()) 