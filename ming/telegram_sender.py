import os
from telegram import InputMediaPhoto

def check_file_sizes(photo_paths):
    """檢查圖片檔案大小"""
    total_size = 0
    print("📊 檔案大小檢查:")
    for path in photo_paths:
        if os.path.exists(path):
            size = os.path.getsize(path)
            total_size += size
            size_mb = size / (1024 * 1024)
            print(f"  📄 {os.path.basename(path)}: {size_mb:.2f} MB")
        else:
            print(f"  ❌ {os.path.basename(path)}: 檔案不存在")
    
    total_mb = total_size / (1024 * 1024)
    print(f"  📦 總大小: {total_mb:.2f} MB")
    
    if total_mb > 50:
        print("  ⚠️  檔案太大，可能會導致 timeout")
    elif total_mb > 20:
        print("  ⚠️  檔案偏大，上傳可能較慢")
    else:
        print("  ✅ 檔案大小正常")
    
    return total_mb

async def send_telegram_photos(telegram_bot, telegram_chat_id, photo_paths: list, caption: str = None):
    """Send multiple photos to Telegram with a single caption."""
    try:
        # Check if all files exist
        for path in photo_paths:
            if not os.path.exists(path):
                print(f"❌ File not found: {path}")
                return False

        print(f"📤 開始上傳 {len(photo_paths)} 張圖片到 Telegram...")
        
        # Check file sizes first
        total_size = check_file_sizes(photo_paths)
        
        # Create media group
        media = []
        for i, path in enumerate(photo_paths):
            print(f"📄 準備圖片 {i+1}/{len(photo_paths)}: {os.path.basename(path)}")
            with open(path, 'rb') as photo:
                media.append(InputMediaPhoto(photo))

        # Send the media group with timeout settings
        print("🚀 發送中...")
        
        # Adjust timeout based on file size
        if total_size > 50:
            read_timeout = 120
            write_timeout = 120
        elif total_size > 20:
            read_timeout = 90
            write_timeout = 90
        else:
            read_timeout = 60
            write_timeout = 60
            
        print(f"⏱️  設定超時時間: {read_timeout} 秒 (基於檔案大小 {total_size:.1f}MB)")
        
        result = await telegram_bot.send_media_group(
            chat_id=telegram_chat_id,
            media=media,
            caption=caption,
            read_timeout=read_timeout,
            write_timeout=write_timeout,
            connect_timeout=30
        )
        print(f"✅ 成功發送 {len(photo_paths)} 張圖片到 Telegram！")
        return True
        
    except Exception as e:
        print(f"❌ Telegram 發送失敗: {str(e)}")
        
        # 針對不同錯誤類型提供建議
        if "TimedOut" in str(e):
            print("💡 建議：")
            print("  - 檢查網路連線")
            print("  - 圖片檔案可能太大，嘗試壓縮")
            print("  - 稍後再試")
        elif "Flood" in str(e):
            print("💡 建議：發送太頻繁，請等待幾分鐘後再試")
        elif "File too large" in str(e):
            print("💡 建議：圖片檔案太大，需要壓縮")
        
        # Print detailed error for debugging
        import traceback
        print("🔍 詳細錯誤資訊:")
        print(traceback.format_exc())
        return False