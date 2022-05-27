from email.message import Message
from aiogram import types, Bot
from datetime import datetime, timedelta
import config

bot = Bot(token=config.token[1])

async def unmute_handler(message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
       await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
       return
    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
    await message.reply(f'👤 | Администратор: {name1}\n🔊 | Размутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>',  parse_mode='html')


async def mute_handler(message: Message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
       await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
       return
    try:
       muteint = int(message.text.split()[1])
       mutetype = message.text.split()[2]
       comment = " ".join(message.text.split()[3:])
    except IndexError:
       await message.reply('ℹ | Не хватает аргументов!\nПример:\n<code>/мут 1 ч причина</code>')
       return
    if mutetype == "ч" or mutetype == "часов" or mutetype == "час":
       dt = datetime.now() + timedelta(hours=muteint)
       timestamp = dt.timestamp()
       await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
       await message.reply(f'👤 | Администратор: {name1}\n🛑 | Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: {muteint} {mutetype}\n📃 | Причина: {comment}',  parse_mode='html')
    if mutetype == "м" or mutetype == "минут" or mutetype == "минуты":
       dt = datetime.now() + timedelta(minutes=muteint)
       timestamp = dt.timestamp()
       await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
       await message.reply(f'👤 | Администратор: {name1}\n🛑 | Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: {muteint} {mutetype}\n📃 | Причина: {comment}',  parse_mode='html')
    if mutetype == "д" or mutetype == "дней" or mutetype == "день":
       dt = datetime.now() + timedelta(days=muteint)
       timestamp = dt.timestamp()
       await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
       await message.reply(f'👤 | Администратор: {name1}\n | 🛑Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: {muteint} {mutetype}\n📃 | Причина: {comment}',  parse_mode='html')

