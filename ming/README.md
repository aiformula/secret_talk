# 🎭 Secret Talk - 感情故事生成器

一個先進嘅 AI 驅動系統，專門為社交媒體平台（如 Dcard）生成感情故事內容，具備自動視角檢測同動態視覺生成功能。

## 📋 系統概覽

呢個系統可以自動將簡單嘅文字輸入轉換成引人入勝嘅感情故事，生成：
- **吸引人嘅標題** 配關鍵詞高亮顯示
- **多部分故事內容** 具備情感深度
- **發人深省嘅結論** 鼓勵討論
- **Instagram 標題** 配相關標籤
- **精美圖片集** 配合視角適當嘅背景
- **Telegram 自動發佈** 即時分享

## 🆕 最新功能：story_ideas.txt 天條第一誡

我哋而家跟足 **story_ideas.txt** 模板同 **天條第一誡**，確保 100% 遵循你嘅故事概念：

### 🎯 天條第一誡結構：
1. **❗ 天條第一誡** - 100% 絕對遵循你嘅故事概念
2. **角色扮演指令** - 23歲女性，凌晨3點，思緒破碎
3. **展示，唔好解釋** - 用細節展示，唔好直接解釋
4. **風格學習** - 完全跟足黃金風格範例
5. **禁止事項** - 嚴格規定 AI 唔可以做咩

### ✅ 主要特色：
- **絕對服從** - 100% 跟足你嘅故事概念，唔加嘢，唔改嘢
- **角色扮演** - 23歲女性凌晨3點嘅混亂思緒
- **展示唔好解釋** - 用細節展示情感，唔係直接解釋
- **香港口語** - 自然嘅廣東話夾雜英文（final year、check 電話、IG story）
- **黃金風格範例** - 跟足提供嘅風格模板
- **嚴格禁止** - 清楚規定 AI 唔可以做嘅事

### 🌍 地區支援同模擬模式：
- **OpenAI API 可用**：完整 AI 驅動故事生成
- **OpenAI API 受限**：自動切換到模擬/示範模式
- **模擬模式功能**：預寫嘅正宗香港風格故事，符合你嘅故事概念
- **無縫體驗**：系統自動檢測 API 可用性並切換模式
- **📖 詳細指南**：睇 [REGIONAL_SUPPORT.md](REGIONAL_SUPPORT.md) 獲取完整文檔

### 🚀 使用方法：

#### 命令行使用：
```bash
# 使用簡單生成器配默認故事
python relationship_main.py simple

# 使用自定義故事概念
python relationship_main.py simple "你嘅故事概念..."

# 測試 story_ideas.txt 模板
python test_simple_generator.py

# 測試特定故事概念
python test_simple_with_story_concept.py

# 專門測試模擬模式
python test_mock_mode.py
```

#### 互動模式：
```bash
python relationship_main.py
# 然後選擇選項 3：story_ideas.txt 天條第一誡
```

### 📋 JSON 輸出格式：
```json
{
  "標題": "[6-12字標題，要吸引人]",
  "內容": "[完整故事，跟足黃金風格範例，150-200字]",
  "結論": "[簡短問句，問大家意見，6-10字]",
  "原始概念": "你嘅原始故事概念",
  "生成方法": "story_ideas.txt 天條第一誡"
}
```

### 🛡️ 模擬模式（適用於受限地區）：
```json
{
  "標題": "[正宗香港風格標題]",
  "內容": "[預寫故事跟足 story_ideas.txt 模板]",
  "結論": "[自然結論問題]",
  "原始概念": "你嘅原始故事概念",
  "生成方法": "模擬/示範模式（OpenAI API 不可用）",
  "說明": "呢個係示範模式嘅回應，因為 OpenAI API 喺你嘅地區不可用",
  "建議": "如需使用真實 AI 生成，請嘗試使用 VPN 或其他 AI 服務"
}
```

## 📝 最新功能：自定義故事圖片生成

我哋而家支援 **自定義故事內容生成**，你可以使用自己嘅故事內容而唔需要任何修改！

### 🎯 功能概覽：
- ✅ **原文不變** - 使用你嘅原文，完全唔修改
- ✅ **自動分割** - 智能將你嘅故事分割成標題、內容同結論
- ✅ **專業圖片** - 從你嘅內容生成 6 張專業圖片
- ✅ **Telegram 發送** - 自動上傳到你嘅 Telegram

