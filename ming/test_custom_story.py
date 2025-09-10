#!/usr/bin/env python3
"""
🧪 測試自定義故事功能
"""

import asyncio
from custom_story_reader import read_custom_story, validate_custom_story_format

def test_custom_story_reader():
    """測試自定義故事讀取器"""
    print("=== 🎭 測試自定義故事讀取器 ===")
    
    # 驗證檔案格式
    print("🔍 驗證故事格式...")
    is_valid, message = validate_custom_story_format()
    
    if is_valid:
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")
        return
    
    # 讀取故事內容
    print("\n📖 讀取故事內容...")
    story_data = read_custom_story()
    
    if 'error' in story_data:
        print(f"❌ 錯誤: {story_data['error']}")
        print(f"💡 建議: {story_data['suggestion']}")
        return
    
    # 顯示讀取結果
    print("✅ 成功讀取故事")
    print(f"📰 標題: {story_data['title']}")
    print(f"📄 內容長度: {len(story_data['content'])} 字符")
    print(f"📝 內容部分數: {len(story_data['content_parts'])}")
    print(f"❓ 結論: {story_data['conclusion']}")
    print(f"🏷️ 關鍵詞: {', '.join(story_data['keywords'])}")
    print(f"🔧 生成方法: {story_data['generation_method']}")
    
    print("\n📄 內容分割:")
    for i, part in enumerate(story_data['content_parts']):
        if part.strip():
            print(f"  Part {i+1}: {part[:50]}...")
        else:
            print(f"  Part {i+1}: (空)")
    
    return story_data

async def test_full_custom_generation():
    """測試完整自定義內容生成流程"""
    print("\n=== 🚀 測試完整生成流程 ===")
    
    try:
        from relationship_main import generate_custom_story_content
        await generate_custom_story_content()
    except ImportError as e:
        print(f"❌ 導入錯誤: {e}")
    except Exception as e:
        print(f"❌ 執行錯誤: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # 測試讀取器
    test_custom_story_reader()
    
    # 測試完整流程
    print("\n" + "="*50)
    asyncio.run(test_full_custom_generation()) 