import json
import random
import time
import re

# Story scenario variations to ensure different content each time
STORY_SCENARIOS = [
    {
        "theme": "網購成癮", 
        "story_template": """我最近網購成癮，每日都要買嘢，收貨收到郵差都識我。我話網購係我嘅減壓方法，但每個月信用卡賬單都好誇張。我男朋友試過同我傾，但我話佢唔明我嘅需要。而家屋企堆滿咗包裹，好多嘢買咗都冇用過...""",
        "title_examples": ["我網購成癮點算？", "我每日都要買嘢先開心？", "信用卡爆晒都要繼續購物？"]
    },
    {
        "theme": "社交媒體沉迷",
        "story_template": """我沉迷社交媒體，日日都要影相打卡，食飯都要影到靚先食得。我話要維持網上形象，但我男朋友覺得我哋個relationship變咗好假。連拍拖都要配合我影相，佢開始覺得好累...""",
        "title_examples": ["我影相比拍拖重要？", "為咗打卡連食飯都變咗工作？", "網上形象比真實關係重要？"]
    },
    {
        "theme": "遊戲成癮",
        "story_template": """我最近迷上咗手機遊戲，日日玩到深夜，連weekends都唔肯出街。我話要打rank，但我男朋友覺得我已經忽略咗我哋嘅關係。佢試過join我一齊玩，但我話佢技術太差會拖累我...""",
        "title_examples": ["我遊戲成癮唔理男朋友？", "我寧願打機都唔想拍拖？", "為咗遊戲可以唔食唔瞓？"]
    },
    {
        "theme": "工作狂",
        "story_template": """我係工作狂，24小時都喺度返工，連假期都要回覆email。我話要為將來打拼，但我男朋友覺得我哋已經冇time相處。每次佢約我出嚟都話要開會，佢開始懷疑工作對我嚟講係咪比佢重要...""",
        "title_examples": ["我工作狂冇時間拍拖？", "我寧願OT都唔陪男朋友？", "24小時返工正常咩？"]
    },
    {
        "theme": "外貌焦慮",
        "story_template": """我有嚴重外貌焦慮，每日要化妝兩個鐘先肯出門，連去樓下買嘢都要full makeup。我覺得自己好醜，但我男朋友覺得我好靚。我話如果佢真係愛我就會明白我嘅insecurity...""",
        "title_examples": ["我覺得自己醜但男朋友覺得好靚？", "為咗化妝每日遲到？", "外貌焦慮影響我哋關係？"]
    },
    {
        "theme": "朋友圈問題",
        "story_template": """我嘅朋友成日講我男朋友壞話，話佢配唔上我，叫我分手。我開始相信佢哋，對佢態度都變咗。佢覺得我俾朋友影響太多，但我話朋友係為我好。我唔知應該點處理呢個情況...""",
        "title_examples": ["我朋友叫我同男朋友分手？", "我太受朋友影響？", "點樣處理toxic朋友圈？"]
    },
    {
        "theme": "金錢觀念",
        "story_template": """我同男朋友嘅金錢觀念好唔同，佢比較節儉，我就大洗。每次食飯我都要去expensive餐廳，話平嘅嘢食唔落。佢覺得應該慳錢為將來，但我話人生苦短要enjoy。我哋經常為錢爭執...""",
        "title_examples": ["我哋金錢觀念差好遠？", "佢覺得我太大洗？", "為錢爭執影響感情？"]
    },
    {
        "theme": "家庭壓力",
        "story_template": """我嘅屋企人唔like我男朋友，覺得佢background唔夠好。我夾喺中間好辛苦，但又唔敢反抗屋企人。佢開始覺得我哋relationship好有壓力，唔知應該繼續定放棄...""",
        "title_examples": ["我屋企人唔接受男朋友？", "家庭壓力影響我哋感情？", "應該為愛情對抗家人？"]
    }
]

def auto_generate_theme_from_story(story_content):
    """Auto-generate theme from story content using keyword matching"""
    story_lower = story_content.lower()
    
    # Theme keywords mapping
    theme_keywords = {
        "感情困擾": ["嬲", "扮狗", "女朋友", "男朋友", "感情", "關係"],
        "網購成癮": ["網購", "買嘢", "包裹", "信用卡", "購物"],
        "社交媒體沉迷": ["instagram", "ig", "影相", "打卡", "social media", "社交媒體"],
        "遊戲成癮": ["遊戲", "打機", "手機遊戲", "game", "gaming", "rank"],
        "工作狂": ["工作", "ot", "overtime", "返工", "公司", "email"],
        "外貌焦慮": ["化妝", "makeup", "外貌", "醜", "靚", "樣"],
        "金錢觀念": ["錢", "expensive", "慳錢", "大洗", "金錢"],
        "家庭壓力": ["屋企人", "家人", "父母", "家庭"],
        "宅女生活": ["宅", "唔出門", "屋企", "外賣"],
        "夜貓子": ["夜晚", "三點", "夜貓子", "瞓覺", "作息"]
    }
    
    # Find matching theme
    for theme, keywords in theme_keywords.items():
        if any(keyword in story_content for keyword in keywords):
            return theme
    
    # Default theme if no match found
    return "感情困擾"

