#!/usr/bin/env python3
"""
🎭 自定義故事讀取器 (Custom Story Reader)
用於讀取用戶自定義嘅故事內容，完全唔改動用戶嘅文字
支援男性和女性視角模板自動選擇
"""

import os
import re

def detect_perspective_from_filename(filename):
    """
    從檔案名稱自動檢測視角
    
    Args:
        filename: 檔案名稱
        
    Returns:
        str: "male" 或 "female"
    """
    filename_lower = filename.lower()
    if "boy" in filename_lower or "male" in filename_lower or "男" in filename_lower:
        return "male"
    elif "girl" in filename_lower or "female" in filename_lower or "女" in filename_lower:
        return "female"
    else:
        return "female"  # 預設女性視角

def detect_perspective_from_content(content):
    """
    從故事內容自動檢測視角
    
    Args:
        content: 故事內容
        
    Returns:
        str: "male" 或 "female"
    """
    # 男性視角關鍵詞 (更全面的檢測)
    male_keywords = [
        # 直接稱呼
        "兄弟", "各位兄弟", "大佬", "男仔", "做男人", "兄弟們",
        # 關係描述 (男性視角)
        "識女仔", "女朋友", "女神", "正到不得了", "靚女", "女仔一組",
        "我哋男人", "台灣嘅女仔", "香港嘅女朋友", "同一個女仔",
        # 男性化表達
        "瀨嘢", "仆街", "好對唔住", "戰友", "搞掂", "越軌",
        "Long D", "出咗軌", "心虛", "內疚", "拖過手",
        # 男性特有情境
        "宿舍房", "mid-term presentation", "做project"
    ]
    
    # 女性視角關鍵詞  
    female_keywords = [
        # 直接稱呼
        "絲打", "各位絲打", "姐妹", "女仔", "做女人", "姐妹們",
        # 關係描述 (女性視角)
        "識男仔", "男朋友", "男神", "靚仔", "型男", "男仔一組",
        "我哋女人", "台灣嘅男仔", "香港嘅男朋友", "同一個男仔",
        # 女性化表達
        "好心動", "好sweet", "好romantic", "好溫柔"
    ]
    
    # 計算關鍵詞出現次數
    male_score = sum(1 for keyword in male_keywords if keyword in content)
    female_score = sum(1 for keyword in female_keywords if keyword in content)
    
    # 額外檢查：如果內容提到"女朋友"而不是"男朋友"，很可能是男性視角
    if "女朋友" in content and "男朋友" not in content:
        male_score += 3
    elif "男朋友" in content and "女朋友" not in content:
        female_score += 3
    
    # 檢查Long D (遠距離戀愛) - 通常男性會這樣說
    if "Long D" in content or "long d" in content.lower():
        male_score += 2
    
    print(f"🔍 內容檢測詳情:")
    print(f"   男性關鍵詞得分: {male_score}")
    print(f"   女性關鍵詞得分: {female_score}")
    
    if male_score > female_score:
        return "male"
    elif female_score > male_score:
        return "female"
    else:
        return "female"  # 預設女性視角

def read_custom_story(filename="my_custom_story.txt"):
    """
    讀取用戶自定義嘅故事檔案
    
    Args:
        filename: 故事檔案名稱，支援：
                 - my_custom_story.txt (女性視角)
                 - my_custom_story_boy.txt (男性視角)
                 - 任何包含 boy/male/男 的檔案名 (男性視角)
    
    Returns:
        dict: {
            'title': '標題',
            'content': '主要內容',
            'conclusion': '結尾問句',
            'raw_content': '原始內容',
            'perspective': 'male' 或 'female'
        }
    """
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"找唔到檔案: {filename}")
            
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 過濾掉註釋同空行
        content_lines = []
        for line in lines:
            line = line.strip()
            # 跳過註釋行（以 # 開始）同空行
            if line and not line.startswith('#') and not line.startswith('['):
                content_lines.append(line)
        
        if len(content_lines) < 3:
            raise ValueError("故事內容太短，至少需要標題、內容、結尾")
        
        # 第一行係標題
        title = content_lines[0].strip()
        
        # 最後一行係結尾
        conclusion = content_lines[-1].strip()
        
        # 中間係主要內容
        main_content = '\n\n'.join(content_lines[1:-1]).strip()
        
        # 分割內容做3部分（用於生成圖片）
        content_parts = split_content_for_images(main_content)
        
        # 自動檢測視角
        # 1. 先從檔案名稱檢測
        perspective_from_filename = detect_perspective_from_filename(filename)
        
        # 2. 從內容檢測
        full_content = '\n'.join(content_lines)
        perspective_from_content = detect_perspective_from_content(full_content)
        
        # 3. 檢查是否有手動指定的視角標記
        manual_override = None
        for line in content_lines[:5]:  # 檢查前5行是否有手動標記
            if "# 男性視角" in line or "# male" in line.lower():
                manual_override = "male"
                break
            elif "# 女性視角" in line or "# female" in line.lower():
                manual_override = "female"
                break
        
        # 4. 決定最終視角 (優先級: 手動標記 > 檔案名稱 > 內容檢測)
        if manual_override:
            final_perspective = manual_override
            print(f"✅ 發現手動視角標記: {manual_override}")
        elif "boy" in filename.lower() or "male" in filename.lower() or "男" in filename.lower():
            final_perspective = "male"
        elif "girl" in filename.lower() or "female" in filename.lower() or "女" in filename.lower():
            final_perspective = "female"
        else:
            # 如果檔案名稱沒有明確指定，就用內容檢測的結果
            final_perspective = perspective_from_content
        
        return {
            'title': title,
            'content': main_content,
            'content_parts': content_parts,  # 分割做3部分
            'conclusion': conclusion,
            'raw_content': '\n'.join(content_lines),
            'keywords': extract_keywords_from_content(main_content),
            'generation_method': '用戶自定義故事（原文不變）',
            'perspective': final_perspective,  # 新增：視角信息
            'perspective_detection': {
                'filename': perspective_from_filename,
                'content': perspective_from_content,
                'final': final_perspective
            }
        }
        
    except FileNotFoundError:
        return {
            'error': f'找唔到檔案 {filename}',
            'suggestion': f'請確保 {filename} 存在並包含你嘅故事內容'
        }
    except Exception as e:
        return {
            'error': f'讀取故事時發生錯誤: {str(e)}',
            'suggestion': '請檢查檔案格式係咪正確'
        }