### 🚀 使用方法：

#### 第一步：編輯你嘅故事檔案
編輯 `my_custom_story.txt`：
```
你嘅標題（第一行）

你嘅主要內容
可以分幾段來寫
每段之間用空行分開

你嘅結尾問句（最後一行）
```

#### 第二步：運行系統
```bash
python relationship_main.py
# 選擇選項 6：自定義故事圖片生成
```

#### 第三步：生成輸出
- 📰 **標題圖片**：使用你嘅標題
- 📄 **內容圖片**：3 張圖片，自動分割你嘅內容
- ❓ **結論圖片**：你嘅結尾問題
- 🎨 **結束圖片**：標準結尾圖片

### 📁 生成檔案：
```
title.png              # 你嘅標題
content_page1.png       # 你內容嘅第一部分
content_page2.png       # 你內容嘅第二部分  
content_page3.png       # 你內容嘅第三部分
conclusion.png          # 你嘅結論
end.png                # 標準結尾
```

### 🧪 測試：
```bash
python test_custom_story.py
```

### 📖 完整指南：
睇 [CUSTOM_STORY_GUIDE.md](CUSTOM_STORY_GUIDE.md) 獲取詳細說明同例子。

## 🏗️ 系統架構

### 核心檔案結構

```
├── story_ideas.txt                    # 輸入故事配視角標記
├── my_custom_story.txt                # 最新：自定義故事輸入檔案
├── relationship_main.py               # 主要執行協調器
├── relationship_content_generator.py  # AI 內容生成引擎
├── simple_story_generator.py         # 最新：超簡單故事生成器
├── custom_story_reader.py            # 最新：自定義故事讀取器同處理器
├── test_simple_generator.py          # 最新：簡單生成器測試腳本
├── test_custom_story.py              # 最新：自定義故事測試腳本
├── relationship_template_generator.py # HTML 模板創建器
├── image_generator.py                # PNG 圖片生成器
├── telegram_sender.py                # Telegram 發佈自動化
├── config.py                         # 環境設置
├── CUSTOM_STORY_GUIDE.md             # 最新：完整自定義故事指南
└── generated_ig_caption.txt          # 輸出 Instagram 標題
```

### 生成輸出檔案

```
├── title.png           # 主標題幻燈片
├── content_page1.png   # 故事第一部分
├── content_page2.png   # 故事第二部分
├── content_page3.png   # 故事第三部分
├── conclusion.png      # 結論幻燈片
├── end.png            # 結尾幻燈片
└── generated_simple_content.json     # 最新：簡單生成器輸出
```

## 🎯 完整工作流程

### 1. 故事輸入同視角檢測

**輸入**：`story_ideas.txt`
```
# 感情故事概念 - 女性第一人稱視角
我沉迷社交媒體，日日都要影相打卡...

# 感情故事概念 - 男性第一人稱視角  
我女朋友網購成癮，每日都要買嘢...
```

**檢測邏輯**：
- 系統掃描註釋中嘅視角標記
- `女性第一人稱視角` → 設置視角為 "female"
- `男性第一人稱視角` → 設置視角為 "male"
- 故事繼承佢哋所屬部分嘅視角

### 2. AI 內容生成流水線

#### 傳統方法：

##### Phase 1: Title Generation
```python
generate_relationship_title_content()
```
- **Input**: Raw story text + perspective
- **AI Prompt**: Dynamically adapts based on perspective
  - Female: "用第一人稱角度（女性視角），如「我...」、「我應該點做」"
  - Male: "用第一人稱角度（男性視角），如「我女朋友...」、「佢...」"
- **Output**: Title + highlighted keywords
- **Special Feature**: Comma formatting (title with "，" splits into multiple lines)

##### Phase 2: Story Content Generation
```python
generate_relationship_story_content()
```
- **Input**: Base story + perspective
- **Process**: Extracts 3 dramatic story points with detailed descriptions (300-400 words each)
- **AI Adaptation**: 
  - Female perspective: Self-focused narrative
  - Male perspective: Girlfriend-focused narrative
- **Output**: Hook + 3 story points + keywords

##### Phase 3: Conclusion Generation
```python
generate_relationship_conclusion_content()
```
- **Input**: Story points summary
- **Purpose**: Creates reflective questions that invite discussion
- **Output**: Empathetic conclusion tailored to perspective