def auto_generate_titles_from_story(story_content, theme):
    """Auto-generate title examples from story content"""
    # Common question patterns in Cantonese
    question_patterns = [
        f"點解佢咁{theme.replace('成癮', '').replace('狂熱', '')}？",
        f"佢{theme.replace('成癮', '').replace('狂熱', '')}影響我哋感情？",
        f"我應該點處理佢{theme.replace('成癮', '').replace('狂熱', '')}？"
    ]
    
    # Theme-specific titles
    theme_specific = {
        "健身狂熱": ["我愛gym多過愛男朋友？", "要男朋友陪我健身先肯拍拖？", "健身變咗第三者？"],
        "網購成癮": ["我每日都要買嘢先開心？", "信用卡爆晒都要繼續購物？", "屋企堆滿包裹點算？"],
        "遊戲成癮": ["我寧願打機都唔想拍拖？", "為咗遊戲可以唔食唔瞓？", "男朋友係咪輸俾咗手機？"],
        "社交媒體沉迷": ["我影相比拍拖重要？", "為咗打卡連食飯都變咗工作？", "網上形象比真實關係重要？"],
        "工作狂": ["我寧願OT都唔陪男朋友？", "24小時返工正常咩？", "工作比男朋友重要？"],
        "追星成癮": ["我愛idol多過愛男朋友？", "為追星可以花光積蓄？", "學idol做人正常咩？"],
        "外貌焦慮": ["我覺得自己醜但男朋友覺得好靚？", "為咗化妝每日遲到？", "外貌焦慮影響我哋關係？"],
        "金錢觀念": ["我哋金錢觀念差好遠？", "男朋友覺得我太大洗？", "為錢爭執影響感情？"],
        "家庭壓力": ["我屋企人唔接受男朋友？", "家庭壓力影響我哋感情？", "應該為愛情對抗家人？"],
        "完美主義": ["我要求完美令男朋友好累？", "咩都要criticize係愛情咩？", "完美主義影響感情？"]
    }
    
    if theme in theme_specific:
        return theme_specific[theme]
    else:
        return question_patterns

def load_story_ideas_from_file(filename="story_ideas.txt"):
    """Load story ideas from text file with flexible format support"""
    story_scenarios = []
    current_perspective = "female"  # Default to female perspective
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            # Skip empty lines
            if not line:
                continue
            
            # Check for perspective markers in comments
            if line.startswith('#'):
                if '男性第一人稱視角' in line or '男性視角' in line:
                    current_perspective = "male"
                elif '女性第一人稱視角' in line or '女性視角' in line:
                    current_perspective = "female"
                continue
            
            # Simple format: Just story content - auto-generate theme and titles
            story_content = line
            auto_theme = auto_generate_theme_from_story(story_content)
            auto_titles = auto_generate_titles_from_story(story_content, auto_theme)
            
            scenario = {
                "theme": auto_theme,
                "story_template": story_content,
                "title_examples": auto_titles,
                "auto_generated": True,  # Mark as auto-generated for reference
                "perspective": current_perspective  # Add perspective info
            }
            story_scenarios.append(scenario)
        
        return story_scenarios
        
    except FileNotFoundError:
        print(f"Warning: {filename} not found, using default scenarios")
        return get_default_scenarios()
    except Exception as e:
        print(f"Error loading story ideas: {str(e)}")
        return get_default_scenarios()

def get_default_scenarios():
    """Return default scenarios if file loading fails"""
    return [
        {
            "theme": "感情困擾",
            "story_template": "女朋友想我係屋企扮狗",
            "title_examples": ["女朋友想我扮狗？", "我應該點做？", "扮狗係愛情咩？"],
            "perspective": "male"
        }
    ]

def get_random_story_scenario():
    """Get a random story scenario from file"""
    scenarios = load_story_ideas_from_file()
    if not scenarios:
        scenarios = get_default_scenarios()
    
    selected = random.choice(scenarios)
    return selected

