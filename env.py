import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "24401235").strip()
API_HASH = os.getenv("API_HASH", "149f7e13d7d861b27cffc3ab1fd52b22").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "7476307432:AAETfjWyX_8-58DIiuXF-eIL1VaIj_VQepw").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "https://t.me/Puthusa_yosi")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
