#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
香港風格用詞同表達方式收集
用嚟改善內容生成嘅香港特色
"""

# 香港地道用詞同表達
HONG_KONG_STYLE_PHRASES = {
    # 禮貌同尊重
    "禮貌用詞": [
        "基本尊重同禮貌都要有🙏🏻",
        "樓主可能都要顧男朋友感受",
        "分翻開媽媽同男朋友相處",
        "至少唔好令男朋友嘅hard feelings上升到覺得你冇平衡好先",
        "樓主既然都有分寸",
        "唔同意你媽媽睇法就儘管順住自己個flow去處事",
    ],
    
    # 職業相關
    "職業評價": [
        "貨車司機起薪高",
        "未來藍圖都暫時冇辦法用ai取代",
        "你媽媽比人炒都輪唔到佢",
        "我自己做機場物流",
        "我間公司司機起薪40k+",
        "日日仲叫加人工",
        "美國揸貨車係top tier藍領好多人想做",
        "喺香港即刻俾人白鴿眼",
    ],
    
    # 關係建議
    "關係建議": [
        "有咩問題",
        "佢係咩職業真係咁重要咩",
        "佢地一樣過得咁開心",
        "只要你唔介意",
        "其實就唔關其他人事",
        "就算係你屋企都好",
        "始終同你過人世個個係佢唔係你屋企人",
        "結左婚之後你就會明點解拍拖係一啲都唔關你屋企人事",
    ],
    
    # 性觀念討論
    "性觀念": [
        "唔會主動提出，但對方提出就唔會拒絕",
        "師兄，唔好信呢到啲粉頭講野",
        "D卡好多Post粉頭講性事不合",
        "佢地形式上一齊咗先上床，之後埋牙唔得就分手",
        "本質並無分別，一樣係重性",
        "有女仔可以比你試車，係食完再諗，係對佢自己同你都負咗責任",
        "人地提出，又唔係你",
        "你碌鳩唔岩砌咪即係你地唔夾囉",
        "人地有性需要有要求 想試下你碌野",
        "唔夾過點知夾唔夾",
        "拍拖都係試下大家行唔行到下一步",
        "一埋黎直接結婚？",
        "買野食都要試食啦",
    ],
    
    # 世代觀念
    "世代觀念": [
        "其實唔關genz事",
        "英美嘅millenials都會係咁",
        "分別就在於佢地男女朋友關係",
        "係要親密相處一段時間",
        "確認啱feel可以長遠發展",
        "先會升級做男女朋友",
        "其實咁樣反而係對戀愛關係重視",
        "因為唔想輕易開始一段感情",
        "而傳統性觀念係相反",
        "重視性親密嘅行為",
        "但對開始一段感情相對輕率",
        "甚至有啲人會為扑嘢而去講「我愛你」",
        "但喺歐美價值觀入面",
        "講我鍾意你係一回事",
        "但講我愛你係完全另一個階段",
    ],
    
    # 女性觀點
    "女性觀點": [
        "接受到，個人認為依家時代試車真係冇想像中咁大件事",
        "反而係對對方嘅尊重🙂‍↕️",
        "好過一齊左，有左感情基礎之後先發現原來性事夾唔到",
        "戴翻頭盔，每個人唔同，只要雙方同意就絕對冇問題",
        "扑野，第一次最痛嘅都係女仔",
        "HPV，得女仔會發病，男仔帶病但唔會發病",
        "用套都會傳染",
        "套穿左，食事後藥，痛到仆街",
        "對身體有永久傷害",
        "重要食完都有機會無清走",
        "然後就用藥墮胎",
        "用藥，大出血，藥落得唔乾淨，就會清子宮，又係痛",
        "心理上，焦慮嘅都係女仔，男仔依然一切如常",
        "最後，落過仔會被世人當係污點",
        "而令女朋友落過仔嘅男人，係唔會受到任何社會指責🙂",
        "所以女仔要好好保護自己",
        "安全措施同簡對象要更謹慎",
        "扑野係雙方享受，但後果得你承擔",
    ],
    
    # 約會建議
    "約會建議": [
        "我建議你就直接約出來",
        "一開始係真系好撚kam",
        "如果齋網上傾係好難熟到",
        "如果佢對你有興趣唔會拒絕你",
        "睇電影咯😂",
        "首先要知嗰種係舒服嘅靜處定唔舒服嘅dead air先",
        "因為i人眼中冇嘢講未必係問題黎",
        "甚至可能覺得兩個人靜靜地幾好",
        "搞清楚佢有冇興趣/點諗先算啦",
        "睇佢有咩興趣，由興趣入手可能多野講d",
        "然後睇下有無咩藉口約佢出街",
        "最好同佢興趣有關，譬如食野",
        "如果你約佢兩三次都推既話咁就應該無機",
        "如果約到兩次咁應該有機",
        "熟d之後可以開始嘗試營造少少曖昧既氛圍但唔好太明顯",
        "佢唔反感甚至你feel到佢可能都有d好感就可以進取d",
        "類似溫水煮青蛙？",
    ],
    
    # 男性心理
    "男性心理": [
        "以我理解既男仔心理：",
        "前期-佢點解成日搵我仲約我出街既？",
        "佢係咪鍾意我？",
        "佢點會鍾意我應該係我諗多咗",
        "鍾意既話-心底偷笑",
        "可能自己都唔知自己對你有feel",
        "但同你傾計/見面會開心",
    ],
    
    # 網絡互動
    "網絡互動": [
        "如果久唔久send下IG post/reels俾對方",
        "通常都係自己做主動",
        "其實男仔get唔get到~",
        "男仔會察覺到啲咩先發現有人對自己有好感?🥹",
        "淨係send reels 之類",
        "唔會get到",
        "get到都係男方幻想",
        "有好感要約",
        "食飯行街睇戲咩都好",
    ],
    
    # 內向者相處
    "內向者相處": [
        "近排識咗個i仔，好易怕醜好cute",
        "完全係理想型好想approach…",
        "但係真係好易dead air🥹",
        "有無人試過/i仔現身說法",
        "我都係i仔，好慢熱唔識傾計",
        "然後做group project 識咗依家女朋友",
        "嗰時完sem鼓起咗好大嘅勇氣問佢攞ig",
        "所以話就算係i仔只要佢對你有興趣點都會有行動",
    ],
    
    # 批評同指責
    "批評指責": [
        "你呀媽真心無禮貌同唔尊重",
        "對你男朋友冇禮貌加上唔尊重你嘅選擇",
        "有意見可以私底下再講姐",
        "擺上枱面嚟講真係好肉酸",
        "點解呢到99%嘅藍頭都反對樓主",
        "係因為你開地圖炮鬧晒所有男仔",
        "將女仔放係低位",
        "可能你唔係咁意思，但係俾人感覺似女權撚",
    ],
    
    # 風險意識
    "風險意識": [
        "你講果啲風險係存在",
        "所以啲男人都會願意compensate",
        "啲ex全部走AA又車出車入",
        "唔洗夾租/夾供樓",
        "旅行又唔洗出",
        "過節又花又名牌",
        "咁同佢扑野唔過份呀",
        "我又有得爽，爽完其他又唔洗付出",
        "帶套打hpv咪得",
        "咩都有風險出街都會比車撞架啦",
        "有份爽架maaa",
    ],
    
    # 責任觀念
    "責任觀念": [
        "其實我自己覺得係雙方責任啦",
        "拍拖扑野無問題",
        "男方係愛錫女方既話自然會心痛女方",
        "自然唔會比女方做以上既事",
        "不過講到尾都係講緊你揀個咩男仔做男朋友",
        "我知有咗引申好多考量",
        "例如你想唔想生",
        "或者你想唔想結婚",
        "但就咁已經好多變數😂",
    ],
    
    # 安全措施
    "安全措施": [
        "女仔個生理構造就係會比較容易受感染",
        "condom戴啱正常就好少傳染到性病嘅",
        "當然啦，要識得篩選一個有正確避孕常識嘅伴侶都好緊要嘅",
        "唔好話咩啱啱嚟完m可以唔用套",
        "pull&pray唔會中嘅",
        "喺出面磨完入幾下先戴",
        "戴咗射完再隊多幾下嗰啲全部都有機會中！！！",
        "我覺得如果女仔都100%同意拍拖可以有性行為",
        "而男仔係尊重同保護女朋友嘅",
        "就唔好覺得女性係處於弱勢嘅位置上",
        "對有咗真係好有concern嘅建議唔好扑",
        "因為就算扑咗都唔會享受嘅",
    ],
}

# 香港特色語氣詞
HONG_KONG_TONE_MARKERS = [
    "🙏🏻", "😂", "🥹", "🙂‍↕️", "🙂", "😃", "🫩", "🚬", "🤨", "🤣", "😗", "😢"
]

# 香港地道動詞
HONG_KONG_VERBS = [
    "扑野", "埋牙", "試車", "食完再諗", "外射", "內射", "中獎", "落仔", "墮胎",
    "揼", "掃", "shoot", "嘈", "approach", "dead air", "get到", "feel到",
    "約出來", "傾計", "出街", "食飯", "行街", "睇戲", "睇電影"
]

# 香港地道形容詞
HONG_KONG_ADJECTIVES = [
    "好撚kam", "好易怕醜", "好cute", "好慢熱", "好肉酸", "好有concern",
    "好難熟到", "好易dead air", "好大嘅勇氣", "好有興趣", "好有feel"
]

# 香港地道名詞
HONG_KONG_NOUNS = [
    "粉頭", "藍頭", "i仔", "group project", "sem", "ig", "reels", "post",
    "hard feelings", "flow", "dead air", "HPV", "condom", "AA制"
]

def get_hong_kong_style_phrases(category=None):
    """獲取香港風格用詞"""
    if category:
        return HONG_KONG_STYLE_PHRASES.get(category, [])
    return HONG_KONG_STYLE_PHRASES

def get_random_hong_kong_phrase(category=None):
    """隨機獲取香港風格用詞"""
    import random
    if category:
        phrases = HONG_KONG_STYLE_PHRASES.get(category, [])
    else:
        # 隨機選擇一個類別
        category = random.choice(list(HONG_KONG_STYLE_PHRASES.keys()))
        phrases = HONG_KONG_STYLE_PHRASES[category]
    
    if phrases:
        return random.choice(phrases)
    return ""

def is_hong_kong_style(text):
    """檢查文本是否包含香港風格元素"""
    text_lower = text.lower()
    
    # 檢查語氣詞
    has_tone_markers = any(marker in text for marker in HONG_KONG_TONE_MARKERS)
    
    # 檢查地道動詞
    has_hk_verbs = any(verb in text_lower for verb in HONG_KONG_VERBS)
    
    # 檢查地道形容詞
    has_hk_adjectives = any(adj in text_lower for adj in HONG_KONG_ADJECTIVES)
    
    # 檢查地道名詞
    has_hk_nouns = any(noun in text_lower for noun in HONG_KONG_NOUNS)
    
    return has_tone_markers or has_hk_verbs or has_hk_adjectives or has_hk_nouns

def enhance_hong_kong_style(text, category=None):
    """增強文本嘅香港風格"""
    import random
    
    # 隨機添加語氣詞
    if random.random() < 0.3:  # 30%機率添加語氣詞
        tone_marker = random.choice(HONG_KONG_TONE_MARKERS)
        text += f" {tone_marker}"
    
    # 隨機添加香港風格短語
    if random.random() < 0.2:  # 20%機率添加短語
        phrase = get_random_hong_kong_phrase(category)
        if phrase:
            text += f" {phrase}"
    
    return text

if __name__ == "__main__":
    # 測試功能
    print("=== 香港風格用詞測試 ===")
    
    # 測試獲取類別
    print("\n1. 禮貌用詞：")
    phrases = get_hong_kong_style_phrases("禮貌用詞")
    for i, phrase in enumerate(phrases[:3], 1):
        print(f"{i}. {phrase}")
    
    # 測試隨機獲取
    print("\n2. 隨機短語：")
    for i in range(3):
        phrase = get_random_hong_kong_phrase()
        print(f"{i+1}. {phrase}")
    
    # 測試風格檢查
    print("\n3. 風格檢查：")
    test_texts = [
        "我同佢拍拖好開心",
        "我同佢拍拖好開心😂",
        "我同佢扑野好開心",
        "我同佢約出來食飯"
    ]
    
    for text in test_texts:
        is_hk = is_hong_kong_style(text)
        print(f"'{text}' -> {'✅ 香港風格' if is_hk else '❌ 普通風格'}")
    
    # 測試風格增強
    print("\n4. 風格增強：")
    original_text = "我覺得呢件事好重要"
    enhanced_text = enhance_hong_kong_style(original_text)
    print(f"原文：{original_text}")
    print(f"增強：{enhanced_text}") 