def add_randomization_to_prompt(base_prompt, scenario_theme):
    """Add randomization elements to prompts to ensure variety"""
    randomization_elements = [
        "加入一些意想不到嘅情節轉折",
        "用唔同嘅情感角度去講述", 
        "加入更多具體嘅細節同對話",
        "從男朋友嘅角度講述內心掙扎",
        "加入朋友或家人嘅反應",
        "包含更多日常生活嘅細節"
    ]
    
    selected_elements = random.sample(randomization_elements, 2)
    randomization = f"\n\n額外要求：{', '.join(selected_elements)}。"
    
    # Add timestamp-based variation
    current_time = int(time.time())
    variation_seed = current_time % 10
    
    if variation_seed < 3:
        randomization += "\n語調要更加情感豐富，表達更多內心矛盾。"
    elif variation_seed < 6:
        randomization += "\n加入更多具體嘅日常生活場景同細節。"
    else:
        randomization += "\n重點描述對話同人物互動，令故事更生動。"
    
    return base_prompt + randomization

async def generate_relationship_title_content(openai_client, story_content: str, scenario=None):
    """Generate title content for relationship posts"""
    if scenario is None:
        scenario = get_random_story_scenario()
    
    # Use example titles from scenario for inspiration
    title_examples = scenario.get('title_examples', ["我迷信到要整容？"])
    example_title = random.choice(title_examples)
    
    # Get perspective and set appropriate prompt content
    perspective = scenario.get('perspective', 'female')
    
    if perspective == 'male':
        perspective_text = "男性視角"
        perspective_examples = "如「我女朋友...」、「佢...」、「我應該點做」"
        system_content = "你是一個專門創作Dcard風格感情故事的社交媒體內容創作者。創建吸引人且情感豐富的內容，能夠捕捉感情戲劇和困境。必須用第一人稱角度（男性視角）和純正廣東話口語寫作，語調自然親切，就像香港人日常傾計咁樣。用詞要地道，包括「佢」、「嚟」、「咗」、「唔」、「點」、「乜」、「嗰」、「啲」、「俾」、「喺」、「嘅」等廣東話特有詞彙。內容要像Dcard貼文一樣真實、個人化、有情緒張力，包含具體對話和場景描述。每次創作都要有新意同變化。\n\n**重要語言要求：**\n- 避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然或翻譯式表達\n- 不要使用書面語或過於正式的詞彙\n- 使用自然的口語表達，如「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」\n- 避免使用「真係為咗錢咩真係咁啦一齊？」這種結構混亂的句子\n- 使用清晰的問句結構，如「真係為咗錢咩？真係咁樣一齊？」\n- 避免使用「曬爛」、「有形嘅」、「意外嚇」等不常見或生硬的表達\n- 使用更自然的替代詞：\n  * 「借咩」→「咩男朋友嚟㗎」或「邊個男朋友」\n  * 「靠山走水」→「翻山越嶺」或「就算要行好遠」\n  * 「有形嘅」→「有型嘅」或「靚仔嘅」\n  * 「意外嚇」→「嚇親」或「嚇到」\n  * 「曬爛」→「曬到爛」或「曬到變色」"
    else:
        perspective_text = "女性視角"
        perspective_examples = "如「我...」、「我應該點做」、「我好煩惱」"
        system_content = "你是一個專門創作Dcard風格感情故事的社交媒體內容創作者。創建吸引人且情感豐富的內容，能夠捕捉感情戲劇和困境。必須用第一人稱角度（女性視角）和純正廣東話口語寫作，語調自然親切，就像香港人日常傾計咁樣。用詞要地道，包括「佢」、「嚟」、「咗」、「唔」、「點」、「乜」、「嗰」、「啲」、「俾」、「喺」、「嘅」等廣東話特有詞彙。內容要像Dcard貼文一樣真實、個人化、有情緒張力，包含具體對話和場景描述。每次創作都要有新意同變化。\n\n**重要語言要求：**\n- 避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然或翻譯式表達\n- 不要使用書面語或過於正式的詞彙\n- 使用自然的口語表達，如「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」\n- 避免使用「真係為咗錢咩真係咁啦一齊？」這種結構混亂的句子\n- 使用清晰的問句結構，如「真係為咗錢咩？真係咁樣一齊？」\n- 避免使用「曬爛」、「有形嘅」、「意外嚇」等不常見或生硬的表達\n- 使用更自然的替代詞：\n  * 「借咩」→「咩男朋友嚟㗎」或「邊個男朋友」\n  * 「靠山走水」→「翻山越嶺」或「就算要行好遠」\n  * 「有形嘅」→「有型嘅」或「靚仔嘅」\n  * 「意外嚇」→「嚇親」或「嚇到」\n  * 「曬爛」→「曬到爛」或「曬到變色」"
    
    prompt = f"""根據以下感情故事，為社交媒體帖子創建一個吸引人的標題（Dcard風格）：

故事內容：
{story_content}

故事主題：{scenario['theme']}

要求：
1. 標題應該情感豐富且容易產生共鳴
2. 應該是8-15個中文字符
3. 應該捕捉主要困境或情感
4. 使用問句格式或情感陳述
5. 用第一人稱角度（{perspective_text}），{perspective_examples}
6. 必須用純正廣東話口語，例如：「點算好」、「好嬲」、「唔知做乜」
7. **Dcard風格**：個人化、真實、帶有情緒張力，像朋友訴說煩惱
8. 列出3-5個應該在設計中突出顯示的關鍵詞
9. **語言要求**：避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然表達，使用「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」等自然口語

參考例子（但要創新，唔好照抄）：{example_title}

輸出格式：
標題：[標題內容]
關鍵詞：[關鍵詞1], [關鍵詞2], [關鍵詞3]...
"""

    # Add randomization
    prompt = add_randomization_to_prompt(prompt, scenario['theme'])

    response = await openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": prompt}
        ]
    )

    # Parse the response
    lines = response.choices[0].message.content.strip().split('\n')
    title_content = {
        'title': '',
        'keywords': []
    }

    for line in lines:
        if line.startswith('標題：') or line.startswith('標題: '):
            title_content['title'] = line.replace('標題：', '').replace('標題: ', '').strip()
        elif line.startswith('關鍵詞：') or line.startswith('關鍵詞: '):
            keywords = line.replace('關鍵詞：', '').replace('關鍵詞: ', '').strip()
            title_content['keywords'] = [k.strip() for k in keywords.split(',')]

    return title_content

