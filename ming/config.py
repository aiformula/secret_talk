import os
from openai import AsyncOpenAI
from notion_client import Client
from telegram import Bot
from dotenv import load_dotenv

def setup_environment():
    """Setup and validate all environment variables and return initialized clients"""
    
    print("\n=== Environment Variables Debug ===")
    print("Current working directory:", os.getcwd())

    # Get the absolute path to the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(current_dir, '.env')
    print(f"Looking for .env file at: {env_path}")

    # Clear ALL environment variables related to our app
    for key in list(os.environ.keys()):
        if key in ['TELEGRAM_BOT_TOKEN', 'TELEGRAM_CHAT_ID', 'OPENAI_API_KEY', 'NOTION_TOKEN']:
            print(f"Clearing environment variable: {key}")
            del os.environ[key]

    if os.path.exists(env_path):
        print("Found .env file, loading variables...")
        # Print the raw contents of the .env file for debugging
        print("\nContents of .env file:")
        with open(env_path, 'r') as f:
            env_contents = f.read()
            print(env_contents)
        
        # Parse the .env file manually first
        env_vars = {}
        for line in env_contents.split('\n'):
            if '=' in line and not line.startswith('#'):
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                env_vars[key] = value
                print(f"Found in .env: {key}={value}")
        
        # Force reload with override
        load_dotenv(env_path, override=True, verbose=True)
        
        # Double check the values
        print("\nEnvironment variables after loading:")
        for key in ['TELEGRAM_BOT_TOKEN', 'TELEGRAM_CHAT_ID', 'OPENAI_API_KEY', 'NOTION_TOKEN']:
            env_value = os.getenv(key)
            file_value = env_vars.get(key)
            print(f"{key}:")
            print(f"  - From .env file: {file_value}")
            print(f"  - From environment: {env_value}")
            if env_value != file_value:
                print(f"  - WARNING: Values don't match!")
                # Force set the value from the file
                os.environ[key] = file_value
                print(f"  - Forced update to: {file_value}")
    else:
        print(f"No .env file found at {env_path}!")
        raise FileNotFoundError(f".env file not found at {env_path}")

    # Get the final values
    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    notion_token = os.getenv("NOTION_TOKEN")
    notion_page_id = os.getenv("NOTION_PAGE_ID")

    print("\nFinal environment variables:")
    print(f"TELEGRAM_BOT_TOKEN: {telegram_bot_token}")
    print(f"TELEGRAM_CHAT_ID: {telegram_chat_id}")
    print(f"OPENAI_API_KEY: {'Found' if openai_api_key else 'Not found'}")
    print(f"NOTION_TOKEN: {'Found' if notion_token else 'Not found'}")
    print(f"NOTION_PAGE_ID: {notion_page_id}")

    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    if not notion_token:
        raise ValueError("NOTION_TOKEN not found in .env file")
    if not telegram_bot_token:
        raise ValueError("TELEGRAM_BOT_TOKEN not found in .env file")
    if not telegram_chat_id:
        raise ValueError("TELEGRAM_CHAT_ID not found in .env file")
    if not notion_page_id:
        raise ValueError("NOTION_PAGE_ID not found in .env file")

    # Initialize clients with the final values
    notion = Client(auth=notion_token)
    openai_client = AsyncOpenAI(api_key=openai_api_key)
    telegram_bot = Bot(token=telegram_bot_token)

    print("\nClients initialized with new values!")
    print(f"Using Telegram Chat ID: {telegram_chat_id}")

    return {
        'notion': notion,
        'openai_client': openai_client,
        'telegram_bot': telegram_bot,
        'telegram_chat_id': telegram_chat_id,
        'notion_page_id': notion_page_id
    }

# Constants
PEOPLE = ["brian", "kin", "tim", "david"]
STATE_FILE = "current_person.txt"
GITHUB_BASE = "https://raw.githubusercontent.com/Liuhangfung/marketing_automation/main/" 