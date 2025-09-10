#!/usr/bin/env python3
"""
Instagram 優化系統 - 最強 IG Post 策略
包含：發布時間、標籤策略、互動優化、分析工具
"""

import datetime
import json
import random
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class PostOptimization:
    """IG Post 優化設定"""
    best_posting_times: List[str]
    hashtag_strategy: Dict[str, List[str]]
    engagement_tactics: List[str]
    content_hooks: List[str]
    call_to_actions: List[str]

class InstagramOptimizer:
    """Instagram 優化器"""
    
    def __init__(self):
        self.hk_best_times = [
            "19:00-21:00",  # 黃金時間：放工後
            "12:00-14:00",  # 午餐時間
            "22:00-23:00",  # 夜晚睡前
            "09:00-10:00",  # 早上返工途中
            "15:00-16:00",  # 下午休息
        ]
        
        self.weekend_times = [
            "10:00-12:00",  # 週末早上
            "14:00-16:00",  # 週末下午
            "20:00-22:00",  # 週末晚上
        ]
        
        self.hashtag_pools = {
            "熱門大眾": [
                "#香港愛情", "#感情問題", "#拍拖煩惱", "#戀愛日常", 
                "#香港情侶", "#愛情故事", "#分手", "#復合", "#戀愛"
            ],
            "細分目標": [
                "#香港女仔", "#香港男仔", "#情感分享", "#愛情煩惱",
                "#戀愛心得", "#情侶問題", "#感情困擾", "#愛情討論",
                "#戀愛經驗", "#情感療癒", "#愛情成長", "#關係經營"
            ],
            "長尾精準": [
                "#香港dcard", "#感情諮詢", "#愛情解答", "#戀愛故事分享",
                "#情感心理學", "#愛情教練", "#戀愛導師", "#情感支援",
                "#愛情智慧", "#戀愛指南", "#情感成長", "#愛情修復"
            ]
        }
        
        self.engagement_hooks = [
            "你哋會唔會都有呢個經歷？",
            "有冇人試過類似情況？",
            "真係好想知大家點睇...",
            "我係咪諗得太多？",
            "點解會咁嘅？",
            "大家幫下我啦...",
            "我真係好困惑...",
            "唔知點算好..."
        ]
        
        self.call_to_actions = [
            "💬 Comment 區分享你哋嘅經歷啦",
            "🔄 Share 去 story 幫手討論",
            "🏷️ Tag 個朋友一齊傾下",
            "❤️ Like 如果你都有同感",
            "💭 留言講下你哋嘅睇法",
            "🤝 互相支持，一齊成長",
            "📩 DM 我如果想私下傾",
            "🌟 Follow 我睇更多愛情故事"
        ]
        
        self.content_structures = {
            "hook_question": "你哋覺得{topic}係咪好難處理？",
            "story_opener": "我同{person}嘅故事係咁樣開始嘅...",
            "emotional_trigger": "我真係好{emotion}，唔知點算好...",
            "community_question": "有冇人試過{situation}？",
            "advice_seeking": "大家會點樣處理{problem}？"
        }

    def get_optimal_posting_time(self) -> str:
        """獲取最佳發布時間"""
        now = datetime.datetime.now()
        day_of_week = now.weekday()
        
        # 週末用不同時間
        if day_of_week >= 5:  # 週六日
            return random.choice(self.weekend_times)
        else:  # 平日
            return random.choice(self.hk_best_times)
    
    def generate_hashtag_strategy(self, content_theme: str) -> Dict[str, List[str]]:
        """生成標籤策略"""
        strategy = {}
        
        # 熱門標籤 (5-7個)
        strategy["熱門"] = random.sample(self.hashtag_pools["熱門大眾"], 6)
        
        # 細分標籤 (8-10個)
        strategy["細分"] = random.sample(self.hashtag_pools["細分目標"], 9)
        
        # 長尾標籤 (5-8個)
        strategy["長尾"] = random.sample(self.hashtag_pools["長尾精準"], 6)
        
        # 主題相關標籤
        theme_tags = self._get_theme_specific_tags(content_theme)
        strategy["主題"] = theme_tags
        
        return strategy
    
    def _get_theme_specific_tags(self, theme: str) -> List[str]:
        """根據主題生成特定標籤"""
        theme_mapping = {
            "出軌": ["#出軌", "#背叛", "#第三者", "#信任危機"],
            "分手": ["#分手", "#失戀", "#心碎", "#重新開始"],
            "遠距離": ["#遠距離戀愛", "#Long Distance", "#異地戀", "#思念"],
            "家庭壓力": ["#家庭壓力", "#父母反對", "#門第之見", "#家人"],
            "溝通問題": ["#溝通", "#誤會", "#冷戰", "#理解"],
            "同居": ["#同居", "#生活習慣", "#磨合", "#未來規劃"],
            "結婚": ["#結婚", "#婚姻", "#承諾", "#人生規劃"]
        }
        
        for key, tags in theme_mapping.items():
            if key in theme:
                return random.sample(tags, min(len(tags), 3))
        
        return ["#感情", "#愛情", "#戀愛"]
    
    def generate_engagement_content(self, story_content: str) -> Dict[str, str]:
        """生成高互動內容"""
        return {
            "hook": random.choice(self.engagement_hooks),
            "call_to_action": random.choice(self.call_to_actions),
            "emotional_trigger": self._extract_emotional_trigger(story_content),
            "community_question": self._generate_community_question(story_content)
        }
    
    def _extract_emotional_trigger(self, content: str) -> str:
        """提取情感觸發詞"""
        triggers = ["好困惑", "好無奈", "好心痛", "好擔心", "好失望", "好迷茫"]
        return random.choice(triggers)
    
    def _generate_community_question(self, content: str) -> str:
        """生成社群問題"""
        questions = [
            "你哋遇到呢種情況會點做？",
            "有冇人有類似經歷可以分享？",
            "大家覺得我應該點處理？",
            "呢種情況係咪好常見？",
            "你哋會點樣同伴侶處理？"
        ]
        return random.choice(questions)
    
    def analyze_content_performance(self, content: str) -> Dict[str, object]:
        """分析內容表現潛力"""
        score = 0
        feedback = []
        
        # 檢查情感詞彙
        emotional_words = ["好", "真係", "點解", "唔知", "心痛", "無奈", "困惑"]
        emotion_count = sum(1 for word in emotional_words if word in content)
        score += emotion_count * 10
        
        if emotion_count >= 3:
            feedback.append("✅ 情感詞彙豐富")
        else:
            feedback.append("⚠️ 建議增加更多情感詞彙")
        
        # 檢查問句
        question_count = content.count("？") + content.count("?")
        score += question_count * 15
        
        if question_count >= 2:
            feedback.append("✅ 互動問句充足")
        else:
            feedback.append("⚠️ 建議增加更多問句")
        
        # 檢查長度
        if 100 <= len(content) <= 200:
            score += 20
            feedback.append("✅ 內容長度適中")
        else:
            feedback.append("⚠️ 內容長度需要調整")
        
        return {
            "score": score,
            "rating": "優秀" if score >= 80 else "良好" if score >= 60 else "需要改善",
            "feedback": feedback
        }
    
    def get_posting_schedule(self, days: int = 7) -> List[Dict]:
        """獲取發布時間表"""
        schedule = []
        base_date = datetime.datetime.now()
        
        for i in range(days):
            post_date = base_date + datetime.timedelta(days=i)
            optimal_time = self.get_optimal_posting_time()
            
            schedule.append({
                "date": post_date.strftime("%Y-%m-%d"),
                "day": post_date.strftime("%A"),
                "time": optimal_time,
                "reason": self._get_time_reason(optimal_time, post_date.weekday())
            })
        
        return schedule
    
    def _get_time_reason(self, time: str, weekday: int) -> str:
        """解釋時間選擇原因"""
        reasons = {
            "19:00-21:00": "黃金時間 - 大部分人放工後使用手機",
            "12:00-14:00": "午餐時間 - 用餐時刷社交媒體",
            "22:00-23:00": "睡前時間 - 放鬆刷手機",
            "09:00-10:00": "上班途中 - 通勤時間",
            "15:00-16:00": "下午休息 - 工作間隙",
            "10:00-12:00": "週末早上 - 悠閒時光",
            "14:00-16:00": "週末下午 - 休閒時間",
            "20:00-22:00": "週末晚上 - 娛樂時間"
        }
        return reasons.get(time, "一般時間")