async def generate_relationship_story_content(openai_client, base_story: str, scenario=None):
    """Generate the main story content with key points"""
    if scenario is None:
        scenario = get_random_story_scenario()
    
    # Get perspective and set appropriate prompt content
    perspective = scenario.get('perspective', 'female')
    
    if perspective == 'male':
        perspective_text = "男性視角"
        perspective_examples = """如：
   - 「我同佢講...」
   - 「我當時覺得...」
   - 「我真係好無奈...」
   - 「我諗住...」"""
        system_content = "你是一個專門創作Dcard風格感情故事的社交媒體內容創作者。創建吸引人且情感豐富的內容，能夠捕捉感情戲劇和困境。必須用第一人稱角度（男性視角）和純正廣東話口語寫作，語調自然親切，就像香港人日常傾計咁樣。用詞要地道，包括「佢」、「嚟」、「咗」、「唔」、「點」、「乜」、「嗰」、「啲」、「俾」、「喺」、「嘅」等廣東話特有詞彙。內容要像Dcard貼文一樣真實、個人化、有情緒張力，包含具體對話和場景描述。每次創作都要有新意同變化。\n\n**重要語言要求：**\n- 避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然或翻譯式表達\n- 不要使用書面語或過於正式的詞彙\n- 使用自然的口語表達，如「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」\n- 避免使用「真係為咗錢咩真係咁啦一齊？」這種結構混亂的句子\n- 使用清晰的問句結構，如「真係為咗錢咩？真係咁樣一齊？」\n- 避免使用「曬爛」、「有形嘅」、「意外嚇」等不常見或生硬的表達\n- 使用更自然的替代詞：\n  * 「借咩」→「咩男朋友嚟㗎」或「邊個男朋友」\n  * 「靠山走水」→「翻山越嶺」或「就算要行好遠」\n  * 「有形嘅」→「有型嘅」或「靚仔嘅」\n  * 「意外嚇」→「嚇親」或「嚇到」\n  * 「曬爛」→「曬到爛」或「曬到變色」"
    else:
        perspective_text = "女性視角"
        perspective_examples = """如：
   - 「我同佢講...」
   - 「我當時覺得...」
   - 「我真係好無奈...」
   - 「我諗住...」"""
        system_content = "你是一個專門創作Dcard風格感情故事的社交媒體內容創作者。創建吸引人且情感豐富的內容，能夠捕捉感情戲劇和困境。必須用第一人稱角度（女性視角）和純正廣東話口語寫作，語調自然親切，就像香港人日常傾計咁樣。用詞要地道，包括「佢」、「嚟」、「咗」、「唔」、「點」、「乜」、「嗰」、「啲」、「俾」、「喺」、「嘅」等廣東話特有詞彙。內容要像Dcard貼文一樣真實、個人化、有情緒張力，包含具體對話和場景描述。每次創作都要有新意同變化。\n\n**重要語言要求：**\n- 避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然或翻譯式表達\n- 不要使用書面語或過於正式的詞彙\n- 使用自然的口語表達，如「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」\n- 避免使用「真係為咗錢咩真係咁啦一齊？」這種結構混亂的句子\n- 使用清晰的問句結構，如「真係為咗錢咩？真係咁樣一齊？」\n- 避免使用「曬爛」、「有形嘅」、「意外嚇」等不常見或生硬的表達\n- 使用更自然的替代詞：\n  * 「借咩」→「咩男朋友嚟㗎」或「邊個男朋友」\n  * 「靠山走水」→「翻山越嶺」或「就算要行好遠」\n  * 「有形嘅」→「有型嘅」或「靚仔嘅」\n  * 「意外嚇」→「嚇親」或「嚇到」\n  * 「曬爛」→「曬到爛」或「曬到變色」"
    
    prompt = f"""根據這個感情故事，提取關鍵戲劇性要點並創建結構化內容（Dcard風格）：

原始故事：
{base_story}

要求：
1. 創建一個吸引人的鉤子（5-8個字）
2. 識別3個顯示升級的主要故事要點
3. 每個要點應該有標題（4-6個字）和詳細描述（300-400個字）
4. **Dcard風格**：個人化敘述、真實感受、具體細節、情緒豐富
5. 必須用第一人稱角度講述（{perspective_text}），{perspective_examples}
6. 必須用純正廣東話口語寫作，包括：
   - 廣東話詞彙：佢、嚟、咗、唔、點、乜、嗰、啲、俾、喺、嘅等
   - 廣東話語法和句式
   - 日常對話用詞，如「真係」、「好嬲」、「無奈」、「點算好」
7. **像Dcard貼文一樣**：包含對話、內心獨白、具體場景描述
8. 選擇5-7個情感關鍵詞用於突出顯示
9. **語言要求**：避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然表達，使用「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」等自然口語

輸出格式：
鉤子：[鉤子問題或陳述]

故事要點：

1. 標題：[要點1標題]
   描述：[詳細描述300-400字，第一人稱視角，純廣東話口語，Dcard風格]

2. 標題：[要點2標題]  
   描述：[詳細描述300-400字，第一人稱視角，純廣東話口語，Dcard風格]

3. 標題：[要點3標題]
   描述：[詳細描述300-400字，第一人稱視角，純廣東話口語，Dcard風格]

關鍵詞：[關鍵詞1], [關鍵詞2], [關鍵詞3]...
"""

    # Add randomization  
    prompt = add_randomization_to_prompt(prompt, scenario['theme'])

    response = await openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": prompt}
        ]
    )

    # Parse the response
    lines = response.choices[0].message.content.strip().split('\n')
    hook = ""
    story_points = []
    current_point = {}
    keywords = []
    
    for line in lines:
        line = line.strip()
        if line.startswith('鉤子：') or line.startswith('鉤子: '):
            hook = line.replace('鉤子：', '').replace('鉤子: ', '').strip()
        elif line.startswith('關鍵詞：') or line.startswith('關鍵詞: '):
            keywords = [k.strip() for k in line.replace('關鍵詞：', '').replace('關鍵詞: ', '').split(',') if k.strip()]
        elif line.startswith('1. 標題:') or line.startswith('2. 標題:') or line.startswith('3. 標題:') or line.startswith('1. 標題：') or line.startswith('2. 標題：') or line.startswith('3. 標題：'):
            if current_point:
                story_points.append(current_point)
            current_point = {'title': line.split('標題:')[1].strip() if '標題:' in line else line.split('標題：')[1].strip()}
        elif line.startswith('描述：') or line.startswith('描述: '):
            current_point['description'] = line.replace('描述：', '').replace('描述: ', '').strip()
    
    if current_point:
        story_points.append(current_point)
    
    return {
        'hook': hook,
        'story_points': story_points,
        'keywords': keywords,
        'scenario': scenario
    }

