#!/usr/bin/env python3

import asyncio
import os
from relationship_content_generator import (
    generate_relationship_title_content,
    generate_relationship_story_content,
    generate_relationship_conclusion_content,
    generate_instagram_caption,
    get_random_story_scenario
)
from config import setup_environment

async def test_improved_content_generation():
    """測試改善後嘅內容生成效果"""
    
    print("=== 🚀 測試改善後嘅AI內容生成 ===")
    
    # 設定環境
    clients = setup_environment()
    
    # 選擇一個測試故事
    test_scenario = {
        "theme": "金錢觀念差異",
        "story_template": """我同男朋友嘅用錢方式好唔同，我鍾意買嘢俾自己，但佢覺得我太大洗。每次出街食飯都會為錢嘈交，佢話我唔識慳錢，我話佢太孤寒。我哋為錢嘈到好傷感情...""",
        "title_examples": ["我哋金錢觀念差好遠？", "佢覺得我太大洗？", "為錢嘈交傷咗感情？"],
        "perspective": "female"
    }
    
    print(f"\n📝 測試故事主題：{test_scenario['theme']}")
    print(f"👤 視角：{test_scenario['perspective']} ({'男性' if test_scenario['perspective'] == 'male' else '女性'})")
    
    try:
        # 測試標題生成
        print("\n=== 🎯 測試標題生成 ===")
        title_content = await generate_relationship_title_content(
            clients['openai_client'], 
            test_scenario['story_template'], 
            test_scenario
        )
        print(f"✅ 生成標題：{title_content['title']}")
        print(f"🏷️ 關鍵詞：{', '.join(title_content['keywords'])}")
        
        # 測試故事內容生成
        print("\n=== 📖 測試故事內容生成 ===")
        story_content = await generate_relationship_story_content(
            clients['openai_client'], 
            test_scenario['story_template'], 
            test_scenario
        )
        print(f"✅ 生成鉤子：{story_content['hook']}")
        print(f"📚 故事要點數量：{len(story_content['story_points'])}")
        for i, point in enumerate(story_content['story_points'], 1):
            print(f"   {i}. {point['title']}")
            print(f"      {point['description'][:100]}...")
        print(f"🏷️ 關鍵詞：{', '.join(story_content['keywords'])}")
        
        # 測試結論生成
        print("\n=== 💭 測試結論生成 ===")
        conclusion_content = await generate_relationship_conclusion_content(
            clients['openai_client'], 
            story_content
        )
        print(f"✅ 生成結論：{conclusion_content['conclusion']}")
        
        # 測試Instagram標題生成
        print("\n=== 📱 測試Instagram標題生成 ===")
        ig_caption_result = await generate_instagram_caption(
            clients['openai_client'], 
            story_content, 
            word_limit=300
        )
        print(f"✅ 生成Instagram標題：")
        print(f"{ig_caption_result['caption'][:200]}...")
        
        # 保存測試結果
        with open('test_improved_content_result.txt', 'w', encoding='utf-8') as f:
            f.write("=== 改善後嘅AI內容生成測試結果 ===\n\n")
            f.write(f"主題：{test_scenario['theme']}\n")
            f.write(f"視角：{test_scenario['perspective']}\n\n")
            
            f.write("=== 標題 ===\n")
            f.write(f"{title_content['title']}\n")
            f.write(f"關鍵詞：{', '.join(title_content['keywords'])}\n\n")
            
            f.write("=== 故事內容 ===\n")
            f.write(f"鉤子：{story_content['hook']}\n\n")
            for i, point in enumerate(story_content['story_points'], 1):
                f.write(f"{i}. {point['title']}\n")
                f.write(f"{point['description']}\n\n")
            f.write(f"關鍵詞：{', '.join(story_content['keywords'])}\n\n")
            
            f.write("=== 結論 ===\n")
            f.write(f"{conclusion_content['conclusion']}\n\n")
            
            f.write("=== Instagram標題 ===\n")
            f.write(ig_caption_result['caption'])
        
        print(f"\n✅ 測試完成！結果已保存到：test_improved_content_result.txt")
        
        return {
            'title': title_content,
            'story': story_content,
            'conclusion': conclusion_content,
            'ig_caption': ig_caption_result
        }
        
    except Exception as e:
        print(f"❌ 測試失敗：{str(e)}")
        return None

async def main():
    """主函數"""
    await test_improved_content_generation()

if __name__ == "__main__":
    asyncio.run(main()) 