def split_content_for_images(content, target_parts=3):
    """
    將內容分割做指定數量嘅部分（用於生成多張圖片）
    盡量保持每部分長度相近，但唔會打斷句子
    """
    # 按段落分割
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
    
    if len(paragraphs) <= target_parts:
        # 如果段落數少於或等於目標部分數，每個段落一部分
        parts = paragraphs[:]
        # 如果唔夠3部分，用空字符串補足
        while len(parts) < target_parts:
            parts.append("")
        return parts[:target_parts]
    
    # 如果段落太多，需要合併
    total_chars = sum(len(p) for p in paragraphs)
    chars_per_part = total_chars // target_parts
    
    parts = []
    current_part = []
    current_chars = 0
    
    for paragraph in paragraphs:
        current_part.append(paragraph)
        current_chars += len(paragraph)
        
        # 如果當前部分夠長，或者已經係最後一部分
        if (current_chars >= chars_per_part and len(parts) < target_parts - 1) or len(parts) == target_parts - 1:
            parts.append('\n\n'.join(current_part))
            current_part = []
            current_chars = 0
    
    # 處理剩餘內容
    if current_part:
        if parts:
            # 如果已經有部分，將剩餘內容加到最後一部分
            parts[-1] += '\n\n' + '\n\n'.join(current_part)
        else:
            # 如果冇部分，直接作為一部分
            parts.append('\n\n'.join(current_part))
    
    # 確保有足夠嘅部分
    while len(parts) < target_parts:
        parts.append("")
    
    return parts[:target_parts]

def extract_keywords_from_content(content):
    """
    從內容中提取關鍵詞（用於圖片生成）
    """
    # 基本關鍵詞提取（可以根據需要改進）
    keywords = []
    
    # 常見香港用詞
    hk_keywords = [
        'cosplay', 'comic con', '角色扮演', 'costume', 'wig',
        '男朋友', '女朋友', '條仔', '條女', '拍拖', '分手',
        '大學', 'final year', 'assignment', 'staycation',
        'IG', 'story', 'post', 'check', '電話',
        '香港', '廣東話', '繁體字', '英文'
    ]
    
    content_lower = content.lower()
    for keyword in hk_keywords:
        if keyword.lower() in content_lower or keyword in content:
            keywords.append(keyword)
    
    # 限制關鍵詞數量
    return keywords[:10]

def validate_custom_story_format(filename="my_custom_story.txt"):
    """
    驗證自定義故事檔案格式
    """
    try:
        story_data = read_custom_story(filename)
        
        if 'error' in story_data:
            return False, story_data['error']
        
        if not story_data['title']:
            return False, "缺少標題"
        
        if not story_data['content']:
            return False, "缺少主要內容"
        
        if not story_data['conclusion']:
            return False, "缺少結尾問句"
        
        return True, "故事格式正確"
        
    except Exception as e:
        return False, f"驗證時發生錯誤: {str(e)}"

if __name__ == "__main__":
    # 測試功能
    print("=== 🎭 自定義故事讀取器測試 ===")
    
    story = read_custom_story()
    if 'error' in story:
        print(f"❌ 錯誤: {story['error']}")
        print(f"💡 建議: {story['suggestion']}")
    else:
        print(f"✅ 成功讀取故事")
        print(f"📰 標題: {story['title']}")
        print(f"📄 內容長度: {len(story['content'])} 字符")
        print(f"📝 內容部分數: {len(story['content_parts'])}")
        print(f"❓ 結論: {story['conclusion']}")
        print(f"🏷️ 關鍵詞: {', '.join(story['keywords'])}") 