async def generate_relationship_conclusion_content(openai_client, story_content: dict):
    """Generate conclusion content for relationship posts"""
    
    # Get perspective from story content scenario
    scenario = story_content.get('scenario', {})
    perspective = scenario.get('perspective', 'female')
    
    if perspective == 'male':
        perspective_text = "男性視角"
        perspective_examples = "如「我真係唔知點算」、「我應該點做」"
        system_content = "你是一個感情顧問和社交媒體內容創作者。創建深思熟慮、吸引人的結論，邀請討論。必須用第一人稱角度（男性視角）和純正廣東話口語，語調親切自然，像朋友之間傾計咁樣。用「佢」、「嚟」、「咗」、「唔」、「點」、「嗰」等廣東話詞彙。\n\n**重要語言要求：**\n- 避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然或翻譯式表達\n- 不要使用書面語或過於正式的詞彙\n- 使用自然的口語表達，如「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」\n- 避免使用「真係為咗錢咩真係咁啦一齊？」這種結構混亂的句子\n- 使用清晰的問句結構，如「真係為咗錢咩？真係咁樣一齊？」\n- 避免使用「曬爛」、「有形嘅」、「意外嚇」等不常見或生硬的表達\n- 使用更自然的替代詞：\n  * 「借咩」→「咩男朋友嚟㗎」或「邊個男朋友」\n  * 「靠山走水」→「翻山越嶺」或「就算要行好遠」\n  * 「有形嘅」→「有型嘅」或「靚仔嘅」\n  * 「意外嚇」→「嚇親」或「嚇到」\n  * 「曬爛」→「曬到爛」或「曬到變色」"
    else:
        perspective_text = "女性視角"
        perspective_examples = "如「我真係唔知點算」、「我應該點做」"
        system_content = "你是一個感情顧問和社交媒體內容創作者。創建深思熟慮、吸引人的結論，邀請討論。必須用第一人稱角度（女性視角）和純正廣東話口語，語調親切自然，像朋友之間傾計咁樣。用「佢」、「嚟」、「咗」、「唔」、「點」、「嗰」等廣東話詞彙。\n\n**重要語言要求：**\n- 避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然或翻譯式表達\n- 不要使用書面語或過於正式的詞彙\n- 使用自然的口語表達，如「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」\n- 避免使用「真係為咗錢咩真係咁啦一齊？」這種結構混亂的句子\n- 使用清晰的問句結構，如「真係為咗錢咩？真係咁樣一齊？」\n- 避免使用「曬爛」、「有形嘅」、「意外嚇」等不常見或生硬的表達\n- 使用更自然的替代詞：\n  * 「借咩」→「咩男朋友嚟㗎」或「邊個男朋友」\n  * 「靠山走水」→「翻山越嶺」或「就算要行好遠」\n  * 「有形嘅」→「有型嘅」或「靚仔嘅」\n  * 「意外嚇」→「嚇親」或「嚇到」\n  * 「曬爛」→「曬到爛」或「曬到變色」"
    
    prompt = f"""根據感情故事要點，創建一個深思熟慮的結論：

故事鉤子：{story_content['hook']}
故事要點：{[point['title'] for point in story_content['story_points']]}

要求：
- 創建一個反思性問題或陳述（15-25個字）
- 應該邀請參與和討論
- 應該有同理心且容易產生共鳴
- 專注於普遍的感情困境
- 用第一人稱角度（{perspective_text}），{perspective_examples}
- 必須用純正廣東話口語，如「點算好」、「大家覺得呢」、「有冇人試過」
- **語言要求**：避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然表達，使用「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」等自然口語

只輸出結論信息，不要其他內容。
"""

    response = await openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": prompt}
        ]
    )

    conclusion = response.choices[0].message.content.strip()
    return {
        'conclusion': conclusion
    }

