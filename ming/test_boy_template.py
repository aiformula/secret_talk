#!/usr/bin/env python3
"""
🧪 測試男性模板功能
"""

import asyncio
import os
from custom_story_reader import read_custom_story
from relationship_main import generate_custom_story_with_file

async def test_boy_template():
    """測試男性模板功能"""
    print("🧪 測試男性模板功能")
    print("=" * 50)
    
    # 測試檔案名檢測
    print("\n1. 📁 測試檔案名檢測")
    boy_file = "my_custom_story_boy.txt"
    if os.path.exists(boy_file):
        story_data = read_custom_story(boy_file)
        print(f"✅ 成功讀取 {boy_file}")
        print(f"🎭 檢測到的視角: {story_data.get('perspective', 'unknown')}")
        
        if 'perspective_detection' in story_data:
            detection = story_data['perspective_detection']
            print(f"📁 檔案名檢測: {detection['filename']}")
            print(f"📝 內容檢測: {detection['content']}")
            print(f"✅ 最終選擇: {detection['final']}")
    else:
        print(f"❌ 找不到 {boy_file}")
    
    # 測試女性檔案
    print("\n2. 👩 測試女性檔案")
    girl_file = "my_custom_story.txt"
    if os.path.exists(girl_file):
        story_data = read_custom_story(girl_file)
        print(f"✅ 成功讀取 {girl_file}")
        print(f"🎭 檢測到的視角: {story_data.get('perspective', 'unknown')}")
        
        if 'perspective_detection' in story_data:
            detection = story_data['perspective_detection']
            print(f"📁 檔案名檢測: {detection['filename']}")
            print(f"📝 內容檢測: {detection['content']}")
            print(f"✅ 最終選擇: {detection['final']}")
    else:
        print(f"❌ 找不到 {girl_file}")
    
    print("\n3. 🎨 測試模板生成")
    print("注意：這個測試只會檢測視角，不會實際生成圖片")
    
    # 測試男性故事生成（不實際生成圖片）
    if os.path.exists(boy_file):
        print(f"\n🧪 測試 {boy_file} 的視角檢測...")
        try:
            story_data = read_custom_story(boy_file)
            perspective = story_data.get('perspective', 'female')
            print(f"✅ 視角檢測成功: {perspective}")
            print(f"🎯 將使用 {'男性' if perspective == 'male' else '女性'} 模板")
        except Exception as e:
            print(f"❌ 測試失敗: {e}")
    
    print("\n🎉 測試完成！")
    print("💡 如果要實際生成圖片，請運行主程序並選擇選項 6")

if __name__ == "__main__":
    asyncio.run(test_boy_template()) 