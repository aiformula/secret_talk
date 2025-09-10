#!/usr/bin/env python3
"""
繁體中文修復工具 - Traditional Chinese Fixer
找出並修復所有簡體中文字符
"""

import os
import re
from pathlib import Path

# 簡體轉繁體對應表
SIMPLIFIED_TO_TRADITIONAL = {
    # 常見簡體字轉繁體字
    '变': '變',
    '变得': '變得',
    '变成': '變成',
    '开始': '開始',
    '这样': '這樣',
    '没有': '沒有',
    '还是': '還是',
    '应该': '應該',
    '听说': '聽說',
    '怎么': '怎麼',
    '发现': '發現',
    '关系': '關係',
    '学习': '學習',
    '学业': '學業',
    '读书': '讀書',
    '读': '讀',
    '处理': '處理',
    '讲话': '講話',
    '讲得': '講得',
    '说话': '說話',
    '说': '說',
    '过': '過',
    '过程': '過程',
    '经过': '經過',
    '时间': '時間',
    '时候': '時候',
    '吃了': '食咗',
    '吃了没': '食咗飯未',
    '吃了沒': '食咗飯未',
    '晚安': 'good night',  # 更香港化
    '讲': '講',
    '谈': '談',
    '谈话': '談話',
    '说明': '說明',
    '解释': '解釋',
    '认识': '認識',
    '认为': '認為',
    '觉得': '覺得',
    '问题': '問題',
    '问': '問',
    '听': '聽',
    '见': '見',
    '看见': '看見',
    '发生': '發生',
    '发展': '發展',
    '发觉': '發覺',
    '发现': '發現',
    '计划': '計劃',
    '计': '計',
    '让': '讓',
    '让人': '讓人',
    '给': '給',
    '给你': '俾你',
    '给我': '俾我',
    '给他': '俾佢',
    '给她': '俾佢',
    '对': '對',
    '对于': '對於',
    '对不起': '對唔住',
    '谢谢': '多謝',
    '再见': '再見',
    '欢迎': '歡迎',
    '电话': '電話',
    '电脑': '電腦',
    '电': '電',
    '买': '買',
    '卖': '賣',
    '钱': '錢',
    '挣钱': '搵錢',
    '赚钱': '搵錢',
    '工作': '工作',
    '学校': '學校',
    '老师': '老師',
    '学生': '學生',
    '朋友': '朋友',
    '爱情': '愛情',
    '爱': '愛',
    '喜欢': '鍾意',
    '喜': '喜',
    '欢': '歡',
    '乐': '樂',
    '快乐': '快樂',
    '高兴': '高興',
    '开心': '開心',
    '担心': '擔心',
    '紧张': '緊張',
    '压力': '壓力',
    '烦恼': '煩惱',
    '烦': '煩',
    '难': '難',
    '难过': '難過',
    '简单': '簡單',
    '复杂': '複雜',
    '复': '復',
    '报告': '報告',
    '报': '報',
    '写': '寫',
    '写作': '寫作',
    '阅读': '閱讀',
    '读': '讀',
    '看': '睇',
    '观看': '觀看',
    '观': '觀',
    '听': '聽',
    '说': '講',
    '讲': '講',
}

def fix_traditional_chinese_in_file(file_path):
    """修復檔案中的簡體字"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 逐個替換簡體字
        for simplified, traditional in SIMPLIFIED_TO_TRADITIONAL.items():
            content = content.replace(simplified, traditional)
        
        # 如果有變更，寫回檔案
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ 處理檔案 {file_path} 時出錯：{e}")
        return False

def scan_and_fix_directory(directory):
    """掃描目錄並修復所有檔案"""
    fixed_files = []
    
    # 要處理的檔案類型
    file_extensions = ['.py', '.txt', '.md', '.json']
    
    for root, dirs, files in os.walk(directory):
        # 跳過一些不需要處理的目錄
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        for file in files:
            file_path = os.path.join(root, file)
            
            # 檢查檔案副檔名
            if any(file.endswith(ext) for ext in file_extensions):
                if fix_traditional_chinese_in_file(file_path):
                    fixed_files.append(file_path)
    
    return fixed_files

def main():
    """主函數"""
    print("=== 🇭🇰 繁體中文修復工具 ===")
    print("正在掃描並修復簡體中文字符...\n")
    
    # 掃描當前目錄
    current_dir = '.'
    fixed_files = scan_and_fix_directory(current_dir)
    
    if fixed_files:
        print(f"✅ 已修復 {len(fixed_files)} 個檔案：")
        for file_path in fixed_files:
            print(f"   📝 {file_path}")
    else:
        print("✅ 所有檔案已經是正確的繁體中文！")
    
    print("\n🎉 繁體中文修復完成！")
    
    # 檢查常見問題字符
    print("\n=== 📋 常見轉換對應表 ===")
    key_conversions = {
        '变得': '變得',
        '发现': '發現',
        '关系': '關係',
        '学业': '學業',
        '处理': '處理',
        '吃了没': '食咗飯未',
        '晚安': 'good night',
        '给你': '俾你',
        '对不起': '對唔住',
        '谢谢': '多謝',
        '喜欢': '鍾意',
        '看': '睇',
        '说': '講'
    }
    
    for simplified, traditional in key_conversions.items():
        print(f"   {simplified} → {traditional}")

if __name__ == "__main__":
    main() 