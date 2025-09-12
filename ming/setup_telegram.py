#!/usr/bin/env python3
"""
📱 Telegram 設置助手
幫助用戶創建 .env 檔案並配置 Telegram 發送功能
"""

import os

def create_env_file():
    """創建 .env 檔案"""
    print("🚀 Telegram 設置助手")
    print("=" * 50)
    
    env_path = ".env"
    
    # 檢查是否已存在 .env 檔案
    if os.path.exists(env_path):
        print(f"⚠️ {env_path} 檔案已存在")
        overwrite = input("是否要覆蓋現有檔案？(y/N): ").strip().lower()
        if overwrite != 'y':
            print("❌ 取消操作")
            return
    
    print("\n📝 請提供以下資訊：")
    print("💡 如果暫時沒有某個值，可以留空，之後再填")
    
    # 收集用戶輸入
    telegram_bot_token = input("\n🤖 Telegram Bot Token: ").strip()
    telegram_chat_id = input("💬 Telegram Chat ID: ").strip()
    openai_api_key = input("🧠 OpenAI API Key: ").strip()
    notion_token = input("📝 Notion Token (可選): ").strip()
    notion_page_id = input("📄 Notion Page ID (可選): ").strip()
    
    # 創建 .env 內容
    env_content = f"""# Telegram Configuration
TELEGRAM_BOT_TOKEN={telegram_bot_token}
TELEGRAM_CHAT_ID={telegram_chat_id}

# OpenAI Configuration
OPENAI_API_KEY={openai_api_key}

# Notion Configuration (Optional)
NOTION_TOKEN={notion_token}
NOTION_PAGE_ID={notion_page_id}

# 📝 設置說明：
# 1. Telegram Bot Token: 從 @BotFather 獲取
# 2. Chat ID: 你想發送訊息嘅群組或頻道 ID
# 3. OpenAI API Key: 從 https://platform.openai.com/api-keys 獲取
# 4. Notion 設置係可選嘅，用於進階功能
"""
    
    # 寫入檔案
    try:
        with open(env_path, 'w', encoding='utf-8') as f:
            f.write(env_content)
        print(f"\n✅ 成功創建 {env_path} 檔案！")
        
        # 檢查必要設置
        missing = []
        if not telegram_bot_token:
            missing.append("Telegram Bot Token")
        if not telegram_chat_id:
            missing.append("Telegram Chat ID")
        if not openai_api_key:
            missing.append("OpenAI API Key")
        
        if missing:
            print(f"\n⚠️ 以下設置仍然缺少：")
            for item in missing:
                print(f"  - {item}")
            print(f"💡 請編輯 {env_path} 檔案並填入缺少嘅值")
        else:
            print("\n🎉 所有必要設置都已完成！")
            print("🚀 而家可以運行 python relationship_main.py 並選擇選項 6")
        
    except Exception as e:
        print(f"❌ 創建檔案時出錯：{e}")

def show_help():
    """顯示幫助資訊"""
    print("""
📚 獲取 API Keys 嘅方法：

🤖 Telegram Bot Token:
1. 喺 Telegram 搵 @BotFather
2. 發送 /newbot
3. 跟住指示創建 bot
4. 複製返嚟嘅 token

💬 Telegram Chat ID:
1. 將你嘅 bot 加入群組/頻道
2. 發送一條訊息
3. 訪問：https://api.telegram.org/bot你嘅_TOKEN/getUpdates
4. 搵 "chat" -> "id" 數值

🧠 OpenAI API Key:
1. 訪問 https://platform.openai.com/api-keys
2. 登入並創建新 key
3. 複製 key

📝 Notion (可選):
1. 訪問 https://www.notion.so/my-integrations
2. 創建新 integration
3. 複製 token 同 page ID
""")

if __name__ == "__main__":
    print("選擇操作：")
    print("1. 創建 .env 檔案")
    print("2. 顯示幫助資訊")
    
    choice = input("請選擇 (1-2): ").strip()
    
    if choice == "1":
        create_env_file()
    elif choice == "2":
        show_help()
    else:
        print("❌ 無效選擇")
