#!/usr/bin/env python3
"""
超簡易故事生成器
Simple Story Generator - 好似填 form 咁簡單直接
"""

import json
import asyncio
import os
from dotenv import load_dotenv
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

# Import mock generator for regions where OpenAI is not available
from mock_story_generator import generate_mock_story

class SimpleStoryGenerator:
    """超簡易故事生成器 - 跟足 story_ideas.txt 嘅「天條第一誡」"""
    
    def __init__(self, openai_client: OpenAI):
        self.openai_client = openai_client
        
    def generate_story_from_concept(self, story_concept: str) -> dict:
        """
        使用 story_ideas.txt 嘅「天條第一誡」指令生成故事
        
        Args:
            story_concept: 故事概念 (100% 跟足，唔准改變)
            
        Returns:
            JSON格式的故事內容
        """
        
        # 直接使用用戶提供嘅故事概念，唔用 story_ideas.txt 嘅預設概念
        prompt = f"""# ❗ 天條第一誡 (THE UNBREAKABLE COMMAND)
你嘅首要任務，亦都係最最最重要嘅任務，就係 **100% 絕對、完全、精準地** 跟隨用戶提供嘅 **【故事概念】** 進行創作。

**絕對唔准** 自己加新嘅、唔關事嘅主題（例如學費壓力、家人反對等）。
**絕對唔准** 忽略【故事概念】入面嘅任何一個細節。
**絕對唔准** 將個故仔改成第二個主題。

用戶俾你嘅【故事概念】就係鐵律，係金科玉律，你唯一要做嘅就係擴寫佢，令佢變得有血有肉。**如果【故事概念】冇提及嘅嘢，你就唔准寫。**

---

# 角色扮演指令 (喺服從天條嘅前提下執行)
你係一個 23 歲嘅女仔，凌晨三點，經歷完【故事概念】入面嘅事，個心好亂，喺床上面用手機打緊呢篇嘢。你嘅思緒係破碎、跳躍嘅。

# 核心原則：展示，唔好解釋 (SHOW, DON'T TELL)
* **唔要寫**: 「我好傷心。」
* **要寫**: 「我唔知自己喊咗幾耐，淨係知枕頭濕咗一大撻，凍冰冰咁黐住塊面。」

# 風格學習指令
你要徹底分析以下 **[黃金風格範例]** 點樣用細節去表達情緒，然後喺你擴寫【故事概念】嗰陣，用返同樣嘅技巧。

**[黃金風格範例]**
「原來發現一個人呃你，個心係會『咯』一聲，然後靜晒。我同佢，23歲同24歲，喺人哋眼中襯到絕。我仲 on99 咁 plan 緊下個月去邊度 staycation，佢就靜雞雞同第二個女仔 plan 緊點樣唔俾我發現。我噚日問佢，佢冇出聲，淨係望住地下，個樣好似一個做錯事嘅細路。我冇打佢，亦都冇鬧，我淨係覺得好好笑。我哋三年嘅感情，原來就係一場咁好笑嘅笑話。」

---

# 核心任務指令
**根據【天條第一誡】**，請將以下【故事概念】擴寫成一個有血有肉嘅故仔，同時要嚴格遵守所有風格規則。

**【故事概念】：{story_concept}**

# 文筆風格規則 (必須跟足！)：
* ✅ **瘋狂加入生活細節同英文**：cosplay event、comic con、角色扮演、IG post、costume quality、character accuracy…
* ✅ **破碎化思考**：句子可以短啲，諗法可以跳躍。
* ✅ **對白同內心戲要真實**：用返香港人平時講嘢嘅語氣。
* ✅ **針對 cosplay 主題**：講 cosplay 文化、costume 質素、角色形象、香港 cosplay 圈子嘅問題。

# 禁止事項 (最後提醒！)：
* ❌ **再次強調：絕對禁止偏離【故事概念】！**
* ❌ **禁止寫感情故事、愛情關係等無關主題**
* ❌ **禁止任何總結性、解釋性嘅句子** (e.g., 我好無奈)。
* ❌ **禁止任何唔自然嘅文藝腔** (e.g., 低迴)。
* ❌ **必須圍繞 cosplay 主題，唔可以轉去其他話題**

# 輸出格式
將所有你創作嘅內容，放入一個乾淨嘅 JSON 物件，格式如下：

{{
  "標題": "[6-12字標題，關於 cosplay 問題]",
  "內容": "[完整故事，講香港 cosplay 文化問題，跟足黃金風格範例，150-200字]",
  "結論": "[簡短問句，問大家對 cosplay 嘅意見，6-10字]"
}}

唔要任何額外嘢。100% 跟足【故事概念】，必須講 cosplay！"""

        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system", 
                        "content": "你係一個絕對服從嘅 AI。你必須 100% 跟足用戶嘅【故事概念】，唔准加任何新內容，唔准改變主題。完全按照指令執行，唔好自作聰明。"
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                temperature=0.7
            )
            
            # 解析回應
            response_content = response.choices[0].message.content.strip()
            
            # 嘗試提取 JSON
            try:
                # 如果回應包含 JSON 代碼塊
                if "```json" in response_content:
                    json_start = response_content.find("```json") + 7
                    json_end = response_content.find("```", json_start)
                    json_str = response_content[json_start:json_end].strip()
                elif "{" in response_content and "}" in response_content:
                    # 直接提取 JSON 部分
                    json_start = response_content.find("{")
                    json_end = response_content.rfind("}") + 1
                    json_str = response_content[json_start:json_end]
                else:
                    # 如果冇 JSON，手動解析
                    raise ValueError("No JSON found")
                
                result = json.loads(json_str)
                
                # 確保必要欄位存在
                if "標題" not in result or "內容" not in result or "結論" not in result:
                    raise ValueError("Missing required fields")
                
                # 添加額外資訊
                result["原始概念"] = story_concept
                result["生成方法"] = "story_ideas.txt 天條第一誡"
                
                return result
                
            except (json.JSONDecodeError, ValueError) as e:
                # JSON 解析失敗，手動建構結果
                print(f"⚠️ JSON 解析失敗，使用原始回應: {str(e)}")
                
                return {
                    "標題": "AI 生成錯誤",
                    "內容": response_content,
                    "結論": "點解會咁？",
                    "原始概念": story_concept,
                    "生成方法": "story_ideas.txt 天條第一誡",
                    "錯誤": "JSON 解析失敗"
                }
                
        except Exception as e:
            error_message = str(e)
            
            # Check if it's a region/country restriction error
            if "unsupported_country_region_territory" in error_message or "403" in error_message:
                print("⚠️ OpenAI API 在您的地區不可用，切換到 Mock 模式")
                import asyncio
                return asyncio.run(generate_mock_story(story_concept))
            
            return {
                "標題": "生成失敗",
                "內容": f"錯誤：{error_message}",
                "結論": "點算好？",
                "原始概念": story_concept,
                "生成方法": "story_ideas.txt 天條第一誡",
                "錯誤": error_message
            }

