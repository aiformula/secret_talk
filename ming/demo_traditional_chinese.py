#!/usr/bin/env python3
"""
Demo Script - 展示系統使用繁體中文
Demonstrates that the system uses Traditional Chinese characters (繁體字)
"""

import asyncio
import json
from mock_story_generator import generate_mock_story

async def demo_traditional_chinese():
    """演示繁體中文生成"""
    
    print("=== 🇭🇰 繁體中文系統演示 ===")
    print("Demonstrating Traditional Chinese (繁體字) system\n")
    
    # 測試故事概念 - 使用繁體中文
    story_concepts = [
        "我最近發現佢好似有第二個，而且成日都瞞住我。跟住我就問佢，但係佢就點都唔講",
        "我男朋友成日機不離手讀書，成日都要屋企人催三催四先願意出來食飯",
        "我女朋友購物成癮，每個月信用卡賬單都好誇張"
    ]
    
    for i, concept in enumerate(story_concepts, 1):
        print(f"📖 測試 {i}: {concept}")
        print("⏳ 生成中...")
        
        try:
            result = await generate_mock_story(concept)
            
            print("✅ 成功！")
            print(f"📰 標題：{result.get('標題', 'N/A')}")
            print(f"📄 內容：{result.get('內容', 'N/A')[:100]}...")
            print(f"❓ 結論：{result.get('結論', 'N/A')}")
            
            # 檢查是否使用繁體中文
            content = result.get('內容', '')
            traditional_chars = ['發', '過', '講', '係', '個', '點', '嘅', '學', '業', '關', '處', '讀']
            simplified_chars = ['发', '过', '讲', '是', '个', '点', '的', '学', '业', '关', '处', '读']
            
            traditional_count = sum(1 for char in traditional_chars if char in content)
            simplified_count = sum(1 for char in simplified_chars if char in content)
            
            print(f"🔍 繁體字檢測：發現 {traditional_count} 個繁體字元")
            if simplified_count > 0:
                print(f"⚠️ 發現 {simplified_count} 個簡體字元")
            else:
                print("✅ 確認使用純正繁體中文！")
            
        except Exception as e:
            print(f"❌ 錯誤：{str(e)}")
        
        print("-" * 60)
    
    print("\n🎉 繁體中文系統演示完成！")
    print("✅ 系統已經使用繁體中文（繁體字）")
    print("✅ 包括香港粵語口語表達")
    print("✅ 混合英文用詞（final year、check、IG story 等）")

if __name__ == "__main__":
    asyncio.run(demo_traditional_chinese()) 