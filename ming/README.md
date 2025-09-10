# 🎭 Relationship Content Generator

A sophisticated AI-powered system that generates relationship story content for social media platforms like Dcard, with automatic perspective detection and dynamic visual generation.

## 📋 Overview

This system automatically creates engaging relationship stories from simple text inputs, generating:
- **Compelling titles** with keyword highlighting
- **Multi-part story content** with emotional depth
- **Thoughtful conclusions** that encourage discussion
- **Instagram captions** with hashtags
- **Beautiful image sets** with perspective-appropriate backgrounds
- **Telegram auto-posting** for immediate sharing

## 🆕 New: story_ideas.txt 天條第一誡 (The Unbreakable Command)

We now follow the **story_ideas.txt** template with the **天條第一誡** (The Unbreakable Command) - ensuring 100% adherence to your story concept:

### 🎯 天條第一誡 Structure:
1. **❗ 天條第一誡** - 100% absolute adherence to your story concept
2. **角色扮演指令** - 23-year-old female, 3 AM, fragmented thoughts
3. **展示，唔好解釋** - Show, don't tell principle with examples
4. **風格學習** - Follow the golden style example exactly
5. **禁止事項** - Strict rules about what not to do

### ✅ Key Features:
- **絕對服從** - 100% follow your story concept, no additions, no changes
- **角色扮演** - 23-year-old female at 3 AM with confused thoughts
- **展示唔好解釋** - Show emotions through details, not explanations
- **香港口語** - Natural Cantonese with English mixed in (final year, check 電話, IG story)
- **黃金風格範例** - Follow the exact style template provided
- **嚴格禁止** - Clear rules about what AI cannot do

### 🌍 Regional Support & Mock Mode:
- **OpenAI API Available**: Full AI-powered story generation
- **OpenAI API Restricted**: Automatic fallback to Mock/Demo mode
- **Mock Mode Features**: Pre-written authentic Hong Kong style stories that match your story concept
- **Seamless Experience**: System automatically detects API availability and switches modes
- **📖 Detailed Guide**: See [REGIONAL_SUPPORT.md](REGIONAL_SUPPORT.md) for complete documentation

### 🚀 Usage:

#### Command Line:
```bash
# Use simple generator with default story
python relationship_main.py simple

# Use with custom story concept
python relationship_main.py simple "Your story concept here..."

# Test with story_ideas.txt template
python test_simple_generator.py

# Test with specific story concept
python test_simple_with_story_concept.py

# Test Mock mode specifically
python test_mock_mode.py
```

#### Interactive Mode:
```bash
python relationship_main.py
# Then choose option 3 for story_ideas.txt 天條第一誡
```

### 📋 JSON Output Format:
```json
{
  "標題": "[6-12字標題，要吸引人]",
  "內容": "[完整故事，跟足黃金風格範例，150-200字]",
  "結論": "[簡短問句，問大家意見，6-10字]",
  "原始概念": "Your original story concept",
  "生成方法": "story_ideas.txt 天條第一誡"
}
```

### 🛡️ Mock Mode (For Restricted Regions):
```json
{
  "標題": "[Authentic Hong Kong style title]",
  "內容": "[Pre-written story following story_ideas.txt template]",
  "結論": "[Natural conclusion question]",
  "原始概念": "Your original story concept",
  "生成方法": "Mock/Demo Mode (OpenAI API 不可用)",
  "說明": "這是示範模式的回應，因為 OpenAI API 在您的地區不可用",
  "建議": "如需使用真實 AI 生成，請嘗試使用 VPN 或其他 AI 服務"
}
```

## 📝 NEW: 自定義故事圖片生成 (Custom Story Image Generation)

We now support **自定義故事內容生成** (Custom Story Content Generation) where you can use your own story content without any modifications!

### 🎯 Feature Overview:
- ✅ **原文不變** - Uses your exact text without any modifications
- ✅ **自動分割** - Intelligently splits your story into title, content, and conclusion
- ✅ **專業圖片** - Generates 6 professional images from your content
- ✅ **Telegram 發送** - Automatically uploads to your Telegram

