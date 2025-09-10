#!/usr/bin/env python3
"""
修復特定問題 - Fix Specific Hong Kong Cantonese Issues
"""

import os
import glob

# 特定修復對應表 - 針對用戶指出的問題
SPECIFIC_FIXES = {
    # 最重要：修復"知道" - 香港人說"我知"不說"我知道"
    "知道": "知",
    "我唔知道": "我唔知", 
    "唔知道": "唔知",
    "你知道": "你知",
    "佢知道": "佢知",
    "大家知道": "大家都知",
    "我地知道": "我地知",
    "知道點": "知點",
    "知道咩": "知咩",
    "知道嘅": "知嘅",
    "知道個": "知個",
    "知道佢": "知佢",
    "知道呢": "知呢",
    "知道嗰": "知嗰",
    "知道自己": "知自己",
    "知道你": "知你",
    "知道我": "知我",
    
    # 其他香港化修正
    "怎样": "怎樣",
    "这样": "這樣", 
    "那样": "那樣",
    "能够": "能夠",
    "应该": "應該",
    "实际": "實際",
    "帮助": "幫助",
    "帮到": "幫到",
    "获得": "獲得",
    "听说": "聽說",
    
    # 動詞香港化
    "来": "嚟",
    "过来": "過嚟", 
    "回来": "返嚟",
    "出来": "出嚟",
    "看来": "睇嚟",
    
    # 常見字詞
    "给": "俾",
    "给你": "俾你",
    "给我": "俾我",
    "给他": "俾佢", 
    "给她": "俾佢",
    "看": "睇",
    "看见": "睇見",
    "看到": "睇到",
    "没有": "冇",
    "还": "仲",
    "还是": "仲係",
    "还有": "仲有",
    "还要": "仲要",
    "喜欢": "鍾意",
    "不喜欢": "唔鍾意",
    "谢谢": "多謝",
    "对不起": "對唔住",
    
    # 其他
    "吃了": "食咗",
    "晚安": "good night",
    "再见": "bye bye",
}

def apply_fixes_to_content(content):
    """應用修復到內容"""
    # 按長度降序排列避免部分匹配
    sorted_fixes = sorted(SPECIFIC_FIXES.items(), key=lambda x: len(x[0]), reverse=True)
    
    for old, new in sorted_fixes:
        content = content.replace(old, new)
    
    return content

def fix_files_in_directory(directory="."):
    """修復目錄中的所有檔案"""
    file_patterns = ["*.py", "*.txt", "*.md"]
    fixed_files = []
    
    for pattern in file_patterns:
        # 搜尋所有匹配的檔案
        files = []
        for root, dirs, filenames in os.walk(directory):
            # 跳過特定目錄
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            
            for filename in filenames:
                if filename.endswith(pattern[1:]):  # 移除 * 
                    files.append(os.path.join(root, filename))
        
        for file_path in files:
            # 跳過特定檔案
            if any(skip in file_path for skip in ['fix_', 'test_', '__pycache__']):
                continue
            
            try:
                # 讀取檔案
                with open(file_path, 'r', encoding='utf-8') as f:
                    original_content = f.read()
                
                # 應用修復
                fixed_content = apply_fixes_to_content(original_content)
                
                # 如果有變更，寫回檔案
                if fixed_content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(fixed_content)
                    fixed_files.append(file_path)
                    
            except Exception as e:
                print(f"錯誤處理 {file_path}: {e}")
    
    return fixed_files

# 執行修復
if __name__ == "__main__":
    print("🇭🇰 修復香港粵語特定問題...")
    fixed_files = fix_files_in_directory()
    
    if fixed_files:
        print(f"✅ 已修復 {len(fixed_files)} 個檔案")
        for f in fixed_files[:5]:  # 顯示前5個
            print(f"  • {f}")
        if len(fixed_files) > 5:
            print(f"  ... 還有 {len(fixed_files) - 5} 個檔案")
    else:
        print("✅ 所有檔案已經是正確的香港粵語格式")
    
    print("\n🎉 修復完成！")
    
    # 顯示主要修復
    print("\n主要修復：")
    print("• 知道 → 知 (香港粵語)")
    print("• 给 → 俾 (香港粵語)")
    print("• 看 → 睇 (香港粵語)")
    print("• 没有 → 冇 (香港粵語)")
    print("• 喜欢 → 鍾意 (香港粵語)")
    print("• 来 → 嚟 (香港粵語)") 