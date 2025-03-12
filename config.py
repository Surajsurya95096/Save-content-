# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7406982863").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://vishwajitkr642006:BEPMAOkwnBCBxeHd@cluster0.c97un.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "7406982863")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002389409901"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "techvjlink.site")
AD_API = getenv("AD_API", "05623a202a2572b680fa2c04fcdb07bb67cdb55d")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