### 🚀 How to Use:

#### Step 1: Edit Your Story File
Edit `my_custom_story.txt`:
```
你嘅標題（第一行）

你嘅主要內容
可以分幾段來寫
每段之間用空行分開

你嘅結尾問句（最後一行）
```

#### Step 2: Run the System
```bash
python relationship_main.py
# Choose option 6: 自定義故事圖片生成
```

#### Step 3: Generated Output
- 📰 **Title Image**: Uses your title
- 📄 **Content Images**: 3 images with your content automatically split
- ❓ **Conclusion Image**: Your ending question
- 🎨 **End Image**: Standard closing image

### 📁 Generated Files:
```
title.png              # Your title
content_page1.png       # First part of your content
content_page2.png       # Second part of your content  
content_page3.png       # Third part of your content
conclusion.png          # Your conclusion
end.png                # Standard ending
```

### 🧪 Testing:
```bash
python test_custom_story.py
```

### 📖 Complete Guide:
See [CUSTOM_STORY_GUIDE.md](CUSTOM_STORY_GUIDE.md) for detailed instructions and examples.

## 🏗️ System Architecture

### Core Files Structure

```
├── story_ideas.txt                    # Input stories with perspective markers
├── my_custom_story.txt                # NEW: Custom story input file
├── relationship_main.py               # Main execution orchestrator
├── relationship_content_generator.py  # AI content generation engine
├── simple_story_generator.py         # NEW: Super simple story generator
├── custom_story_reader.py            # NEW: Custom story reader and processor
├── test_simple_generator.py          # NEW: Simple generator testing script
├── test_custom_story.py              # NEW: Custom story testing script
├── relationship_template_generator.py # HTML template creator
├── image_generator.py                # PNG image generator
├── telegram_sender.py                # Telegram posting automation
├── config.py                         # Environment setup
├── CUSTOM_STORY_GUIDE.md             # NEW: Complete custom story guide
└── generated_ig_caption.txt          # Output Instagram caption
```

### Generated Output Files

```
├── title.png           # Main title slide
├── content_page1.png   # Story part 1
├── content_page2.png   # Story part 2
├── content_page3.png   # Story part 3
├── conclusion.png      # Conclusion slide
├── end.png            # Ending slide
└── generated_simple_content.json     # NEW: Simple generator output
```

## 🎯 Complete Workflow

### 1. Story Input & Perspective Detection

**Input**: `story_ideas.txt`
```
# 感情故事概念 - 女性第一人稱視角
我沉迷社交媒體，日日都要影相打卡...

# 感情故事概念 - 男性第一人稱視角  
我女朋友網購成癮，每日都要買嘢...
```

**Detection Logic**:
- System scans for perspective markers in comments
- `女性第一人稱視角` → Sets perspective to "female"
- `男性第一人稱視角` → Sets perspective to "male"
- Stories inherit the perspective from their section

### 2. AI Content Generation Pipeline

#### Traditional Method:

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

## 🛠️ Setup and Configuration

### Prerequisites
```bash
pip install openai python-dotenv imgkit asyncio pathlib requests
```

### Environment Variables
```bash
OPENAI_API_KEY=your_openai_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

### System Dependencies
- **wkhtmltoimage**: For HTML to PNG conversion
- **Font Files**: Chinese font support required

## 🚀 Usage Examples

### Quick Start (Simple Mode)
```bash
# Interactive mode with menu
python relationship_main.py

# Direct simple generator usage
python relationship_main.py simple "我男朋友成日打機..."

# Test with story_ideas.txt template
python test_simple_generator.py

# Test with specific story concept
python test_simple_with_story_concept.py
```

### Traditional Full Generation
```bash
# Complete pipeline with images
python relationship_main.py

# Short content only
python relationship_main.py short

# Performance analysis
python relationship_main.py report
```

### Advanced Usage
```bash
# Interactive testing
python test_simple_generator.py interactive

# Batch testing with examples
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