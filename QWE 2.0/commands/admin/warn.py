from aiogram.types import message
from db import cursor, connect
import config

async def unwarn_handler(message):
    if not message.reply_to_message:
       await message.reply("🆘 | Эта команда должна быть ответом на сообщение!")
       return   
    reply_user_id = message.reply_to_message.from_user.id

    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    reply_user_name = cursor.execute(f"SELECT user_name from users where user_id = {reply_user_id}").fetchone()
    reply_user_name = str(reply_user_name[0])
    user_id = message.from_user.id
    

    status_block = cursor.execute("SELECT status_block from users where user_id = ?",(message.from_user.id,)).fetchone()
    status_block = str(status_block[0])
    
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_status = str(user_status[0])

    warn = cursor.execute(f"SELECT warn from warn where user_id = {reply_user_id}").fetchone()
    warn = int(warn[0])

    warn2 = warn - 1
   
    if user_status == 'Owner':
       if warn2 < 0:
          await message.reply( f"🆘 | Нельзя забирать больше варнов чем у самого игрока")
          return
    if user_status == 'Helper_Admin':
       if warn2 < 0:
          await message.reply( f"🆘 | Нельзя забирать больше варнов чем у самого игрока")
          return
    if user_status == 'Owner':
       await message.bot.send_message(message.chat.id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Отбор варнов
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')
       cursor.execute(f'UPDATE warn SET warn = {warn - 1} WHERE user_id = {reply_user_id}')
       connect.commit()
       return
    if user_status == 'Helper_Admin':
       await message.bot.send_message(config.owner_id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Отбор варнов
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')
       await message.bot.send_message(message.chat.id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Отбор варнов
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')
       cursor.execute(f'UPDATE warn SET warn = {warn - 1} WHERE user_id = {reply_user_id}')
       connect.commit()
       return
    else:
       await message.reply( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная команда доступна от прав администратора \"HELPER-ADMINS\"", parse_mode='html')


async def unwarn_id_handler(message):
    reply_user_id = int(message.text.split()[1])

    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    reply_user_name = cursor.execute(f"SELECT user_name from users where user_id = {reply_user_id}").fetchone()
    reply_user_name = str(reply_user_name[0])
    user_id = message.from_user.id
    

    status_block = cursor.execute("SELECT status_block from users where user_id = ?",(message.from_user.id,)).fetchone()
    status_block = str(status_block[0])
    
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_status = str(user_status[0])

    warn = cursor.execute(f"SELECT warn from warn where user_id = {reply_user_id}").fetchone()
    warn = int(warn[0])

    warn2 = warn - 1
   
    if user_status == 'Owner':
       if warn2 < 0:
          await message.reply( f"🆘 | Нельзя забирать больше варнов чем у самого игрока")
          return
    if user_status == 'Helper_Admin':
       if warn2 < 0:
          await message.reply( f"🆘 | Нельзя забирать больше варнов чем у самого игрока")
          return
    if user_status == 'Owner':
       await message.bot.send_message(message.chat.id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Отбор варнов по ID
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')
       cursor.execute(f'UPDATE warn SET warn = {warn - 1} WHERE user_id = {reply_user_id}')
       connect.commit()
       return
    if user_status == 'Helper_Admin':
       await message.bot.send_message(config.owner_id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Отбор варнов по ID
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')
       await message.bot.send_message(message.chat.id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Отбор варнов по ID
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')
       cursor.execute(f'UPDATE warn SET warn = {warn - 1} WHERE user_id = {reply_user_id}')
       connect.commit()
       return
    else:
       await message.reply( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная команда доступна от прав администратора \"HELPER-ADMINS\"", parse_mode='html')


async def warn_id_hendler(message):
    reply_user_id = int(message.text.split()[1])

    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    reply_user_name = cursor.execute(f"SELECT user_name from users where user_id = {reply_user_id}").fetchone()
    reply_user_name = str(reply_user_name[0])
    user_id = message.from_user.id
    

    status_block = cursor.execute("SELECT status_block from users where user_id = ?",(message.from_user.id,)).fetchone()
    status_block = str(status_block[0])
    
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_status = str(user_status[0])

    warn = cursor.execute(f"SELECT warn from warn where user_id = {reply_user_id}").fetchone()
    warn = int(warn[0])

    warn2 = warn + 1
   
    if user_status == 'Owner':
       if warn2 > 5:
          await message.bot.send_message(reply_user_id, f"⚠️ | <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> , ваш аккаунт был заблокирован из-за 6\6 варнов", parse_mode='html')

          await message.bot.send_message(message.chat.id, f"⚠️ | Аккаунт: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> был заблокирован ", parse_mode='html')
          cursor.execute(f'UPDATE users SET status_block = "on" WHERE user_id = {reply_user_id}')
          cursor.execute(f'UPDATE warn SET warn = {0} WHERE user_id = {reply_user_id}')
          connect.commit()
          return
    if user_status == 'Helper_Admin':
       if warn2 > 5:
          await message.bot.send_message(reply_user_id, f"⚠️ | <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> , ваш аккаунт был заблокирован из-за 6\6 варнов", parse_mode='html')

          await message.bot.send_message(config.owner_id, f"⚠️ | Аккаунт: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> был заблокирован ", parse_mode='html')

          await message.bot.send_message(message.chat.id, f"⚠️ | Аккаунт: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> был заблокирован ", parse_mode='html')
          cursor.execute(f'UPDATE users SET status_block = "on" WHERE user_id = {reply_user_id}')
          cursor.execute(f'UPDATE warn SET warn = {0} WHERE user_id = {reply_user_id}')
          connect.commit()
          return
    if user_status == 'Owner':
       await message.bot.send_message(message.chat.id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Выдача варна по ID
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')
       cursor.execute(f'UPDATE warn SET warn = {warn + 1} WHERE user_id = {reply_user_id}')
       connect.commit()
       return
    if user_status == 'Helper_Admin':
       await message.bot.send_message(config.owner_id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Выдача варна по ID
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')

       await message.bot.send_message(message.chat.id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Выдача варна по ID
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')
       cursor.execute(f'UPDATE warn SET warn = {warn + 1} WHERE user_id = {reply_user_id}')
       connect.commit()
       return
    else:
       await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная команда доступна от прав администратора \"HELPER-ADMINS\"", parse_mode='html')


async def warn_hendler(message):
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    reply_user_name = str(reply_user_name[0])
    user_id = message.from_user.id
    reply_user_id = message.reply_to_message.from_user.id

    status_block = cursor.execute("SELECT status_block from users where user_id = ?",(message.from_user.id,)).fetchone()
    status_block = str(status_block[0])
    
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_status = str(user_status[0])

    warn = cursor.execute("SELECT warn from warn where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
    warn = int(warn[0])

    warn2 = warn + 1
   
    if user_status == 'Owner':
       if warn2 > 5:
          await message.bot.send_message(message.chat.id, f"⚠️ | <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> , ваш аккаунт был заблокирован ", parse_mode='html')
          cursor.execute(f'UPDATE users SET status_block = "on" WHERE user_id = {reply_user_id}')
          cursor.execute(f'UPDATE warn SET warn = {0} WHERE user_id = {reply_user_id}')
          connect.commit()
          return
    if user_status == 'Helper_Admin':
       if warn2 > 5:
          await message.bot.send_message(message.chat.id, f"⚠️ | <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> , ваш аккаунт был заблокирован ", parse_mode='html')
          cursor.execute(f'UPDATE users SET status_block = "on" WHERE user_id = {reply_user_id}')
          cursor.execute(f'UPDATE warn SET warn = {0} WHERE user_id = {reply_user_id}')
          connect.commit()
          return
    if user_status == 'Owner':
       await message.bot.send_message(message.chat.id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Выдача варна
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')
       cursor.execute(f'UPDATE warn SET warn = {warn + 1} WHERE user_id = {reply_user_id}')
       connect.commit()
       return
    if user_status == 'Helper_Admin':
       await message.bot.send_message(config.owner_id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Выдача варна
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')

       await message.bot.send_message(message.chat.id, f"""
⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>   
⚙️ | Действие: Выдача варна
👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
🛑 | Варнов у игрока: {warn2}/6     
       """, parse_mode='html')
       cursor.execute(f'UPDATE warn SET warn = {warn + 1} WHERE user_id = {reply_user_id}')
       connect.commit()
       return
    else:
       await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная команда доступна от прав администратора \"HELPER-ADMINS\"", parse_mode='html')
    





