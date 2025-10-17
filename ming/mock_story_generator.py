#!/usr/bin/env python3
"""
Mock Story Generator - 當 OpenAI API 不可用時的示範模式
Works without OpenAI API for unsupported regions
"""

import json
import random
from typing import Dict

class MockStoryGenerator:
    """模擬故事生成器 - 適用於 OpenAI API 不可用的地區"""
    
    def __init__(self):
        # 預設的示範回應模板
        self.demo_responses = [
            {
                "標題": "發現男朋友派帽俾我",
                "內容": "原來發現一個人呃你，個心係會『咯』一聲，然後靜晒。我同佢，23歲同24歲，喺人哋眼中襯到絕。我仲 on99 咁 plan 緊下個月去邊度 staycation，佢就靜雞雞同第二個女仔 plan 緊點樣唔俾我發現。我噚日問佢，佢冇出聲，淨係望住地下，個樣好似一個做錯事嘅細路。而家 final year 都讀唔落，成日諗住呢件事，連 assignment 都做唔完。朋友話我傻，但我真係唔知點算好。",
                "結論": "大家覺得我應該點做？"
            },
            {
                "標題": "男朋友成日打機唔理我",
                "內容": "佢每日返到屋企第一件事就係開機打 game，連食飯都要我叫三次先肯落嚟。我試過同佢講，佢話呢個係佢嘅 hobby，叫我唔好管咁多。Weekend 我想一齊出街，佢話要打 rank，話好重要。我坐喺佢隔離睇佢打咗成個鐘，佢連望都唔望我一眼。我開始覺得自己好似透明人咁，喺佢心目中連個 game 都不如。",
                "結論": "我係咪要求太多？"
            },
            {
                "標題": "女朋友網購成癮我好擔心",
                "內容": "佢每日都要買嘢，收貨收到郵差都識我哋屋企地址。我話佢唔好咁樣，佢話網購係佢嘅減壓方法。但每個月信用卡賬單都好誇張，我地 budget 根本 handle 唔到。屋企堆滿咗包裹，好多嘢買咗都冇用過，tag 都未剪。我試過收埋佢部電話，佢發晒脾氣話我控制狂。而家我唔知點 balance 我哋嘅關係同經濟壓力。",
                "結論": "點樣先可以幫到佢？"
            }
        ]
    
    def generate_story_from_concept_sync(self, story_concept: str) -> Dict:
        """
        同步版本的故事生成 - 使用預設模板
        
        Args:
            story_concept: 故事概念
            
        Returns:
            模擬的故事內容
        """
        
        # 根據故事概念選擇最合適的示範回應
        selected_response = self._select_best_response(story_concept)
        
        # 添加元數據
        result = {
            **selected_response,
            "原始概念": story_concept,
            "生成方法": "Mock 模式 (同步)",
            "說明": "這是示範內容，因為 OpenAI API 在您的地區不可用"
        }
        
        return result
    
    async def generate_story_from_concept(self, story_concept: str) -> Dict:
        """
        模擬故事生成 - 使用預設模板
        
        Args:
            story_concept: 故事概念
            
        Returns:
            模擬的故事內容
        """
        
        # 根據故事概念選擇最合適的示範回應
        selected_response = self._select_best_response(story_concept)
        
        # 添加元數據
        result = {
            **selected_response,
            "原始概念": story_concept,
            "生成方法": "Mock/Demo Mode (OpenAI API 不可用)",
            "說明": "這是示範模式的回應，因為 OpenAI API 在您的地區不可用",
            "建議": "如需使用真實 AI 生成，請嘗試使用 VPN 或其他 AI 服務"
        }
        
        return result
    
    def _select_best_response(self, story_concept: str) -> Dict:
        """根據故事概念選擇最合適的示範回應"""
        
        concept_lower = story_concept.lower()
        
        # 關鍵詞匹配邏輯
        if any(keyword in concept_lower for keyword in ["派帽", "呃", "綠帽", "背叛", "出軌"]):
            return self.demo_responses[0]  # 派帽故事
        elif any(keyword in concept_lower for keyword in ["打機", "遊戲", "game", "電腦", "忽略"]):
            return self.demo_responses[1]  # 打機故事
        elif any(keyword in concept_lower for keyword in ["網購", "買嘢", "購物", "消費", "錢"]):
            return self.demo_responses[2]  # 網購故事
        else:
            # 隨機選擇一個
            return random.choice(self.demo_responses)

# 主要函數
def generate_mock_story_sync(story_concept: str) -> Dict:
    """
    同步版本的模擬故事生成 - 主函數
    
    Args:
        story_concept: 故事概念
        
    Returns:
        模擬的故事內容
    """
    generator = MockStoryGenerator()
    result = generator.generate_story_from_concept_sync(story_concept)
    return result

async def generate_mock_story(story_concept: str) -> Dict:
    """
    模擬故事生成 - 主函數
    
    Args:
        story_concept: 故事概念
        
    Returns:
        模擬的故事內容
    """
    generator = MockStoryGenerator()
    result = await generator.generate_story_from_concept(story_concept)
    return result

# 測試函數
async def test_mock_generator():
    """測試模擬生成器"""
    
    test_concepts = [
        "我發現我24歲嘅男朋友派帽俾我，影響到我 final year 嘅學業。",
        "我男朋友成日打機，連約會都唔肯放低手機。",
        "我女朋友網購成癮，每個月信用卡賬單都好誇張。"
    ]
    
    print("=== 🎭 Mock Story Generator 測試 ===")
    print("適用於 OpenAI API 不可用的地區\n")
    
    for i, concept in enumerate(test_concepts, 1):
        print(f"📖 測試 {i}: {concept}")
        
        result = await generate_mock_story(concept)
        
        print("✅ 模擬生成完成！")
        print(f"📰 標題：{result['標題']}")
        print(f"📄 內容：{result['內容'][:100]}...")
        print(f"❓ 結論：{result['結論']}")
        print(f"🔧 方法：{result['生成方法']}")
        print("-" * 60)
    
    print("🎉 測試完成！")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_mock_generator()) 