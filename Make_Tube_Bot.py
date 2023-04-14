from __future__ import unicode_literals
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import CallbackQuery, Message
import yt_dlp

app = Client("Make_Tube_Bot")


# Hook que imprime un mensaje cuando yt-dlp envia el estado de finished
def my_hook(d):
    if d["status"] == "finished":
        print("Done downloading, now converting ...")


# ydl_opts opciones de descarga
ydl_opts = {
    "format": "bestaudio/worst",
    "outtmpl": "%(id)s",
    "noplaylist": True,
    "progress_hooks": [my_hook],
}

# Código para descargar video previamente definido en una variable o enlace
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([""])

app.run()
