# Created By @Its_romeoo
# Copyright By M8N

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSUSERNAME = getenv("ASSUSERNAME")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/UnknownMortal/M8N-Music-Bot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "872919-98282-99292")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "hsbsi")
MONGO_DB_URI = getenv("MONGO_DB_URI")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
UPDATE = getenv("UPDATE", "M8N_OFFICIAL")
SUPPORT = getenv("SUPPORT", "M8N_SUPPORT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/b71c329d2c24f6bc46525.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5058236569").split()))
START_PIC = getenv("START_PIC")
OWNER_USERNAME = getenv("OWNER_USERNAME")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/3b663a7e9a414304c084f.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
