# 📖 How to Use Custom Story Generation

## 🎯 Quick Start

### Step 1: Edit Your Story
Edit the file: **`my_custom_story.txt`** (in root directory)

Your story format:
```
標題（第一行）

內容段落1

內容段落2

內容段落3

結尾問句（最後一行）
```

### Step 2: Run the Generator
```bash
cd ming
python run_custom_story.py
```

That's it! The system will:
- ✅ Auto-detect your story's perspective (男/女)
- ✅ Generate beautiful images (6-9 pages)
- ✅ Send to Telegram automatically
- ✅ Save IG-optimized caption

## 🎭 Perspective Detection

The system **automatically** detects if your story is from:
- 👩‍💼 **Girl View**: If you mention "男朋友", "老公", "我男朋友"
- 👨‍💼 **Boy View**: If you mention "女朋友", "老婆", "我女朋友"

### Your Current Story:
✅ **Girl View** - You mentioned "男朋友" in your story

## 📁 File Locations

The script searches for your story in:
1. **Root directory**: `C:\Users\user\Desktop\ming\my_custom_story.txt` ← **Your file**
2. **Ming subdirectory**: `C:\Users\user\Desktop\ming\ming\my_custom_story.txt`

It will use whichever it finds first.

## 🧪 Test Perspective Detection

To verify your story's perspective:
```bash
cd ming
python test_perspective_detection.py
```

You should see:
```
✅ 結論: 這是一個 👩‍💼 女性視角 (Girl View) 的故事
```

## 🎨 Generated Output

After running, you'll get:
1. **Images**: `title.png`, `story1.png`, ..., `conclusion.png`, `end.png`
2. **IG Caption**: `generated_ig_caption.txt`
3. **Telegram**: Auto-posted to your channel

## ⚙️ Advanced: Force a Specific Perspective

If auto-detection is wrong, add to **top** of your story file:

**For Girl View:**
```
# 女性視角
準備結婚，男朋友話連「禮金」都要同我AA制...
```

**For Boy View:**
```
# 男性視角
準備結婚，女朋友話唔要禮金...
```

## 🎯 Alternative: Interactive Mode

```bash
cd ming
python relationship_main.py
```

Then choose:
- **Option 6**: 自定義故事圖片生成

This includes full IG optimization features:
- 📊 Content performance score
- ⏰ Best posting time
- 🏷️ Hashtag strategy
- 📅 Weekly posting schedule

## 📊 What's Different Between Scripts?

| Feature | `run_custom_story.py` | `relationship_main.py` (Option 6) |
|---------|----------------------|-----------------------------------|
| Read your story | ✅ | ✅ |
| Generate images | ✅ | ✅ |
| Auto-detect perspective | ✅ | ✅ |
| Send to Telegram | ✅ | ✅ |
| IG optimization | ❌ | ✅ (Full suite) |
| Speed | ⚡ Fast | Slower (more features) |

## 🔧 Troubleshooting

### "找唔到 my_custom_story.txt 檔案"
**Solution**: Make sure file exists at:
- `C:\Users\user\Desktop\ming\my_custom_story.txt` (root)
- OR `C:\Users\user\Desktop\ming\ming\my_custom_story.txt`

### "Wrong perspective detected"
**Solution**: Add manual override at top of file:
```
# 女性視角
```

### "Images not generating"
**Solution**: Check if you have required packages:
```bash
pip install -r requirements.txt
```

## 💡 Pro Tips

1. **Keep paragraphs short**: Each paragraph becomes part of an image
2. **Clear title**: First line should be catchy and clear
3. **Question ending**: End with a question to boost engagement
4. **Keywords matter**: Mention "男朋友"/"女朋友" clearly for correct detection

## 📝 Example Story Structure

```txt
準備結婚，男朋友話連「禮金」都要同我AA制，叫我夾錢娶我自己？

我同男朋友一齊四年，平時拍拖AA制，我都接受。

最近我哋決定結婚，開始plan婚禮。佢話佢負責整budget，叫我放心。

尋晚，佢send咗個Excel file俾我，入面每一項開支都係「Total / 2」。

即係全部除二，一人一半。

你哋有冇聽過禮金都要AA制？定係我太古板？
```

## ✅ Ready to Go!

Your story is ready! Just run:
```bash
cd ming
python run_custom_story.py
```

The system now **correctly identifies** your story as **Girl View** and will use the appropriate template! 🎉

