from aiogram.types import message
from db import cursor, connect
from email.message import Message
from button.inline import help2
import config


async def help_handler(message: Message):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       
       await message.bot.send_message(message.chat.id, f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, виберите категории🔍

📝 | Основные
🎮 | Игры 
🔨 | Работы
🏘 | Имущество
📖 | Привилегии
⛔️ | Admins menu 

Разработчик: {config.owner} 💻
Наша беседа: {config.chat}  💬 
    ''', reply_markup=help2, parse_mode='html')
