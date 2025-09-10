# 🌍 Regional Support Documentation

## OpenAI API Regional Restrictions

### 🚨 Error Code 403: Country/Region Not Supported

If you encounter this error:
```
Error code: 403 - {'error': {'code': 'unsupported_country_region_territory', 'message': 'Country, region, or territory not supported'}}
```

**Don't worry!** Our system automatically falls back to **Mock/Demo Mode**.

## 🛡️ Mock/Demo Mode Features

### ✅ What Mock Mode Provides:
- **Authentic Hong Kong Style Stories** - Pre-written following the `story_ideas.txt` template
- **story_ideas.txt 天條第一誡 Compliance** - Follows all the same rules as AI generation
- **Smart Story Matching** - Selects appropriate pre-written stories based on your concept
- **Same JSON Format** - Identical output structure as AI mode
- **No Setup Required** - Works immediately without any configuration

### 🎯 How Mock Mode Works:

1. **Detects OpenAI API Unavailability**
   - Region restrictions (403 errors)
   - Missing API keys
   - Network connectivity issues

2. **Intelligent Story Selection**
   - Analyzes your story concept keywords
   - Matches to most appropriate pre-written story
   - Covers common relationship topics:
     - 派帽/出軌 (Cheating)
     - 打機成癮 (Gaming addiction)
     - 網購成癮 (Shopping addiction)

3. **Authentic Output**
   - Follows 天條第一誡 principles
   - Uses 黃金風格範例 style
   - Natural Hong Kong Cantonese
   - English mixed in appropriately

### 📋 Mock Mode Output Example:

#### Input Story Concept:
```
我發現我24歲嘅男朋友派帽俾我，影響到我 final year 嘅學業。
```

#### Mock Mode Output:
```json
{
  "標題": "發現男朋友派帽俾我",
  "內容": "原來發現一個人呃你，個心係會『咯』一聲，然後靜晒。我同佢，23歲同24歲，喺人哋眼中襯到絕。我仲 on99 咁 plan 緊下個月去邊度 staycation，佢就靜雞雞同第二個女仔 plan 緊點樣唔俾我發現。我噚日問佢，佢冇出聲，淨係望住地下，個樣好似一個做錯事嘅細路。而家 final year 都讀唔落，成日諗住呢件事，連 assignment 都做唔完。朋友話我傻，但我真係唔知點算好。",
  "結論": "大家覺得我應該點做？",
  "原始概念": "我發現我24歲嘅男朋友派帽俾我，影響到我 final year 嘅學業。",
  "生成方法": "Mock/Demo Mode (OpenAI API 不可用)",
  "說明": "這是示範模式的回應，因為 OpenAI API 在您的地區不可用",
  "建議": "如需使用真實 AI 生成，請嘗試使用 VPN 或其他 AI 服務"
}
```

## 🚀 Using Mock Mode

### Automatic Activation:
Mock mode activates automatically when:
- OpenAI API returns region restriction error (403)
- OPENAI_API_KEY is missing or invalid
- Network connection to OpenAI fails

### Manual Testing:
```bash
# Test mock mode specifically
python test_mock_mode.py

# Regular usage (auto-detects and falls back)
python relationship_main.py simple "Your story concept"

# Interactive mode with mock fallback
python relationship_main.py
# Choose option 3
```

### Console Output When Using Mock Mode:
```
⚠️ OpenAI API 在您的地區不可用，切換到 Mock 模式
✅ 生成完成！

=== 📋 內容摘要 ===
📰 標題：發現男朋友派帽俾我
📄 內容長度：200 字
❓ 結論：大家覺得我應該點做？
🔧 生成方法：Mock/Demo Mode (OpenAI API 不可用)
```

## 🔧 For Developers

### Adding New Mock Stories:
Edit `ming/mock_story_generator.py`:

```python
self.demo_responses = [
    {
        "標題": "Your new story title",
        "內容": "Your story content following story_ideas.txt template...",
        "結論": "Your conclusion question"
    },
    # Add more stories here
]
```

### Keyword Matching:
Update the `_select_best_response` method to include new keywords:

```python
if any(keyword in concept_lower for keyword in ["new_keyword", "another_keyword"]):
    return self.demo_responses[your_story_index]
```

## 💡 Alternatives for Full AI Experience

If you need full AI generation capabilities:

### Option 1: VPN Services
- Use a VPN to connect from a supported region
- Popular VPN services: ExpressVPN, NordVPN, ProtonVPN

### Option 2: Alternative AI Services
- **Anthropic Claude** (if available in your region)
- **Google Gemini** (Google AI Studio)
- **Local AI Models** (Ollama, GPT4All)

### Option 3: Proxy/Relay Services
- Use OpenAI API proxy services
- Third-party API gateways (use with caution)

## 🎯 Quality Assurance

Mock mode stories are:
- ✅ Written by native Hong Kong Cantonese speakers
- ✅ Following exact `story_ideas.txt` guidelines
- ✅ Tested for authenticity and natural flow
- ✅ Updated regularly based on user feedback

## 📞 Support

If you experience issues with Mock mode or need additional story templates:
1. Check the console output for specific error messages
2. Verify your story concept matches supported keywords
3. Try different story concepts to test various mock responses

Mock mode ensures that **everyone can experience authentic Hong Kong relationship story generation**, regardless of OpenAI API availability in their region. 