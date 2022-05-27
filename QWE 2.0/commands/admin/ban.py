from aiogram.types import message
from db import cursor, connect
import config

async def unban_id_handler(message):

    
    msg = message
    user_id = msg.from_user.id
    reply_user_id = int(message.text.split()[1])

    user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    reply_user_name = cursor.execute(f"SELECT user_name from users where user_id = {reply_user_id}").fetchone()
    reply_user_name = str(reply_user_name[0])

    

    if user_status == 'Owner':
       await message.bot.send_message(reply_user_id, f"✅ | <a href='tg://user?id={user_id}'>{reply_user_name}</a>, ваш аккаунт был разблокирован по ID", parse_mode='html')

       await message.bot.send_message(message.chat.id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Разбан аккаунта по ID\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')
       cursor.execute(f'UPDATE users SET status_block = "off"  WHERE user_id = {reply_user_id}')
       connect.commit()
       return
    if user_status == 'Helper_Admin':
       await message.bot.send_message(reply_user_id, f"✅ | <a href='tg://user?id={user_id}'>{reply_user_name}</a>, ваш аккаунт был разблокирован по ID", parse_mode='html')
       await message.bot.send_message(config.owner_id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Разбан аккаунта по ID\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')

       await message.bot.send_message(message.chat.id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Разбан аккаунта по ID\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')
       cursor.execute(f'UPDATE users SET status_block = "off"  WHERE user_id = {reply_user_id}')
       connect.commit()
       full_name = msg.from_user.full_name
       reply_full_name = msg.reply_to_message.from_user.full_name
       print(f'{full_name} выдал разбан игроку: {reply_full_name}')
       return
    else:
       await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная функция доступна только с категории администратора \"HELPER ADMIN\"", parse_mode='html')

async def unban_handler(message):
    if not message.reply_to_message:
       await message.reply("Эта команда должна быть ответом на сообщение!")
       return

    msg = message
    user_id = msg.from_user.id
    reply_user_id = msg.reply_to_message.from_user.id
    user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    reply_user_name = str(reply_user_name[0])

    

    if user_status == 'Owner':
       await message.bot.send_message(message.chat.id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Разбан аккаунта\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')
       cursor.execute(f'UPDATE users SET status_block = "off"  WHERE user_id = {reply_user_id}')
       connect.commit()
       return
    if user_status == 'Helper_Admin':
       await message.bot.send_message(config.owner_id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Разбан аккаунта\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')

       await message.bot.send_message(message.chat.id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Разбан аккаунта\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')
       cursor.execute(f'UPDATE users SET status_block = "off"  WHERE user_id = {reply_user_id}')
       connect.commit()
       full_name = msg.from_user.full_name
       reply_full_name = msg.reply_to_message.from_user.full_name
       print(f'{full_name} выдал разбан игроку: {reply_full_name}')
       return
    else:
       await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная функция доступна только с категории администратора \"HELPER ADMIN\"", parse_mode='html')


async def ban_id_handler(message):
    msg = message
    user_id = msg.from_user.id
    reply_user_id = int(message.text.split()[1])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    reply_user_name = cursor.execute(f"SELECT user_name from users where user_id = {reply_user_id}").fetchone()
    reply_user_name = str(reply_user_name[0])

    


    if user_status == 'Owner':
       await message.bot.send_message(reply_user_id, f"📛 | <a href='tg://user?id={user_id}'>{reply_user_name}</a>, ваш аккаунт был заблокирован по ID", parse_mode='html')

       await message.bot.send_message(message.chat.id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Бан аккаунта\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')
       cursor.execute(f'UPDATE users SET status_block = "on"  WHERE user_id = {reply_user_id}')
       full_name = msg.from_user.full_name
       
       print(f'{full_name} выдал бан игроку: {reply_user_name}')
       connect.commit()
       return
    if user_status == 'Helper_Admin':
       await message.bot.send_message(reply_user_id, f"📛 | <a href='tg://user?id={user_id}'>{reply_user_name}</a>, ваш аккаунт был заблокирован по ID", parse_mode='html')
       await message.bot.send_message(config.owner_id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Бан аккаунта\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')

       await message.bot.send_message(message.chat.id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Бан аккаунта\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')
       cursor.execute(f'UPDATE users SET status_block = "on"  WHERE user_id = {reply_user_id}')
       full_name = msg.from_user.full_name
       
       print(f'{full_name} выдал бан игроку: {reply_user_name}')
       connect.commit()
       return
    else:
       await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная функция доступна только с категории администратора \"HELPER ADMIN\"", parse_mode='html')

async def ban_handler(message):
    if not message.reply_to_message:
       await message.reply("Эта команда должна быть ответом на сообщение!")
       return


    msg = message
    user_id = msg.from_user.id
    reply_user_id = msg.reply_to_message.from_user.id
    user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    reply_user_name = str(reply_user_name[0])

    


    if user_status == 'Owner':
       await message.bot.send_message(message.chat.id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Бан аккаунта\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')
       cursor.execute(f'UPDATE users SET status_block = "on"  WHERE user_id = {reply_user_id}')
       full_name = msg.from_user.full_name
       reply_full_name = msg.reply_to_message.from_user.full_name
       print(f'{full_name} выдал бан игроку: {reply_full_name}')
       connect.commit()
       return
    if user_status == 'Helper_Admin':
       await message.bot.send_message(1887634547, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Бан аккаунта\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')

       await message.bot.send_message(message.chat.id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Бан аккаунта\n💈 | Время: навсегда\n👨 |Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')
       cursor.execute(f'UPDATE users SET status_block = "on"  WHERE user_id = {reply_user_id}')
       full_name = msg.from_user.full_name
       reply_full_name = msg.reply_to_message.from_user.full_name
       print(f'{full_name} выдал бан игроку: {reply_full_name}')
       connect.commit()
       return
    else:
       await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная функция доступна только с категории администратора \"HELPER ADMIN\"", parse_mode='html')









