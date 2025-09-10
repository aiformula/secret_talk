#!/usr/bin/env python3
"""
測試 Mock 模式 - 適用於 OpenAI API 不可用的地區
Test Mock Mode for regions where OpenAI API is not available
"""

import asyncio
import json
from simple_story_generator import generate_simple_story

async def test_mock_mode():
    """測試 Mock 模式是否正常工作"""
    
    print("=== 🎭 測試 Mock 模式 ===")
    print("適用於 OpenAI API 不可用的地區\n")
    
    # 測試故事概念
    test_story = "我發現我24歲嘅男朋友派帽俾我，影響到我 final year 嘅學業。"
    
    print(f"📖 測試故事概念：")
    print(f"「{test_story}」")
    print("\n⏳ 生成中...")
    
    try:
        result = await generate_simple_story(test_story)
        
        print("✅ 生成成功！")
        print("\n=== 📋 結果 ===")
        print(f"📰 標題：{result.get('標題', 'N/A')}")
        print(f"📄 內容：{result.get('內容', 'N/A')}")
        print(f"❓ 結論：{result.get('結論', 'N/A')}")
        print(f"🔧 生成方法：{result.get('生成方法', 'N/A')}")
        
        if "Mock" in result.get('生成方法', ''):
            print(f"💡 說明：{result.get('說明', 'N/A')}")
            print(f"🔗 建議：{result.get('建議', 'N/A')}")
        
        print("\n=== 📋 完整 JSON ===")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
        # 保存結果
        with open('test_mock_result.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print("\n💾 結果已保存到：test_mock_result.json")
        
        return result
        
    except Exception as e:
        print(f"❌ 測試失敗：{str(e)}")
        return None

if __name__ == "__main__":
    asyncio.run(test_mock_mode()) 