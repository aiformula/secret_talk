# 📱 Telegram 設置指南

## 🚨 問題：選擇選項 6 時無法發送到 Telegram

如果你見到呢個訊息：
```
⚠️ 跳過 Telegram 發送（環境變量未設置）
```

呢個係因為缺少 `.env` 配置檔案。

## 🛠️ 解決方法

### 第一步：創建 .env 檔案

喺 `ming` 目錄入面創建一個叫 `.env` 嘅檔案，內容如下：

```
# Telegram Configuration
TELEGRAM_BOT_TOKEN=你嘅_telegram_bot_token
TELEGRAM_CHAT_ID=你嘅_telegram_chat_id

# OpenAI Configuration  
OPENAI_API_KEY=你嘅_openai_api_key

# Notion Configuration (Optional)
NOTION_TOKEN=你嘅_notion_token
NOTION_PAGE_ID=你嘅_notion_page_id
```

### 第二步：獲取 Telegram Bot Token

1. 喺 Telegram 搵 `@BotFather`
2. 發送 `/newbot` 命令
3. 跟住指示創建你嘅 bot
4. 複製返嚟嘅 token

### 第三步：獲取 Chat ID

1. 將你嘅 bot 加入你想發送訊息嘅群組或頻道
2. 發送一條訊息俾你嘅 bot
3. 訪問：`https://api.telegram.org/bot你嘅_BOT_TOKEN/getUpdates`
4. 搵 `chat` -> `id` 數值

### 第四步：獲取 OpenAI API Key

1. 訪問 https://platform.openai.com/api-keys
2. 登入你嘅 OpenAI 帳戶
3. 創建新嘅 API key
4. 複製 key

### 第五步：測試

運行程式並選擇選項 6，而家應該可以成功發送到 Telegram！

## 🔒 安全提示

- **絕對唔好**將 `.env` 檔案上傳到 GitHub
- 呢個檔案已經被 `.gitignore` 保護
- 如果意外上傳咗，立即重新生成所有 API keys

## 🆘 常見問題

### Q: 我唔想用 Telegram，可以跳過嗎？
A: 可以！程式會自動跳過 Telegram 發送，只生成圖片。

### Q: 我只想測試，唔想設置咁多嘢？
A: 你可以只設置 `OPENAI_API_KEY`，其他可以暫時留空。

### Q: 點樣知道我嘅設置係咪正確？
A: 運行程式時會顯示環境變數檢查結果。
