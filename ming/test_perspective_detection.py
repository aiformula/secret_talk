#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
視角檢測測試腳本
Test perspective detection for custom stories
"""

import os
import sys
import io

# Fix Windows console encoding issues
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from custom_story_reader import read_custom_story, verify_story_perspective

def test_perspective_detection():
    """
    測試視角檢測功能
    """
    print("=" * 60)
    print("🧪 視角檢測測試工具")
    print("=" * 60)
    
    # 測試所有可能的故事檔案
    test_files = [
        "my_custom_story.txt",  # 當前目錄
        "../my_custom_story.txt",  # 父目錄
        "my_custom_story_boy.txt",  # 男性視角
        "my_custom_story_girl.txt",  # 女性視角
    ]
    
    found_files = []
    
    # 檢查哪些檔案存在
    print("\n📁 搜尋故事檔案...")
    for file in test_files:
        if os.path.exists(file):
            abs_path = os.path.abspath(file)
            found_files.append((file, abs_path))
            print(f"   ✅ 找到: {abs_path}")
    
    if not found_files:
        print("\n❌ 找不到任何故事檔案！")
        print("💡 請確保以下檔案之一存在：")
        for file in test_files:
            print(f"   - {os.path.abspath(file)}")
        return
    
    print(f"\n✅ 找到 {len(found_files)} 個故事檔案\n")
    print("=" * 60)
    
    # 測試每個找到的檔案
    for file_path, abs_path in found_files:
        print(f"\n{'=' * 60}")
        print(f"📝 測試檔案: {os.path.basename(file_path)}")
        print(f"📍 完整路徑: {abs_path}")
        print('=' * 60)
        
        try:
            # 使用驗證函數
            verify_story_perspective(file_path)
            
        except Exception as e:
            print(f"❌ 測試失敗: {e}")
            import traceback
            traceback.print_exc()
        
        print("\n")
    
    print("=" * 60)
    print("✅ 測試完成！")
    print("=" * 60)

if __name__ == "__main__":
    test_perspective_detection()

