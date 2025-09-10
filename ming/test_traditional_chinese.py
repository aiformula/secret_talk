#!/usr/bin/env python3
"""
測試繁體中文 - Test Traditional Chinese
"""

# 簡體中文檢測
simplified_chars = ['变', '发', '关', '学', '读', '处', '说', '过', '时', '问', '给', '对', '谢', '欢', '电', '买', '钱', '爱', '难']
traditional_chars = ['變', '發', '關', '學', '讀', '處', '說', '過', '時', '問', '給', '對', '謝', '歡', '電', '買', '錢', '愛', '難']

def test_text_conversion():
    """測試文字轉換"""
    
    print("=== 🇭🇰 繁體中文測試 ===")
    
    # 測試樣本文字
    test_samples = [
        "我發現我24歲嘅男朋友派帽俾我，影響到我 final year 嘅學業。",
        "原來發現一個人呃你，個心係會『咯』一聲，然後靜晒。",
        "我同佢，23歲同24歲，喺人哋眼中襯到絕。",
        "而家 final year 都讀唔落，成日諗住呢件事。"
    ]
    
    print("✅ 測試樣本（應該全部是繁體字）：")
    for i, sample in enumerate(test_samples, 1):
        print(f"   {i}. {sample}")
        
        # 檢查是否包含簡體字
        has_simplified = any(char in sample for char in simplified_chars)
        has_traditional = any(char in sample for char in traditional_chars)
        
        if has_simplified:
            print(f"      ⚠️ 發現簡體字！")
        else:
            print(f"      ✅ 純繁體字")
    
    print("\n=== 📋 字符對比 ===")
    print("簡體 → 繁體")
    for s, t in zip(simplified_chars, traditional_chars):
        print(f"  {s} → {t}")
    
    print("\n=== 🎯 香港粵語特色詞彙 ===")
    hk_phrases = [
        "派帽俾我",
        "final year",
        "讀唔落",
        "諗住",
        "好似",
        "係會",
        "嘅",
        "佢",
        "唔",
        "俾",
        "咗",
        "呢",
        "嗰",
        "咁"
    ]
    
    for phrase in hk_phrases:
        print(f"  ✅ {phrase}")
    
    print("\n🎉 繁體中文測試完成！")

if __name__ == "__main__":
    test_text_conversion() 