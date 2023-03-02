# ©AKBOTZ

import re
import aiohttp

from os import environ
from pyrogram import Client, filters
from pyrogram.types import *

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY')
API_URL = environ.get('API_URL')

akbotz = Client('link shortener bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=100)

print("Developer: @AKBotZ , Join & Share Channel")
print("Bot is Started Now")

@akbotz.on_message(filters.command('start') & filters.private)
async def start(bot, message):
      await bot.send_photo(
         chat_id=msg.chat.id,
         photo="https://te.legra.ph/file/97f5e8527f3ee553f3851.jpg",
         caption=f"""**ʜᴇʟʟᴏ {message.chat.first_name} !
         
๏ ᴛʜɪs ɪs 
➻ ᴛʜᴇ ᴍᴏsᴛ ᴩᴏᴡᴇʀғᴜʟ ʟɪɴᴋ sʜᴏʀᴛɴᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.
➻ ʏᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴍᴜʟᴛɪᴘʟᴇ ʟɪɴᴋs sᴇᴘᴇʀᴀᴛᴇᴅ ʙʏ sᴘᴀᴄᴇ ᴀɴᴅ ᴇɴᴛᴇʀ.

──────────────────
๏ Jᴜsᴛ sᴇɴᴅ ᴍᴇ ʟɪɴᴋ ᴀɴᴅ ɢᴇᴛ sʜᴏʀᴛ ʟɪɴᴋ
ᴅᴇᴠʟᴏᴘᴇʀ : @SayJust***"""

reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/ScaryServer")
                ],
                [
                    InlineKeyboardButton("✘ sᴜᴘᴘᴏʀᴛ", url="https://t.me/Chat_ixz")
                ]
            ]
        ),
    )



@akbotz.on_message(filters.private & filters.text & filters.incoming)
async def link_handler(bot, message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) <1:
        await message.reply("**ɴᴏ ʟɪɴᴋ ғᴏᴜɴᴅ ɪɴ ᴛʜɪs ᴛᴇxᴛ**",quote=True)
        return
    for link in links:
        try:
            short_link = await get_shortlink(link)
            await message.reply(f"**ʜᴇʀᴇ ɪs ʏᴏᴜʀ sʜᴏʀᴛᴇɴᴇᴅ ʟɪɴᴋ**\n\n**ᴏʀɪɢɪɴᴀʟ ʟɪɴᴋ: {link}**\n\n**sʜᴏʀᴛᴇɴᴅ ʟɪɴᴋ : `{short_link}` **",quote=True,disable_web_page_preview=True)
        except Exception as e:
            await message.reply(f'**ᴇʀʀᴏʀ : `{e}` **', quote=True)


async def get_shortlink(link):
    url = API_URL
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


akbotz.run()
