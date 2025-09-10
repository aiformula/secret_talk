#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📝 故事檔案同步工具
解決用戶編輯故事後系統仍顯示舊內容的問題
"""

import os
import shutil
from datetime import datetime

def show_story_files():
    """顯示所有故事檔案內容"""
    print("=== 📂 當前故事檔案狀況 ===")
    
    files_to_check = [
        "my_custom_story.txt",
        "ming/my_custom_story.txt"
    ]
    
    for file_path in files_to_check:
        print(f"\n📍 檔案: {file_path}")
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                print(f"✅ 存在 ({len(lines)} 行)")
                print(f"🏷️ 標題: {lines[0].strip() if lines else '(空檔案)'}")
                if len(lines) > 2:
                    print(f"📝 開頭: {lines[2].strip()[:50]}..." if len(lines[2].strip()) > 50 else f"📝 開頭: {lines[2].strip()}")
                print(f"📅 修改時間: {datetime.fromtimestamp(os.path.getmtime(file_path))}")
            except Exception as e:
                print(f"❌ 讀取錯誤: {e}")
        else:
            print("❌ 不存在")

def sync_from_main_to_ming():
    """從主目錄同步到 ming 目錄"""
    source = "my_custom_story.txt"
    dest = "ming/my_custom_story.txt"
    
    if not os.path.exists(source):
        print(f"❌ 源檔案不存在: {source}")
        return False
    
    try:
        # 創建備份
        if os.path.exists(dest):
            backup = f"ming/my_custom_story_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            shutil.copy2(dest, backup)
            print(f"💾 已備份原檔案到: {backup}")
        
        # 複製檔案
        shutil.copy2(source, dest)
        print(f"✅ 成功同步: {source} → {dest}")
        return True
    except Exception as e:
        print(f"❌ 同步失敗: {e}")
        return False

def sync_from_ming_to_main():
    """從 ming 目錄同步到主目錄"""
    source = "ming/my_custom_story.txt"
    dest = "my_custom_story.txt"
    
    if not os.path.exists(source):
        print(f"❌ 源檔案不存在: {source}")
        return False
    
    try:
        # 創建備份
        if os.path.exists(dest):
            backup = f"my_custom_story_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            shutil.copy2(dest, backup)
            print(f"💾 已備份原檔案到: {backup}")
        
        # 複製檔案
        shutil.copy2(source, dest)
        print(f"✅ 成功同步: {source} → {dest}")
        return True
    except Exception as e:
        print(f"❌ 同步失敗: {e}")
        return False

def create_new_story():
    """創建新故事檔案"""
    print("\n=== 📝 創建新故事 ===")
    print("請輸入故事內容 (按 Ctrl+D 或輸入 'END' 結束):")
    
    lines = []
    try:
        while True:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
    except EOFError:
        pass
    
    if not lines:
        print("❌ 沒有輸入內容")
        return
    
    content = '\n'.join(lines)
    
    # 同時寫入兩個檔案
    for file_path in ["my_custom_story.txt", "ming/my_custom_story.txt"]:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ 已保存到: {file_path}")
        except Exception as e:
            print(f"❌ 保存失敗 {file_path}: {e}")

def main():
    """主程序"""
    while True:
        print("\n" + "="*50)
        print("📝 故事檔案同步工具")
        print("="*50)
        
        print("1. 📂 查看所有故事檔案狀況")
        print("2. ⬇️  從主目錄同步到 ming 目錄")
        print("3. ⬆️  從 ming 目錄同步到主目錄")
        print("4. 📝 創建新故事（同步到兩個位置）")
        print("5. 🚀 測試 Option 6")
        print("0. ❌ 退出")
        
        choice = input("\n請選擇 (0-5): ").strip()
        
        if choice == "0":
            print("👋 再見！")
            break
        elif choice == "1":
            show_story_files()
        elif choice == "2":
            sync_from_main_to_ming()
        elif choice == "3":
            sync_from_ming_to_main()
        elif choice == "4":
            create_new_story()
        elif choice == "5":
            print("🚀 準備測試 Option 6...")
            os.system("echo 6 | python ming/relationship_main.py")
        else:
            print("❌ 無效選擇")

if __name__ == "__main__":
    main() 