def create_optimized_caption(story_content: str, optimizer: InstagramOptimizer) -> str:
    """創建優化後的 Instagram 標題"""
    
    # 生成互動內容
    engagement = optimizer.generate_engagement_content(story_content)
    
    # 生成標籤策略
    hashtag_strategy = optimizer.generate_hashtag_strategy(story_content)
    
    # 組合所有標籤
    all_hashtags = []
    for category, tags in hashtag_strategy.items():
        all_hashtags.extend(tags)
    
    # 建構標題
    caption_parts = [
        f"💭 {engagement['hook']}",
        "",
        f"📖 {story_content}",
        "",
        f"🤔 {engagement['community_question']}",
        "",
        f"💬 {engagement['call_to_action']}",
        "",
        " ".join(all_hashtags)
    ]
    
    return "\n".join(caption_parts)

# 使用示例
if __name__ == "__main__":
    optimizer = InstagramOptimizer()
    
    # 測試內容
    test_content = "我同男朋友一齊咗12年，但佢為咗21歲嘅妹妹仔同我講分手。我真係好無奈，唔知點算好。"
    
    # 生成優化建議
    optimal_time = optimizer.get_optimal_posting_time()
    hashtag_strategy = optimizer.generate_hashtag_strategy(test_content)
    engagement = optimizer.generate_engagement_content(test_content)
    performance = optimizer.analyze_content_performance(test_content)
    schedule = optimizer.get_posting_schedule(7)
    
    print("=== Instagram 優化報告 ===")
    print(f"最佳發布時間: {optimal_time}")
    print(f"內容評分: {performance['score']}/100 ({performance['rating']})")
    feedback_str = ', '.join(performance['feedback'])
    print(f"建議: {feedback_str}")
    all_tags = []
    for tags in hashtag_strategy.values():
        all_tags.extend(tags)
    print(f"標籤策略: {len(all_tags)} 個標籤")
    print(f"互動策略: {engagement['call_to_action']}") 