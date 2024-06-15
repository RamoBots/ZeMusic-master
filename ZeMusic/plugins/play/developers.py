import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["رامو","المبرمج رامو","مطور السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/f9d90e1ae27f9b53cc59c.mp4",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𐇮 𝑹𝑨𝑴𝑶 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮](https://t.me/C_lxl_C)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @C_lxl_C ❫
◉ 𝙸𝙳      : ❪ `6236388211` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@VIP_ALBEAR) my world (@R_surce - @UY_FU) my bro (@Myself) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𐇮 𝑹𝑨𝑴𝑶 𖠮🚸𖠮 آلـۘهہؚيـٰـ‌ُـُ໋۠بـ໋ۘ۠ه 𐇮", url=f"https://t.me/C_lxl_C"), 
                 ],[
                   InlineKeyboardButton(
                        "🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝑹𝑨𝑴𝑶 🔱", url=f"https://t.me/R_surce"),
                ],

            ]

        ),

    )
