#!/usr/bin/env python3
"""
測試使用具體故事概念的生成器
Test the generator with a specific story concept from story_ideas.txt template
"""

import asyncio
import json
from simple_story_generator import generate_simple_story

async def test_with_specific_concept():
    """測試具體故事概念"""
    
    # 使用一個具體的故事概念來測試
    story_concept = "我今年23歲，發現我24歲嘅男朋友派帽俾我。呢件事搞到我 final year 讀唔到書，甚至要問朋友借錢交學費。我而家開始懷疑呢段關係係咪一場遊戲。"
    
    print("=== 🎯 測試 story_ideas.txt 天條第一誡 ===")
    print("測試範例故事概念，確保 100% 跟足內容\n")
    
    print(f"📖 故事概念：")
    print(f"「{story_concept}」")
    print("\n⏳ 使用天條第一誡生成...")
    
    try:
        result = await generate_simple_story(story_concept)
        
        print("✅ 生成成功！")
        print("\n=== 📋 結果分析 ===")
        print(f"📰 標題：{result.get('標題', 'N/A')}")
        print(f"📄 內容長度：{len(result.get('內容', ''))} 字")
        print(f"❓ 結論：{result.get('結論', 'N/A')}")
        print(f"🔧 生成方法：{result.get('生成方法', 'N/A')}")
        
        print("\n=== 📄 完整內容 ===")
        print(f"內容：{result.get('內容', 'N/A')}")
        
        print("\n=== 📋 完整 JSON ===")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
        # 保存結果
        with open('test_story_concept_result.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print("\n💾 結果已保存到：test_story_concept_result.json")
        
        # 檢查是否跟足故事概念
        content = result.get('內容', '')
        print("\n=== ✅ 檢查是否跟足故事概念 ===")
        
        checks = {
            "提及年齡 (23歲/24歲)": "23" in content or "24" in content,
            "提及派帽": "派帽" in content or "綠帽" in content or "呃" in content,
            "提及 final year": "final year" in content or "final" in content,
            "提及學費/借錢": "學費" in content or "借錢" in content or "錢" in content,
            "提及懷疑關係": "懷疑" in content or "遊戲" in content or "關係" in content,
        }
        
        for check, passed in checks.items():
            status = "✅" if passed else "❌"
            print(f"{status} {check}: {'通過' if passed else '未通過'}")
        
        return result
        
    except Exception as e:
        print(f"❌ 生成失敗：{str(e)}")
        return None

if __name__ == "__main__":
    asyncio.run(test_with_specific_concept()) 