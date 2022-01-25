import os
from pyrogram import Client, filters
from pyrogram.types import *

from LovelyRobot.conf import get_str_key
from LovelyRobot import pbot
 
 # pls don't delete
REPO_TEXT = "**Lovely [BOT](https://telegra.ph/file/526ed899597d7827474a1.jpg) will Make Your Groups Secured And it's have a lot of fun features (:  ! \n\n↼ Owner ⇀ : 『 [𝐋ᴏɢ ✘ Ꭺғᴋ xD](t.me/log_afk) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @UNIQUE_SOCIETY «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("ʀᴇᴘᴏꜱɪᴛᴏʀʏ", url=f"https://github.com/TEAM-BLAZ/BLAZE-SPAMMER-ROBOT"),
        InlineKeyboardButton("Gɪᴛʜᴜʙ", url=f"https://t.me/LOG_AFK"),
      ],[
        InlineKeyboardButton("Oᴡɴᴇʀ ❣️", url="https://t.me/Evil_xD_boy"),
        InlineKeyboardButton("Oᴡɴᴇʀ ❣️", url="https://t.me/Unknown_Shadow_xD"),
       InlineKeyboardButton("Oᴡɴᴇʀ ❣️", url="https://t.me/its_jack"),
      ],[
        InlineKeyboardButton("Uᴘᴅᴀᴛᴇꜱ", url="https://t.me/Blaze_Support"),
        InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Harsh_Pandit_xD"),
       InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/The_Blaze_network"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
