#!/usr/bin/env python3
"""
測試 Cosplay 故事生成
"""

import asyncio
import json
from simple_story_generator import generate_simple_story

async def test_cosplay_story():
    """測試 cosplay 故事概念"""
    
    print("=== 🎭 測試 Cosplay 故事生成 ===")
    
    story_concept = "我明白cosplay係好 係興趣 但著唔得點解重要行出街 雖然好仆街 但係香港d cosplayer 真係唔得囉 我會覺得佢影響緊個角色"
    
    print(f"📖 測試概念: {story_concept}")
    print("⏳ 生成中...")
    
    try:
        result = generate_simple_story(story_concept)
        
        print("✅ 生成成功！")
        print(f"🎯 生成方法: {result.get('生成方法', '未知')}")
        print(f"📰 標題: {result.get('標題', '未知')}")
        print(f"📄 內容: {result.get('內容', '未知')[:100]}...")
        print(f"❓ 結論: {result.get('結論', '未知')}")
        
        # 檢查是否包含 cosplay 相關內容
        content = result.get('內容', '')
        if 'cosplay' in content.lower() or 'cos' in content:
            print("✅ 內容包含 cosplay 相關字眼")
        else:
            print("❌ 內容唔包含 cosplay，可能仍然用緊舊模板")
            
        return result
        
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        return None

if __name__ == "__main__":
    asyncio.run(test_cosplay_story()) 