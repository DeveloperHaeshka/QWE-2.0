from email.message import Message
from aiogram import types, Bot
from datetime import datetime, timedelta
import config

bot = Bot(token=config.token[1])

async def ban_handler(message: Message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
       await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
       return
    comment = " ".join(message.text.split()[1:])
    await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False))
    await message.reply(f'👤 | Администратор: {name1}\n🛑 | Забанил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: навсегда\n📃 | Причина: {comment}',  parse_mode='html')

async def unban_handler(message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
       await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
       return
    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
    await message.reply(f'👤 | Администратор: {name1}\n📲 | Разбанил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>',  parse_mode='html')