async def generate_instagram_caption(openai_client, story_content: dict, word_limit: int = 290):
    """Generate Instagram caption with hashtags"""
    
    # Get perspective from story content scenario
    scenario = story_content.get('scenario', {})
    perspective = scenario.get('perspective', 'female')
    
    if perspective == 'male':
        perspective_text = "男性視角"
        perspective_examples = "如「我...」、「我覺得...」、「我真係唔知...」"
        system_content = "你是專門創作Dcard風格感情內容的社交媒體內容創作者。寫出吸引人、情感豐富的標題，鼓勵互動。必須用第一人稱角度（男性視角）和純正廣東話口語，就像香港人日常講嘢咁樣自然。用詞要地道，包括所有廣東話特有詞彙和語法。內容要像Dcard貼文一樣真實、個人化、有強烈情緒感染力，讓讀者感同身受。\n\n**重要語言要求：**\n- 避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然或翻譯式表達\n- 不要使用書面語或過於正式的詞彙\n- 使用自然的口語表達，如「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」\n- 避免使用「真係為咗錢咩真係咁啦一齊？」這種結構混亂的句子\n- 使用清晰的問句結構，如「真係為咗錢咩？真係咁樣一齊？」\n- 避免使用「曬爛」、「有形嘅」、「意外嚇」等不常見或生硬的表達\n- 使用更自然的替代詞：\n  * 「借咩」→「咩男朋友嚟㗎」或「邊個男朋友」\n  * 「靠山走水」→「翻山越嶺」或「就算要行好遠」\n  * 「有形嘅」→「有型嘅」或「靚仔嘅」\n  * 「意外嚇」→「嚇親」或「嚇到」\n  * 「曬爛」→「曬到爛」或「曬到變色」"
    else:
        perspective_text = "女性視角"
        perspective_examples = "如「我...」、「我覺得...」、「我真係唔知...」"
        system_content = "你是專門創作Dcard風格感情內容的社交媒體內容創作者。寫出吸引人、情感豐富的標題，鼓勵互動。必須用第一人稱角度（女性視角）和純正廣東話口語，就像香港人日常講嘢咁樣自然。用詞要地道，包括所有廣東話特有詞彙和語法。內容要像Dcard貼文一樣真實、個人化、有強烈情緒感染力，讓讀者感同身受。\n\n**重要語言要求：**\n- 避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然或翻譯式表達\n- 不要使用書面語或過於正式的詞彙\n- 使用自然的口語表達，如「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」\n- 避免使用「真係為咗錢咩真係咁啦一齊？」這種結構混亂的句子\n- 使用清晰的問句結構，如「真係為咗錢咩？真係咁樣一齊？」\n- 避免使用「曬爛」、「有形嘅」、「意外嚇」等不常見或生硬的表達\n- 使用更自然的替代詞：\n  * 「借咩」→「咩男朋友嚟㗎」或「邊個男朋友」\n  * 「靠山走水」→「翻山越嶺」或「就算要行好遠」\n  * 「有形嘅」→「有型嘅」或「靚仔嘅」\n  * 「意外嚇」→「嚇親」或「嚇到」\n  * 「曬爛」→「曬到爛」或「曬到變色」"
    
    prompt = f"""根據這個感情故事創建Instagram標題（Dcard風格）：

鉤子：{story_content['hook']}
故事要點：{[f"{point['title']}: {point['description']}" for point in story_content['story_points']]}

要求：
1. 用第一人稱角度講述（{perspective_text}），{perspective_examples}
2. 用純正廣東話口語寫作，語調親切自然
3. 總共大約{word_limit}字（包括標籤）
4. 讓內容情感豐富且容易產生共鳴
5. **Dcard風格**：真實、個人化、情緒豐富、像朋友傾訴
6. 包括15-20個相關標籤
7. 使用吸引人的問題來鼓勵評論，如「大家點睇」、「有冇人試過」
8. 結構：介紹 → 故事摘要 → 反思 → 行動呼籲 → 標籤
9. 必須用廣東話詞彙：佢、嚟、咗、唔、點、乜、嗰、啲、俾、喺、嘅等
10. **語言要求**：避免使用「借咩」、「靠山走水」、「有形嘅」、「意外嚇」等不自然表達，使用「咩男朋友嚟㗎」、「就算要行好遠」、「真係咁樣一齊」等自然口語

輸出格式應該是完整的Instagram標題，準備發布。
"""

    response = await openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