##### Phase 4: Instagram Caption
```python
generate_instagram_caption()
```
- **Input**: Complete story content
- **Output**: ~290 word caption with 15-20 hashtags in pure Cantonese

#### NEW: story_ideas.txt 天條第一誡 Method:

```python
generate_simple_story()
```
- **Input**: Story concept string
- **Process**: 
  1. 天條第一誡 - 100% absolute adherence to story concept
  2. 角色扮演 - 23-year-old female, 3 AM, fragmented thoughts
  3. 展示唔好解釋 - Show through details, not explanations
  4. 黃金風格範例 - Follow exact style template
  5. 嚴格禁止 - Clear restrictions on what AI cannot do
- **Output**: JSON with title, content, conclusion following story_ideas.txt template
- **Style**: Hong Kong Cantonese, mixed English, authentic emotions, broken thoughts

### 3. Visual Template Generation

#### Template Creation
```python
relationship_template_generator.py
```

**Perspective-Based Background Selection**:
- **Female Perspective**: `title_girl.png`, `content_page1_girl.png`, etc.
- **Male Perspective**: `title_boy.png`, `content_page1_boy.png`, etc.

**Template Types**:
- **Title Template**: Main story title with highlighted keywords
- **Story Templates**: 3 content pages with story points
- **Conclusion Template**: Final question/reflection
- **End Template**: Closing slide

#### Image Generation
```python
image_generator.py
```
- **HTML to PNG**: Uses `imgkit` and `wkhtmltoimage`
- **Responsive Design**: Templates adapt to different content lengths
- **Typography**: Custom fonts and styling for readability
- **Color Schemes**: Perspective-appropriate color palettes

### 4. Instagram Optimization System

#### Performance Analysis
```python
ig_optimization.py
```
- **Content Scoring**: Analyzes engagement potential (0-100)
- **Optimal Timing**: Calculates best posting times
- **Hashtag Strategy**: Generates targeted hashtag groups
- **Engagement Tips**: Provides improvement suggestions

#### Posting Schedule
- **Weekly Calendar**: Strategic posting times
- **Audience Analysis**: Hong Kong timezone optimization
- **Content Variety**: Balanced emotional themes

### 5. Automated Distribution

#### Telegram Integration
```python
telegram_sender.py
```
- **Multi-Image Posts**: Sends complete image sets
- **Caption Generation**: Optimized Instagram captions
- **Error Handling**: Robust delivery with retry logic

## 📊 Content Quality Features

### Language Processing
- **Pure Cantonese**: Authentic Hong Kong expressions
- **Perspective Awareness**: Gender-appropriate language patterns
- **Emotional Authenticity**: Real relationship dynamics
- **Cultural Context**: Hong Kong social media culture

### Content Optimization
- **Engagement Scoring**: Predicts viral potential
- **Hashtag Intelligence**: Strategic tag selection
- **Timing Optimization**: Peak audience engagement
- **Visual Consistency**: Brand-aligned image generation

## 🛠️ 設置同配置

### 先決條件
```bash
pip install openai python-dotenv imgkit asyncio pathlib requests
```

### 環境變數
```bash
OPENAI_API_KEY=你嘅_openai_api_key
TELEGRAM_BOT_TOKEN=你嘅_telegram_bot_token
TELEGRAM_CHAT_ID=你嘅_telegram_chat_id
```

### 系統依賴
- **wkhtmltoimage**：用於 HTML 轉 PNG 轉換
- **字體檔案**：需要中文字體支援

## 🚀 使用例子

### 快速開始（簡單模式）
```bash
# 互動模式配選單
python relationship_main.py

# 直接使用簡單生成器
python relationship_main.py simple "我男朋友成日打機..."

# 使用 story_ideas.txt 模板測試
python test_simple_generator.py

# 使用特定故事概念測試
python test_simple_with_story_concept.py
```

### 傳統完整生成
```bash
# 完整流水線配圖片
python relationship_main.py

# 只生成短內容
python relationship_main.py short

# 性能分析
python relationship_main.py report
```

### 進階使用
```bash
# 互動測試
python test_simple_generator.py interactive

# 批量測試配例子
python test_simple_generator.py
```

## 📈 Performance Metrics

### Content Analysis
- **Engagement Score**: 0-100 rating system
- **Viral Potential**: Hashtag and timing optimization
- **Language Quality**: Natural Cantonese assessment
- **Emotional Impact**: Relationship story effectiveness

