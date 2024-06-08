addimport re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "27497317"))
API_HASH = getenv("API_HASH", "912dc329039f9fcf92b6ace0efb35cef")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7221149690:AAGspc1Dw2mnrVqJg1on6bQJPU2IzO5aq00", None)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://OrboroBot:OrboroBot@cluster0.tvxqfcx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002207392342", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6484740378"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("orborobot")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-2c5ef219-3ac7-4908-b6cf-d2b12e44bf8f")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/chestchannel")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/OrboroBotSupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQGjk2UALpvTOlUtMQIo-J586DOK8aveUVKgvrDoza8YwezMXQeZpcO7IgsEtAbugDKbWIia-8cTPWnU7T3IdQcu9XbkB1xvp9Wmw3ctIKhStcWqSlSAUUTM1225zCSXU7knetF1yW67QroGpfK_rgXj35TYThB_REFqeXEiaVZ9r6LGwUBF8EJu9iM0GrnrEYVvCqb3wCr5vSa-8fPlafCOjtmpbFEfnDU1YQ-d52bLkENsiw6UzvzHUZUCkB0fl8kqzg3AueK8l3R08Y5v8pJIlah6EUzY3t3XjFGBXo77QHC_1gyPsrwNBv4gIPWjQob8ksRQFStnBCA1MF53BRm9VQT_GwAAAAGChUkaAA", None)
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
    "START_IMG_URL", "https://graph.org/file/1933127a986436b9f970c.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
STATS_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
STREAM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"


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