async def generate_varied_relationship_content(openai_client):
    """Generate completely different relationship content each time"""
    # Get all stories from file
    scenarios = load_story_ideas_from_file()
    if not scenarios:
        scenarios = get_default_scenarios()
    
    # Pick random story
    selected_scenario = random.choice(scenarios)
    base_story = selected_scenario['story_template']
    
    # Generate all content with this story
    title_content = await generate_relationship_title_content(
        openai_client, base_story, selected_scenario
    )
    
    story_content = await generate_relationship_story_content(
        openai_client, base_story, selected_scenario
    )
    
    conclusion_content = await generate_relationship_conclusion_content(
        openai_client, story_content
    )
    
    ig_caption = await generate_instagram_caption(
        openai_client, story_content, word_limit=290
    )
    
    return {
        'scenario': selected_scenario,
        'base_story': base_story,
        'title_content': title_content,
        'story_content': story_content,
        'conclusion_content': conclusion_content,
        'ig_caption': ig_caption
    }

# Story templates for different relationship scenarios - DEPRECATED
# Now using story_ideas.txt file instead
RELATIONSHIP_STORY_TEMPLATES = {
    "superstition_plastic_surgery": {
        "title": "我迷信到要整容？",
        "hook": "我嘅愛情同迷信嘅界線喺邊度？",
        "story_points": [
            {
                "title": "IG買魔法蠟燭同淨化儀式",
                "description": "我會喺Instagram上面買嗰啲所謂嘅「能量蠟燭」，仲會搵人做啲咩淨化儀式。成個過程就係先私訊對方，提供啲個人資料，好似生日時間、地址、照片、父母姓名、出生地點咁樣，然後等對方影相俾我睇完成咗嘅「儀式」。有時係點蠟燭，有時係燒符咒，有時係用水晶擺陣，有時仲要我自己買埋一大堆配件返嚟。過幾日再問下效果點樣，如果無效果就話係「阻力太大」，要做多幾次先得。每次都要花好幾千蚊，貴嘅仲要成萬蚊，一個月落嚟隨時要兩三萬。我男朋友開始覺得呢啲好似詐騙多啲，但我話有效果，佢都唔知點講我好。我仲成日同佢講邊個朋友搵到好工、邊個脫單、邊個發咗財，話係因為做咗儀式。佢真係好無奈，試過同我講呢啲可能係巧合，但我唔聽，話佢唔信我，仲話佢負能量太重會影響效果。呢啲師父仲話我要定期做，如果唔做嘅話之前嘅功效會消失，所以我越來越沉迷，每個月都要做幾次。我哋嘅積蓄都俾我花晒，信用卡都爆晒，我仲想問屋企人借錢。佢真係開始擔心我係咪俾人呃緊，但又唔知點樣勸我，一講我就嬲。"
            },
            {
                "title": "面相點痣辭工躺平半年", 
                "description": "更加誇張嘅係，前排我去睇面相，個師父話我額頭上面有粒痣會影響運勢，會阻住我嘅事業運同財運，仲話會影響我同男朋友感情，建議我即刻去脫。我即刻就去點痣，話要改運。點痣之後無幾耐，我又去求籤，個老師話我今年犯太歲，財運特別唔好，唔適合工作，最好休息一年等運氣轉好，如果勉強返工會有血光之災。我竟然聽咗，直接同公司講辭職，連notice都唔俾，話要「順應天意」，整整喺屋企躺平咗半年。我男朋友當時真係好嬲，我哋本來計劃緊結婚買樓，而家冇咗我份收入，所有計劃都要推遲。但我話係為咗我自己好，要佢支持我，話如果勉強工作會有更大嘅災禍，會連累埋佢。佢諗住我可能真係需要休息下，工作壓力大，所以就由得我，仲要一個人供養成頭屋。點知我越來越深陷落去，成日都係上網睇風水命理，同啲師父傾計，買各種水晶護身符，完全唔諗搵工嘅事。佢催我搵工我就話時機未到，要等到明年先得，而家搵工會衰足十年。佢真係好絕望，唔知仲要養我幾耐。"
            },
            {
                "title": "為聚財要隆鼻整容",
                "description": "但係最令我男朋友震驚嘅係上個禮拜我同佢講嘅事。我睇咗某個風水師嘅YouTube片，話鼻頭要有肉先會聚財，鼻樑要高啲會增強貴人運，山根要飽滿先會有富貴命，所以我想去做鼻整形，特別要將個鼻頭整得豐滿啲，仲要墊高個鼻樑同山根。佢聽完真係好無言，雖然佢知道「鼻頭有肉聚財」呢個講法，但從來無諗過會有人為咗呢個去整容。我話已經上網搵咗好多間整容診所，仲book咗三間唔同嘅consultation，問佢意見支唔支持。佢真係唔知應該點反應，支持定反對？我話呢個係為咗我哋嘅未來，為咗有錢結婚買樓，改善我哋嘅生活。我仲話如果鼻相改好咗，我就會有財運，到時搵工都會順利啲，人工都會高啲，我哋就可以過好日子。但係整容要成十幾萬，我哋而家連積蓄都冇，我仲想用信貸去做。佢愛我，但係佢覺得呢啲都好瘋狂。整容唔係小事，有風險之餘仲要花好多錢，而且佢覺得我而家嘅樣已經好靚，唔需要改變。最重要係，佢唔覺得改個鼻就會發達，呢個世界邊有咁容易嘅事？"
            }
        ],
        "keywords": ["迷信", "整容", "愛情", "煩惱", "支持", "界線", "理解"]
    }
} 