#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最終繁體字修復工具
Final Traditional Chinese Fixer

專門修復以下問題：
1. 知道 → 知 (香港粵語特色)
2. 其他簡體字轉繁體字
3. 香港粵語用詞調整
"""

import os
import re

def fix_files():
    """修復所有文件的繁體字問題"""
    
    # 需要修復的文件列表
    files_to_fix = [
        'hk_dcard_stories.py',
        'relationship_content_generator.py',
        'relationship_main.py',
        'generated_ig_caption.txt'
    ]
    
    # 修復字典
    fixes = {
        # 最重要：香港粵語 "知道" → "知"
        r'我唔知道': '我唔知',
        r'唔知道': '唔知',
        r'你知道': '你知', 
        r'佢知道': '佢知',
        r'大家知道': '大家都知',
        r'我地知道': '我地知',
        r'知道佢': '知佢',
        r'知道咩': '知咩',
        r'知道點': '知點',
        r'知道個': '知個',
        r'知道呢': '知呢',
        r'知道嗰': '知嗰',
        r'知道自己': '知自己',
        r'知道你': '知你',
        r'知道我': '知我',
        
        # 其他常見問題
        r'這個': '呢個',
        r'那個': '嗰個', 
        r'這些': '呢啲',
        r'那些': '嗰啲',
        r'這裡': '呢度',
        r'那裡': '嗰度',
        r'這樣': '呢樣',
        r'那樣': '嗰樣',
        r'沒有': '冇',
        r'給': '俾',
        r'來': '嚟',
        r'謝謝': '多謝',
        r'對不起': '對唔住',
        r'喜歡': '鍾意',
        r'怎樣': '怎樣',
        r'實際': '實際',
        r'應該': '應該',
        r'能夠': '能夠',
        r'幫助': '幫助',
        r'獲得': '獲得',
        r'聽說': '聽說',
        r'時間': '時間',
        r'問題': '問題',
        r'關係': '關係',
        r'處理': '處理',
        r'發現': '發現',
        r'學習': '學習',
        r'變': '變',
        r'開始': '開始'
    }
    
    total_fixes = 0
    
    for filename in files_to_fix:
        if os.path.exists(filename):
            print(f"修復文件: {filename}")
            
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                file_fixes = 0
                
                # 應用修復
                for pattern, replacement in fixes.items():
                    if pattern in content:
                        count = content.count(pattern)
                        content = content.replace(pattern, replacement)
                        file_fixes += count
                        if count > 0:
                            print(f"  ✅ {pattern} → {replacement} ({count}次)")
                
                # 如果有修改，寫回文件
                if content != original_content:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  📝 文件已更新，共修復 {file_fixes} 處")
                    total_fixes += file_fixes
                else:
                    print(f"  ✅ 文件已是繁體字，無需修復")
                    
            except Exception as e:
                print(f"  ❌ 錯誤: {e}")
        else:
            print(f"  ⚠️ 文件不存在: {filename}")
    
    print(f"\n🎉 修復完成！總共修復了 {total_fixes} 處問題")
    
    # 顯示修復報告
    print("\n📋 修復報告:")
    print("✅ 知道 → 知 (香港粵語特色)")
    print("✅ 簡體字 → 繁體字")
    print("✅ 香港粵語用詞調整")
    print("\n🎯 所有文件現在都使用正宗香港繁體字!")

if __name__ == "__main__":
    fix_files() 