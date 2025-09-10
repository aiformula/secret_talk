# 禁止使用嘅詞語清單
# 呢啲詞語唔係香港人會用嘅，要避免使用

BANNED_WORDS = [
    # 唔自然嘅廣東話詞語
    "派頭",
    "食檸檬鵝", 
    "心窒",
    "隱藏自我",
    "迷糊",
    "落到真",
    "變動之中",
    "排洩閥門",
    "慶祝出生係佢個機",
    
    # 過於書面化嘅詞語
    "然而",
    "因此",
    "故此",
    "於是乎",
    "不過",
    
    # 唔自然嘅英文混雜
    "relationship",  # 應該用「關係」
    "time",          # 應該用「時間」
    "insecurity",    # 應該用「不安」
    "quality time",  # 應該用「相處時間」
    "background",    # 應該用「背景」
    "ready",         # 應該用「準備好」
    
    # 過於正式嘅詞語
    "戀愛關係",
    "感情生活",
    "情感交流",
    "心靈溝通",
    
    # 唔自然嘅表達
    "我唔知",
    "我唔明白",
    "我唔清楚"
]

# 建議用嘅自然表達
NATURAL_EXPRESSIONS = {
    "我唔知": "我知唔到",
    "我唔明白": "我唔明", 
    "我唔清楚": "我唔清楚",
    "relationship": "關係",
    "time": "時間",
    "insecurity": "不安",
    "quality time": "相處時間",
    "background": "背景",
    "ready": "準備好"
}

def check_banned_words(text):
    """檢查文本係咪包含禁止詞語"""
    found_words = []
    for word in BANNED_WORDS:
        if word in text:
            found_words.append(word)
    return found_words

def replace_with_natural(text):
    """將唔自然嘅表達替換成自然嘅表達"""
    for old, new in NATURAL_EXPRESSIONS.items():
        text = text.replace(old, new)
    return text 