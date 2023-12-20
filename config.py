import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","28687973"))
API_HASH = getenv("API_HASH","c377969d25dcee0a496a9c937897591d")
BOT_TOKEN = getenv("BOT_TOKEN","6452346857:AAFWxE4vTKNVrlhBEvtWR4VmgvdVDgNYBb0")
BOT_USERNAME = getenv("BOT_USERNAME","MikaShaaAIBot")
USERNAME = getenv("USERNAME","MikaShaaAIBot")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://MikashaaAi:LvJ8T7z3IAtYZsCj@mikashaaai.ljsm4zo.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002078194217"))
OWNER_ID = int(getenv("OWNER_ID", "5360305806"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME","Mikashaa AI")
ASSUSERNAME = getenv("ASSUSERNAME" , "Mikashaa_Ai")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","mikasaakk")
DEEP_API = getenv("DEEP_API","c8e3d7fc-1f7e-455b-8019-5c1b7f21047a")
OPENAI_KEY = getenv("OPENAI_KEY",None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY","601f56a4-dac8-4f9e-96af-8996ddfff3e2")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/AbhiMod/Mikashaa_AI",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
AM_CHAT = getenv("AM_CHAT","https://t.me/AM_YTSUPPORT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+iGreVgrKv003OWI1")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "True"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", "BQAcaInFhmK-s4_YPmyyNLFzRIqjKJwa6WYARqdCh82ukvI7deO81ae77RDEWD6fRlH3JSeV7s5UVWaJe5O2p7P0crz92eQykKzdnhD6R3xdXXKdRDtG3n351xz2emE8gYANoXLjJP3ivgX7TVgFNysnNEpKmC7Gu7Wwql4AlZOSnjKXw9d9cqdMsfz9S98QP_52_apeFIf43g-KYysT9tc-4-CqVUMZcLX3tBPTsgOXNBy2jYdO2XeBiyQvtRO_I1KMxr-HouIMXzsGPPce3ZrVhz2GrqCWoXLpYkvbaOk5zyS72QcLId0Vv-D5wFfpP68bc4XV1ugpAPZ_BUYPKK1XAAAAAY7DHMkA")
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
