from email.message import Message
from aiogram.types import message
from db import cursor, connect
import random
import config

async def zabrach_handler(message: Message):
       if not message.reply_to_message:
           await message.reply("Эта команда должна быть ответом на сообщение!")
           return

       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = str(reply_user_name[0])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])

       if int(balance2 - perevod) < 0:
         
          await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>,  нельзя заберать больше чем сам баланс игрока", parse_mode='html')
          return

       if user_status[0] == 'Owner':
          await message.reply(f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Отбор денег\n💈 |Количество: {perevod2}$\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
          return
       if user_status[0] == 'Helper_Admin':
          rows = cursor.execute('SELECT user_id FROM users where user_status = "Helper_Admin"').fetchall()
          for row in rows:
             await message.bot.send_message(row[0], f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Отбор денег\n💈 |Количество: {perevod2}$\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

          await message.bot.send_message(config.owner_id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Отбор денег\n💈 |Количество: {perevod2}$\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

          await message.reply(f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Отбор денег\n💈 |Количество: {perevod2}$\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
          return
       if user_status[0] == 'Admin':
          rows = cursor.execute('SELECT user_id FROM users where user_status = "Helper_Admin"').fetchall()
          for row in rows:
             await message.bot.send_message(row[0], f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Отбор денег\n💈 |Количество: {perevod2}$\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

          await message.bot.send_message(config.owner_id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Отбор денег\n💈 |Количество: {perevod2}$\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

          await message.reply(f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Отбор денег\n💈 |Количество: {perevod2}$\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
          return
       else:
          await message.reply(f"<a href='tg://user?id={user_id}'>{user_name}</a> ,Вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику <a href='t.me/haeshka_qwe_per/'>Хаешка</a>  ⚠️", parse_mode='html')

