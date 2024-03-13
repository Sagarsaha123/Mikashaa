import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","28301929")) # Get this value from my.telegram.org/apps
API_HASH = getenv("API_HASH","f77634e3747f7431584a82c29afba85c") # Get this value from my.telegram.org/apps
BOT_TOKEN = getenv("BOT_TOKEN","6452346857:AAGsuCka_fFQlansNpiJyj3uRKQ2RF6SfLk")
BOT_USERNAME = getenv("BOT_USERNAME","MikaShaaAIBot")
USERNAME = getenv("USERNAME","MikaShaaAIBot")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://MikashaaAi:LvJ8T7z3IAtYZsCj@mikashaaai.ljsm4zo.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001998469453"))
AM_SUPPORT = int(getenv("NeoMusicSupport", "-1002067385481"))
OWNER_ID = int(getenv("OWNER_ID", "6809585463"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME","Mikashaa AI")
ASSUSERNAME = getenv("ASSUSERNAME" , "Mikashaa_Ai")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME",None)
DEEP_API = getenv("DEEP_API","c8e3d7fc-1f7e-455b-8019-5c1b7f21047a")
OPENAI_KEY = getenv("OPENAI_KEY",None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY",None)
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/Sagarsaha123/Mikashaa",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
AM_CHAT = getenv("AM_CHAT","https://t.me/NeoMusicSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+iGreVgrKv003OWI1")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
AUTO_GCAST = getenv("AUTO_GCAST","True")
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION",  None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/10732f260cbbd4a65bfce.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/10732f260cbbd4a65bfce.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
STATS_IMG_URL = "https://telegra.ph/file/10732f260cbbd4a65bfce.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/48f39202823b358203234.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/4eee6d4a7a1de179ff26d.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