### System Performance
- **Generation Speed**: ~30-45 seconds per complete set
- **Success Rate**: 99%+ content generation success
- **Image Quality**: High-resolution PNG output
- **Distribution**: Automated multi-platform posting

## 🎨 Customization Options

### Content Themes
- Relationship conflicts and resolutions
- Social media and modern dating
- Personal growth and self-reflection
- Hong Kong cultural references

### Visual Styling
- **Color Schemes**: Customizable palettes
- **Typography**: Multiple font options
- **Layout Templates**: Various story formats
- **Background Graphics**: Perspective-appropriate designs

### AI Parameters
- **Model Selection**: GPT-4 for premium quality
- **Temperature Settings**: Balanced creativity and consistency  
- **Prompt Engineering**: Optimized for Cantonese output
- **Response Formatting**: Structured JSON output

## 🔧 Troubleshooting

### Common Issues
1. **Missing API Keys**: Check environment variables
2. **Font Rendering**: Ensure Chinese fonts installed
3. **Image Generation**: Verify wkhtmltoimage installation
4. **Network Errors**: Check OpenAI API connectivity

### Debug Mode
```bash
# Enable verbose logging
python relationship_main.py test

# Simple generator debugging
python test_simple_generator.py interactive
```

## 📝 Contributing

### Development Guidelines
- Follow existing code structure
- Test new features thoroughly
- Maintain Cantonese language quality
- Document API changes

### Feature Requests
- Content generation improvements
- New perspective options
- Additional social media platforms
- Enhanced visual templates

---

## 🎯 story_ideas.txt 天條第一誡文檔

### ❗ The Unbreakable Command Structure

#### 1. 天條第一誡 (The Unbreakable Command)
- **Rule**: **100% 絕對、完全、精準地** follow the user's story concept
- **Forbidden**: 絕對唔准 add new themes, ignore details, or change the story
- **Principle**: User's story concept is **鐵律** (iron law) - only expand it, don't modify

#### 2. 角色扮演指令 (Role-Playing Instructions)
- **Character**: 23-year-old female, 3 AM, confused thoughts
- **Setting**: In bed, using phone, experiencing fragmented thinking
- **Mental State**: 個心好亂，思緒係破碎、跳躍嘅

#### 3. 展示，唔好解釋 (Show, Don't Tell)
- **Don't Write**: 「我好傷心」 (explanatory)
- **Do Write**: 「我唔知自己喊咗幾耐，淨係知枕頭濕咗一大撻，凍冰冰咁黐住塊面」 (showing through details)

#### 4. 黃金風格範例 (Golden Style Example)
**Template to Follow Exactly**:
"原來發現一個人呃你，個心係會『咯』一聲，然後靜晒。我同佢，23歲同24歲，喺人哋眼中襯到絕。我仲 on99 咁 plan 緊下個月去邊度 staycation，佢就靜雞雞同第二個女仔 plan 緊點樣唔俾我發現。我噚日問佢，佢冇出聲，淨係望住地下，個樣好似一個做錯事嘅細路。我冇打佢，亦都冇鬧，我淨係覺得好好笑。我哋三年嘅感情，原來就係一場咁好笑嘅笑話。"

#### 5. 文筆風格規則 (Writing Style Rules)
- ✅ **瘋狂加入生活細節同英文**: 大學 last year、check 佢電話、IG story、staycation、Muji 買嘅情侶杯
- ✅ **破碎化思考**: 句子可以短啲，諗法可以跳躍
- ✅ **對白同內心戲要真實**: 用返香港人平時講嘢嘅語氣

#### 6. 禁止事項 (Forbidden Actions)
- ❌ **絕對禁止偏離【故事概念】**
- ❌ **禁止任何總結性、解釋性嘅句子** (e.g., 我好無奈)
- ❌ **禁止任何唔自然嘅文藝腔** (e.g., 低迴)

### 🎯 Why story_ideas.txt Works Better:
1. **天條第一誡** - Unbreakable rule ensures 100% story concept adherence
2. **詳細角色設定** - Specific character and mental state for consistency
3. **具體風格範例** - Exact template to follow for authentic voice
4. **嚴格禁止清單** - Clear boundaries prevent AI from going off-track
5. **香港本土化** - Authentic Cantonese with natural English mixing

This template from `story_ideas.txt` ensures the AI generates authentic Hong Kong relationship content that perfectly follows your story concept while maintaining the exact style and voice you want. 