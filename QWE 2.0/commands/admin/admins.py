from email.message import Message
from aiogram.types import message
from db import cursor, connect
from button.inline import admin_menu

async def admin_menu_handler(message: Message):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await message.bot.send_message(message.chat.id,f"<a href='tg://user?id={user_id}'>{user_name}</a>, войдите в админ меню🆘", reply_markup=admin_menu, parse_mode='html')
