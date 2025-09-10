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

## 🏗️ System Architecture

### Core Files Structure

```
├── story_ideas.txt                    # Input stories with perspective markers
├── relationship_main.py               # Main execution orchestrator
├── relationship_content_generator.py  # AI content generation engine
├── relationship_template_generator.py # HTML template creator
├── image_generator.py                # PNG image generator
├── telegram_sender.py                # Telegram posting automation
├── config.py                         # Environment setup
└── generated_ig_caption.txt          # Output Instagram caption
```

### Generated Output Files

```
├── title.png           # Main title slide
├── content_page1.png   # Story part 1
├── content_page2.png   # Story part 2
├── content_page3.png   # Story part 3
├── conclusion.png      # Conclusion slide
└── end.png            # Ending slide
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

#### Phase 1: Title Generation
```python
generate_relationship_title_content()
```
- **Input**: Raw story text + perspective
- **AI Prompt**: Dynamically adapts based on perspective
  - Female: "用第一人稱角度（女性視角），如「我...」、「我應該點做」"
  - Male: "用第一人稱角度（男性視角），如「我女朋友...」、「佢...」"
- **Output**: Title + highlighted keywords
- **Special Feature**: Comma formatting (title with "，" splits into multiple lines)

#### Phase 2: Story Content Generation
```python
generate_relationship_story_content()
```
- **Input**: Base story + perspective
- **Process**: Extracts 3 dramatic story points with detailed descriptions (300-400 words each)
- **AI Adaptation**: 
  - Female perspective: Self-focused narrative
  - Male perspective: Girlfriend-focused narrative
- **Output**: Hook + 3 story points + keywords

#### Phase 3: Conclusion Generation
```python
generate_relationship_conclusion_content()
```
- **Input**: Story points summary
- **Purpose**: Creates reflective questions that invite discussion
- **Output**: Empathetic conclusion tailored to perspective

#### Phase 4: Instagram Caption
```python
generate_instagram_caption()
```
- **Input**: Complete story content
- **Output**: ~290 word caption with 15-20 hashtags in pure Cantonese

### 3. Visual Template Generation

#### Template Creation
```python
relationship_template_generator.py
```

**Perspective-Based Background Selection**:
- **Female Perspective**: `title_girl.png`, `content_page1_girl.png`, etc.
- **Male Perspective**: `title_boy.png`, `content_page1_boy.png`, etc.

**Template Types**:
1. **Title Template**: Large title with comma line breaks + "感情煩惱分享"
2. **Story Templates** (3x): Individual story points with highlighted keywords
3. **Conclusion Template**: Reflective question + call-to-action
4. **End Template**: Clean ending slide

#### Dynamic Features
- **Keyword Highlighting**: Important emotional words highlighted in red
- **Responsive Design**: Optimized for 1080x1350 social media format
- **Font Integration**: Noto Sans TC for proper Chinese character display

### 4. Image Generation Pipeline

#### PNG Creation Process
```python
image_generator.py
```

**Technical Process**:
1. **Browser Automation**: Uses Playwright to render HTML templates
2. **High Resolution**: 2x device scale factor for crisp images
3. **Element Capture**: Screenshots specific `#xiaohongshu-post` elements
4. **Clean Naming**: Outputs as `title.png`, `content_page1.png`, etc.

**Error Handling**:
- Debug screenshots for failed renders
- Fallback full-page captures
- Comprehensive error logging

### 5. Distribution & Sharing

#### Telegram Integration
```python
telegram_sender.py
```
- **Auto-posting**: Sends complete image set to configured Telegram channel
- **Caption**: Includes theme, timestamp, and full Instagram caption
- **Format**: Multi-image album for easy sharing

## 🎨 Perspective System Details

### Female Perspective Stories
- **Background Images**: `*_girl.png` series
- **Language Style**: "我覺得...", "我好煩惱...", "我應該點做..."
- **Narrative Focus**: Self-reflection and personal struggles
- **Example**: Social media addiction affecting relationship

### Male Perspective Stories  
- **Background Images**: `*_boy.png` series
- **Language Style**: "我女朋友...", "佢...", "我試過同佢傾..."
- **Narrative Focus**: Girlfriend's behavior and relationship dynamics
- **Example**: Girlfriend's shopping addiction from boyfriend's view

## ⚙️ Configuration & Setup

### Environment Variables
```python
# config.py requirements
OPENAI_API_KEY=your_openai_key
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

### Dependencies
- OpenAI GPT-4 API access
- Playwright for browser automation
- Telegram Bot API
- Python 3.8+ with asyncio support

## 🚀 Usage Instructions

### Basic Usage
```bash
python relationship_main.py
```

### Test Mode (No AI, uses predefined templates)
```bash
python relationship_main.py test
```

### Adding New Stories

1. **Edit `story_ideas.txt`**:
```
# 感情故事概念 - 女性第一人稱視角
我男朋友成日打機，連約會都唔肯放低手機...

# 感情故事概念 - 男性第一人稱視角
我女朋友太完美主義，咩都要criticize...
```

2. **Run the system** - it will automatically:
   - Detect the perspective
   - Generate appropriate content
   - Use correct background images
   - Create all 6 PNG files
   - Post to Telegram

## 🎯 Key Features

### Intelligent Content Adaptation
- **Perspective Detection**: Automatically determines male/female viewpoint
- **Dynamic Prompts**: AI instructions change based on detected perspective
- **Visual Consistency**: Background images match story perspective
- **Language Authenticity**: Pure Cantonese with perspective-appropriate phrases

### Content Quality Assurance
- **Dcard Style**: Authentic social media storytelling format
- **Emotional Depth**: 300-400 word detailed story segments
- **Engagement Focus**: Questions and relatable scenarios
- **Cultural Accuracy**: Hong Kong relationship dynamics and language

### Technical Reliability
- **Error Handling**: Comprehensive fallbacks and debug outputs
- **High Quality**: 2x resolution images for crisp display
- **Clean Organization**: Standardized file naming and structure
- **Automation**: End-to-end pipeline from text to published content

## 📊 Output Examples

### Generated Files Per Run
1. **6 PNG Images**: Complete visual story set
2. **Instagram Caption**: Ready-to-post social media content  
3. **Debug Logs**: Perspective detection and generation status
4. **Telegram Post**: Automatic distribution to audience

### Content Characteristics
- **Title**: 8-15 characters, emotionally engaging
- **Story Points**: 3 detailed sections with natural progression
- **Keywords**: 5-7 highlighted emotional terms
- **Conclusion**: 15-25 character reflective question
- **Caption**: ~290 words with 15-20 relevant hashtags

## 🔧 Technical Architecture

### Asynchronous Processing
- **Concurrent AI Calls**: Multiple content generation in parallel
- **Non-blocking I/O**: Efficient file and network operations
- **Scalable Design**: Easy to extend with additional content types

### Error Recovery
- **Graceful Degradation**: System continues with partial failures
- **Debug Artifacts**: Error screenshots and logs for troubleshooting  
- **Fallback Content**: Default scenarios when story loading fails

This system represents a complete content creation pipeline, from simple text inputs to professionally formatted, culturally authentic relationship stories ready for social media distribution. 