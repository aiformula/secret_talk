#!/usr/bin/env python3
"""
🎭 自定義故事讀取器 (Custom Story Reader)
用於讀取用戶自定義嘅故事內容，完全唔改動用戶嘅文字
支援男性和女性視角模板自動選擇
"""

import os
import re
import datetime

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
    從故事內容自動檢測視角（智能版 - 考慮上下文）
    
    Args:
        content: 故事內容
        
    Returns:
        str: "male" 或 "female"
    """
    male_score = 0
    female_score = 0
    
    # 分割內容為行，以便分析上下文
    lines = content.split('\n')
    full_text = ' '.join(lines)
    
    # 🎯 最強指標：男朋友 vs 女朋友（優先檢測，權重最高）
    boyfriend_count = content.count("男朋友")
    girlfriend_count = content.count("女朋友")
    husband_count = content.count("老公")
    wife_count = content.count("老婆")
    
    # 💡 關鍵改進：檢查「男朋友」是否在第三人稱上下文中（男性視角討論別人）
    # 如果「男朋友」出現在「啲女仔同男朋友」、「女仔嘅男朋友」等上下文中，降低權重
    third_person_boyfriend_patterns = [
        "啲女仔同男朋友", "女仔同男朋友", "女仔嘅男朋友", "女仔的男朋友",
        "見到男朋友", "發現男朋友", "男朋友同", "男朋友喺"
    ]
    third_person_boyfriend_count = sum(full_text.count(p) for p in third_person_boyfriend_patterns)
    
    # 💡 關鍵改進：檢查標題/第一句的關鍵詞（權重加倍）
    first_line = lines[0] if lines else ""
    title_boyfriend = first_line.count("男朋友")
    title_girlfriend = first_line.count("女朋友")
    title_husband = first_line.count("老公")
    title_wife = first_line.count("老婆")
    
    if boyfriend_count > 0:
        # 如果「男朋友」出現在第三人稱上下文中，降低權重
        if third_person_boyfriend_count > 0:
            # 第三人稱上下文中的「男朋友」權重降低（可能是男性視角在討論別人）
            reduced_score = boyfriend_count * 3  # 降低權重到3
            female_score += reduced_score
            print(f"   ⚠️ 發現 '男朋友' {boyfriend_count} 次（{third_person_boyfriend_count}次在第三人稱上下文）→ 女性視角 +{reduced_score} (降權，可能是男性視角討論別人)")
        else:
            # 第一人稱「男朋友」，正常權重
            base_score = boyfriend_count * 10
            title_bonus = title_boyfriend * 10  # 標題出現額外加分
            female_score += base_score + title_bonus
            print(f"   ✅ 發現 '男朋友' {boyfriend_count} 次 → 女性視角 +{base_score}" + 
                  (f" (標題加分 +{title_bonus})" if title_bonus > 0 else ""))
    
    if girlfriend_count > 0:
        base_score = girlfriend_count * 10
        title_bonus = title_girlfriend * 10
        male_score += base_score + title_bonus
        print(f"   ✅ 發現 '女朋友' {girlfriend_count} 次 → 男性視角 +{base_score}" +
              (f" (標題加分 +{title_bonus})" if title_bonus > 0 else ""))
    
    if husband_count > 0:
        base_score = husband_count * 10
        title_bonus = title_husband * 10
        female_score += base_score + title_bonus
        print(f"   ✅ 發現 '老公' {husband_count} 次 → 女性視角 +{base_score}" +
              (f" (標題加分 +{title_bonus})" if title_bonus > 0 else ""))
    
    # 💡 關鍵改進：'老婆' 的上下文分析（降低權重，因為可能是引述別人的話）
    if wife_count > 0:
        # 檢查是否在引號內（別人說的話）
        quoted_wife = 0
        for match in ['「老婆', '『老婆', '"老婆']:
            quoted_wife += full_text.count(match)
        
        # 如果大部分'老婆'都在引號內，降低權重
        if quoted_wife >= wife_count * 0.5:  # 超過一半在引號內
            reduced_score = wife_count * 3  # 降低權重到3
            male_score += reduced_score
            print(f"   ⚠️ 發現 '老婆' {wife_count} 次（{quoted_wife}次在引號內）→ 男性視角 +{reduced_score} (降權)")
        else:
            base_score = wife_count * 10
            title_bonus = title_wife * 10
            male_score += base_score + title_bonus
            print(f"   ✅ 發現 '老婆' {wife_count} 次 → 男性視角 +{base_score}" +
                  (f" (標題加分 +{title_bonus})" if title_bonus > 0 else ""))
    
    # 💡 超強指標：檢查"我+關係詞"組合（最明確的視角指示）
    my_boyfriend_patterns = ["我男朋友", "我個男朋友", "我嘅男朋友"]
    my_girlfriend_patterns = ["我女朋友", "我個女朋友", "我嘅女朋友"]
    my_husband_patterns = ["我老公", "我個老公", "我嘅老公"]
    my_wife_patterns = ["我老婆", "我個老婆", "我嘅老婆"]
    
    my_boyfriend_count = sum(full_text.count(p) for p in my_boyfriend_patterns)
    my_girlfriend_count = sum(full_text.count(p) for p in my_girlfriend_patterns)
    my_husband_count = sum(full_text.count(p) for p in my_husband_patterns)
    my_wife_count = sum(full_text.count(p) for p in my_wife_patterns)
    
    if my_boyfriend_count > 0:
        super_bonus = my_boyfriend_count * 20  # 超高權重
        female_score += super_bonus
        print(f"   🎯 發現 '我+男朋友' {my_boyfriend_count} 次 → 女性視角 +{super_bonus} (確定性證據)")
    
    if my_girlfriend_count > 0:
        super_bonus = my_girlfriend_count * 20
        male_score += super_bonus
        print(f"   🎯 發現 '我+女朋友' {my_girlfriend_count} 次 → 男性視角 +{super_bonus} (確定性證據)")
    
    if my_husband_count > 0:
        super_bonus = my_husband_count * 20
        female_score += super_bonus
        print(f"   🎯 發現 '我+老公' {my_husband_count} 次 → 女性視角 +{super_bonus} (確定性證據)")
    
    if my_wife_count > 0:
        super_bonus = my_wife_count * 20
        male_score += super_bonus
        print(f"   🎯 發現 '我+老婆' {my_wife_count} 次 → 男性視角 +{super_bonus} (確定性證據)")
    
    # 男性視角次要關鍵詞（較低權重）
    male_keywords = [
        # 直接稱呼
        "兄弟", "各位兄弟", "大佬", "兄弟們", "我哋男人", "小弟",
        # 關係描述 (男性視角)
        "識女仔", "女神", "正到不得了", "靚女", "女仔一組",
        "台灣嘅女仔", "香港嘅女朋友", "同一個女仔",
        # 男性化表達
        "瀨嘢", "仆街", "戰友", "搞掂", "越軌",
        "Long D", "出咗軌", "心虛", "內疚",
        # 男性特有情境
        "宿舍房", "mid-term presentation", "做project",
        # 男性視角特有表達
        "好男人", "搵到錢", "年薪", "有車有樓", "操大隻",
        "憑實力單身", "基層", "破處", "叫雞", "未畀人搞過",
        "時間管理大師", "溝", "霸住"
    ]
    
    # 女性視角次要關鍵詞（較低權重）
    female_keywords = [
        # 直接稱呼
        "絲打", "各位絲打", "姐妹", "姐妹們", "我哋女人", "港女", "姨姨", "女仔們",
        # 關係描述 (女性視角)
        "識男仔", "男神", "靚仔", "型男", "男仔一組",
        "台灣嘅男仔", "香港嘅男朋友", "同一個男仔",
        # 女性化表達
        "好心動", "好sweet", "好romantic", "好溫柔", "師姐",
        # 女性勸告/建議場景 (明顯女性視角)
        "奉勸未婚嘅女仔", "想奉勸", "個男仔都好孝順", "娶我", "要戒指",
        "放女朋友第一位"
    ]
    
    # 計算次要關鍵詞出現次數（權重1）
    male_secondary = sum(1 for keyword in male_keywords if keyword in content)
    female_secondary = sum(1 for keyword in female_keywords if keyword in content)
    
    # 💡 關鍵改進：如果發現強烈的男性視角關鍵詞，給予額外加分
    strong_male_indicators = ["小弟", "識女仔", "好男人", "破處", "叫雞", "憑實力單身", "基層", "搵到錢", "年薪"]
    strong_male_count = sum(1 for indicator in strong_male_indicators if indicator in content)
    if strong_male_count >= 3:  # 如果發現3個或以上強烈男性指標
        male_score += strong_male_count * 5  # 額外加分
        print(f"   🎯 發現 {strong_male_count} 個強烈男性視角指標 → 男性視角 +{strong_male_count * 5} (強烈證據)")
    
    male_score += male_secondary
    female_score += female_secondary
    
    print(f"🔍 內容檢測詳情:")
    print(f"   男性關鍵詞得分: {male_score} (主要指標 + 次要關鍵詞)")
    print(f"   女性關鍵詞得分: {female_score} (主要指標 + 次要關鍵詞)")
    
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
        # 確保使用絕對路徑，避免路徑問題
        abs_filename = os.path.abspath(filename)
        
        if not os.path.exists(abs_filename):
            raise FileNotFoundError(f"找唔到檔案: {abs_filename}")
        
        # 顯示文件信息（用於調試）
        file_mtime = os.path.getmtime(abs_filename)
        file_size = os.path.getsize(abs_filename)
        print(f"📄 讀取檔案：{abs_filename}")
        print(f"📅 檔案大小：{file_size} 字節")
        print(f"🕐 最後修改：{datetime.datetime.fromtimestamp(file_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
        
        # 強制重新讀取文件（不使用緩存）
        with open(abs_filename, 'r', encoding='utf-8') as f:
            raw_content = f.read()
            lines = raw_content.splitlines()
        
        # 過濾掉註釋同空行（但保留段落結構）
        content_lines = []
        for line in lines:
            line = line.strip()
            # 跳過註釋行（以 # 開始）同空行
            if line and not line.startswith('#') and not line.startswith('['):
                content_lines.append(line)
        
        if len(content_lines) < 3:
            raise ValueError(f"故事內容太短，至少需要標題、內容、結尾（目前只有 {len(content_lines)} 行）")
        
        # 第一行係標題
        title = content_lines[0].strip()
        
        # 最後一行係結尾
        conclusion = content_lines[-1].strip()
        
        # 中間係主要內容（保留段落結構）
        # 使用原始內容，但只取中間部分
        raw_lines = raw_content.splitlines()
        non_empty_raw_lines = [line.strip() for line in raw_lines if line.strip() and not line.strip().startswith('#') and not line.strip().startswith('[')]
        
        if len(non_empty_raw_lines) >= 3:
            # 找到標題和結論在原始內容中的位置
            title_line_idx = None
            conclusion_line_idx = None
            
            for i, line in enumerate(raw_lines):
                stripped = line.strip()
                if stripped and not stripped.startswith('#') and not stripped.startswith('['):
                    if title_line_idx is None and stripped == title:
                        title_line_idx = i
                    if stripped == conclusion:
                        conclusion_line_idx = i
            
            # 提取中間內容（保留原始格式）
            if title_line_idx is not None and conclusion_line_idx is not None and conclusion_line_idx > title_line_idx:
                middle_lines = raw_lines[title_line_idx + 1:conclusion_line_idx]
                main_content = '\n'.join(middle_lines).strip()
            else:
                # 如果找不到，使用備用方法
                main_content = '\n\n'.join(content_lines[1:-1]).strip()
        else:
            # 備用方法：直接連接中間行
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
    
    # 計算每個段落嘅字數
    paragraph_lengths = [len(p) for p in paragraphs]
    total_chars = sum(paragraph_lengths)
    
    # 設定每頁最佳字數範圍（為6頁內容優化）
    optimal_chars_per_page = 100  # 增加到100字，適合6頁分配
    max_chars_per_page = 140      # 增加到140字，確保完整句子
    min_chars_per_page = 70       # 增加到70字，確保內容充實
    
    parts = []
    current_part = []
    current_chars = 0
    
    for i, paragraph in enumerate(paragraphs):
        paragraph_len = paragraph_lengths[i]
        
        # 如果單個段落太長，嘗試按句子分割（但保留完整內容）
        if paragraph_len > max_chars_per_page:
            # 更智能的句子分割，保留語意完整性
            sentences = []
            temp_sentence = ""
            
            # 先按主要標點符號分割
            for char in paragraph:
                temp_sentence += char
                # 主要句子結束標點
                if char in ['。', '！', '？']:
                    if temp_sentence.strip():
                        sentences.append(temp_sentence.strip())
                    temp_sentence = ""
                # 次要分割點（只在句子太長時使用）
                elif char in ['；', '，'] and len(temp_sentence) > max_chars_per_page * 0.8:
                    if temp_sentence.strip():
                        sentences.append(temp_sentence.strip())
                    temp_sentence = ""
            
            # 加入剩餘內容
            if temp_sentence.strip():
                sentences.append(temp_sentence.strip())
            
            for sentence in sentences:
                sentence_len = len(sentence)
                
                # 如果加入呢句會超過最大字數，完成當前部分
                if current_part and (current_chars + sentence_len > max_chars_per_page):
                    parts.append('\n\n'.join(current_part))
                    current_part = [sentence]
                    current_chars = sentence_len
                else:
                    current_part.append(sentence)
                    current_chars += sentence_len
                
                # 如果達到最佳長度就分頁
                if current_chars >= optimal_chars_per_page:
                    parts.append('\n\n'.join(current_part))
                    current_part = []
                    current_chars = 0
        else:
            # 正常處理短段落
            # 如果加入呢個段落會超過最大字數，而且當前部分已經有內容
            if current_part and (current_chars + paragraph_len > max_chars_per_page):
                # 完成當前部分
                parts.append('\n\n'.join(current_part))
                current_part = [paragraph]
                current_chars = paragraph_len
            else:
                # 加入當前段落
                current_part.append(paragraph)
                current_chars += paragraph_len
            
            # 更積極嘅分頁：如果當前部分達到最佳長度就分頁
            if (current_chars >= optimal_chars_per_page and 
                i < len(paragraphs) - 1):
                parts.append('\n\n'.join(current_part))
                current_part = []
                current_chars = 0
    
    # 處理剩餘內容
    if current_part:
        remaining_content = '\n\n'.join(current_part)
        
        # 總是保留剩餘內容，唔好合併（確保內容完整）
        parts.append(remaining_content)
    
    # 確保有足夠嘅部分，但唔好加空字符串（會產生空白頁）
    while len(parts) < target_parts:
        if parts:
            # 如果最後一部分太短，唔加新部分
            if len(parts[-1]) < min_chars_per_page * 2:
                break
        parts.append("")
    
    # 移除空白部分
    parts = [part for part in parts if part.strip()]
    
    # 控制總圖片數量為9張（包括標題、結論、結尾圖片）
    target_max_parts = 6  # 目標最多6個內容頁（加上標題、結論、結尾頁，總共9張圖片）
    
    # 如果分割後部分太多，智能合併
    while len(parts) > target_max_parts:
        print(f"📄 內容分割成 {len(parts)} 頁，正在優化到 {target_max_parts} 頁以內...")
        
        # 搵最短嘅兩個相鄰部分合併
        min_combined_length = float('inf')
        merge_index = -1
        
        for i in range(len(parts) - 1):
            combined_length = len(parts[i]) + len(parts[i + 1])
            if combined_length < min_combined_length and combined_length <= max_chars_per_page * 1.5:
                min_combined_length = combined_length
                merge_index = i
        
        # 如果搵到合適嘅合併位置
        if merge_index != -1:
            # 合併兩個部分
            parts[merge_index] = parts[merge_index] + '\n\n' + parts[merge_index + 1]
            parts.pop(merge_index + 1)
        else:
            # 如果搵唔到合適嘅合併，強制合併最短嘅兩個相鄰部分
            shortest_pair_index = 0
            shortest_pair_length = len(parts[0]) + len(parts[1])
            
            for i in range(1, len(parts) - 1):
                pair_length = len(parts[i]) + len(parts[i + 1])
                if pair_length < shortest_pair_length:
                    shortest_pair_length = pair_length
                    shortest_pair_index = i
            
            parts[shortest_pair_index] = parts[shortest_pair_index] + '\n\n' + parts[shortest_pair_index + 1]
            parts.pop(shortest_pair_index + 1)
    
    print(f"✅ 最終分割成 {len(parts)} 個內容頁")
    
    return parts[:target_max_parts]

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

def verify_story_perspective(filename="my_custom_story.txt"):
    """
    驗證並詳細顯示故事視角檢測結果
    """
    print(f"\n=== 🔍 視角檢測驗證工具 ===")
    print(f"📁 檔案: {filename}\n")
    
    story = read_custom_story(filename)
    
    if 'error' in story:
        print(f"❌ 錯誤: {story['error']}")
        print(f"💡 建議: {story['suggestion']}")
        return
    
    print(f"📰 標題: {story['title']}")
    print(f"📄 內容長度: {len(story['content'])} 字符\n")
    
    # 顯示視角檢測詳情
    if 'perspective_detection' in story:
        detection = story['perspective_detection']
        print(f"🎭 視角檢測詳情:")
        print(f"   1️⃣ 檔案名稱檢測: {detection['filename']} ({'👨 男性' if detection['filename'] == 'male' else '👩 女性'})")
        print(f"   2️⃣ 內容分析檢測: {detection['content']} ({'👨 男性' if detection['content'] == 'male' else '👩 女性'})")
        print(f"   3️⃣ 最終決定: {detection['final']} ({'👨‍💼 男性視角' if detection['final'] == 'male' else '👩‍💼 女性視角'})\n")
    
    # 顯示關鍵證據
    print(f"🔍 關鍵詞分析:")
    boyfriend_count = story['content'].count('男朋友') + story['title'].count('男朋友')
    girlfriend_count = story['content'].count('女朋友') + story['title'].count('女朋友')
    husband_count = story['content'].count('老公') + story['title'].count('老公')
    wife_count = story['content'].count('老婆') + story['title'].count('老婆')
    
    if boyfriend_count > 0:
        print(f"   ✅ '男朋友' 出現 {boyfriend_count} 次 → 女性視角證據")
    if girlfriend_count > 0:
        print(f"   ✅ '女朋友' 出現 {girlfriend_count} 次 → 男性視角證據")
    if husband_count > 0:
        print(f"   ✅ '老公' 出現 {husband_count} 次 → 女性視角證據")
    if wife_count > 0:
        print(f"   ✅ '老婆' 出現 {wife_count} 次 → 男性視角證據")
    
    total_female_evidence = boyfriend_count + husband_count
    total_male_evidence = girlfriend_count + wife_count
    
    print(f"\n📊 證據統計:")
    print(f"   👩 女性視角證據: {total_female_evidence} 個關鍵詞")
    print(f"   👨 男性視角證據: {total_male_evidence} 個關鍵詞")
    
    final_perspective = story.get('perspective', 'unknown')
    if final_perspective == 'female':
        print(f"\n✅ 結論: 這是一個 👩‍💼 女性視角 (Girl View) 的故事")
    elif final_perspective == 'male':
        print(f"\n✅ 結論: 這是一個 👨‍💼 男性視角 (Boy View) 的故事")
    else:
        print(f"\n⚠️ 結論: 無法確定視角")

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
        
        # 運行視角驗證
        print("\n" + "="*50)
        verify_story_perspective() 