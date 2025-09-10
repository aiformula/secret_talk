import os
from telegram import InputMediaPhoto

async def send_telegram_photos(telegram_bot, telegram_chat_id, photo_paths: list, caption: str = None):
    """Send multiple photos to Telegram with a single caption."""
    try:
        # Check if all files exist
        for path in photo_paths:
            if not os.path.exists(path):
                print(f"File not found: {path}")
                return

        # Create media group
        media = []
        for path in photo_paths:
            with open(path, 'rb') as photo:
                media.append(InputMediaPhoto(photo))

        # Send the media group
        await telegram_bot.send_media_group(
            chat_id=telegram_chat_id,
            media=media,
            caption=caption
        )
        print(f"Photos sent successfully with caption: {caption}")
    except Exception as e:
        print(f"Error sending photos: {str(e)}")
        # Print more detailed error information
        import traceback
        print("Full error details:")
        print(traceback.format_exc()) 