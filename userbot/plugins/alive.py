#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "BAPU"
PM_IMG = "https://1.bp.blogspot.com/-feE2aIDKae8/X0nXBguWThI/AAAAAAAADgA/U9ZBLPzUvRQYDKj_aqKZLm574SijdUCsACPcBGAsYHg/s0/IMG_20200813_151339_068.jpg"
pm_caption = "`Bot is :` **ONLINE**\n\n"
pm_caption += "**I prefer broken bones instead of broken hearts**\n"
pm_caption += "`TELETHON VERSION:` **1.16.4**\n`Python:` **3.7.9**\n"
pm_caption += "`DATABASE STATUS:` **Check DATABASEPROPERTYEX Manually**\n"
pm_caption += "**Current Branch** : `Im a whole Tree you shit`\n"
pm_caption += "**FriClone Shit** : `3.14`\n"
pm_caption += f"**The Editor** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `If this text was edited in time then yeaa its working as its supposed to..`\n\n"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)

    