# 主要函數
def generate_simple_story(story_concept: str) -> dict:
    """
    故事生成 - 使用 story_ideas.txt 嘅「天條第一誡」
    
    Args:
        story_concept: 故事概念 (100% 跟足)
        
    Returns:
        JSON格式的故事
    """
    # 載入環境
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if not openai_api_key:
        print("⚠️ 找不到 OPENAI_API_KEY，使用 Mock 模式")
        import asyncio
        return asyncio.run(generate_mock_story(story_concept))
    
    # 檢查 OpenAI 是否可用
    if OpenAI is None:
        print("⚠️ OpenAI 套件未安裝，使用 Mock 模式")
        import asyncio
        return asyncio.run(generate_mock_story(story_concept))
    
    try:
        # 初始化 OpenAI
        openai_client = OpenAI(api_key=openai_api_key)
        
        # 創建生成器
        generator = SimpleStoryGenerator(openai_client)
        
        # 生成故事
        result = generator.generate_story_from_concept(story_concept)
        
        return result
        
    except Exception as e:
        error_message = str(e)
        
        # Check for region restrictions
        if "unsupported_country_region_territory" in error_message or "403" in error_message:
            print("⚠️ OpenAI API 在您的地區不可用，使用 Mock 模式")
            import asyncio
            return asyncio.run(generate_mock_story(story_concept))
        
        # Other errors, still try mock mode as fallback
        print(f"⚠️ OpenAI 錯誤：{error_message}，使用 Mock 模式")
        import asyncio
        return asyncio.run(generate_mock_story(story_concept))

# 測試和演示
async def test_simple_generator():
    """測試簡易生成器"""
    
    test_stories = [
        "我發現我24歲嘅男朋友派帽俾我，影響到我 final year 嘅學業。",
        "我沉迷社交媒體，日日都要影相打卡，但我男朋友覺得我哋個relationship變咗好假。",
        "我最近網購成癮，每個月信用卡賬單都好誇張，我男朋友開始擔心。"
    ]
    
    print("=== 🎯 story_ideas.txt 天條第一誡測試 ===")
    
    for i, story in enumerate(test_stories, 1):
        print(f"\n📖 測試 {i}: {story}")
        print("⏳ 使用天條第一誡生成...")
        
        result = await generate_simple_story(story)
        
        print("✅ 完成！")
        print("=" * 50)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        print("=" * 50)

if __name__ == "__main__":
    # 測試模式
    asyncio.run(test_simple_generator()) 