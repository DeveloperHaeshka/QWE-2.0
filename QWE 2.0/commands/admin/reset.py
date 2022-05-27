from email.message import Message
from aiogram.types import message
from db import cursor, connect
import config
import random

async def obnyl_handler(message: Message):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = str(reply_user_name[0])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()

       if not message.reply_to_message:
                await message.reply("Эта команда должна быть ответом на сообщение!")
                return
       if user_status[0] == 'Owner':
          await message.reply(f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Обнуление\n💈 |Количество: 1 раз\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET depozit = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET ethereum = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET iron = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET metall = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET silver = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET bronza = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET gold = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE farm SET linen = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE farm SET cotton = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE house SET house = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE house SET basement = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE cars SET cars = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE cars SET hp = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE cars SET benz = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_games = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_bonus = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_depozit = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_pick = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_rake = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_craft = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_kit = {0} WHERE user_id = "{reply_user_id}"')
          

          connect.commit() 
          return
       if user_status[0] == 'Helper_Admin':
          rows = cursor.execute('SELECT user_id FROM users where user_status = "Helper_Admin"').fetchall()
          for row in rows:
             await message.bot.send_message(row[0], f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Обнуление\n💈 |Количество: 1 раз\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

          await message.bot.send_message(config.owner_id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Обнуление\n💈 |Количество: 1 раз\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

          await message.reply(f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Обнуление\n💈 |Количество: 1 раз\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET depozit = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET ethereum = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET iron = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET metall = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET silver = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET bronza = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET gold = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE farm SET linen = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE farm SET cotton = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE house SET house = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE house SET basement = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE cars SET cars = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE cars SET hp = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE cars SET benz = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_games = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_bonus = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_depozit = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_pick = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_rake = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_craft = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_kit = {0} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
          return
       if user_status[0] == 'Admin':
          rows = cursor.execute('SELECT user_id FROM users where user_status = "Helper_Admin"').fetchall()
          for row in rows:
             await message.bot.send_message(row[0], f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Обнуление\n💈 |Количество: 1 раз\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

          await message.bot.send_message(config.owner_id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Обнуление\n💈 |Количество: 1 раз\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

          await message.reply(f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> \n⚙️ |Действие: Обнуление\n💈 |Количество: 1 раз\n👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET depozit = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET ethereum = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET iron = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET metall = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET silver = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET bronza = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE mine SET gold = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE farm SET linen = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE farm SET cotton = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE house SET house = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE house SET basement = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE cars SET cars = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE cars SET hp = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE cars SET benz = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_games = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_bonus = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_depozit = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_pick = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_rake = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_craft = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE bot_time SET time_kit = {0} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
          return
       else:
          await message.reply(f"<a href='tg://user?id={user_id}'>{user_name}</a> ,Вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику <a href='t.me/haeshka_qwe_per/'>Хаешка</a>  ⚠️", parse_mode='html')


async def reset_id_handler(message):

    msg = message
    user_id = msg.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_status = str(user_status[0])

    reply_user_id = int(message.text.split()[1])

    text = ' '.join(message.text.split()[2:])


    reply_user_name = cursor.execute(f"SELECT user_name from users where user_id = {reply_user_id}").fetchone()
    reply_user_name = str(reply_user_name[0])

    if user_status == 'Helper_Admin':
       await message.bot.send_message(config.owner_id, f"""
⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> 
⚙️ |Действие: Обнуление по ID
💈 |Причина: {text} 
👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
       """, parse_mode='html')

       await message.bot.send_message(message.chat.id, f"""
⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> 
⚙️ |Действие: Обнуление по ID
💈 |Причина: {text} 
👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
       """, parse_mode='html')
       cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE users SET depozit = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE users SET ethereum = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE mine SET iron = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE mine SET metall = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE mine SET bronza = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE farm SET linen = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE farm SET cotton = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE house SET house = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE house SET basement = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE cars SET cars = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE cars SET hp = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE cars SET benz = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET stavka_games = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET stavka_bank = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET stavka_bonus = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET stavka_depozit = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET time_pick = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET time_rake = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET time_craft = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET time_kit = {0} WHERE user_id = "{reply_user_id}"')
       connect.commit()
       await message.bot.send_message(reply_user_id, f"""
<b>🆘 | <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>, ВЫ БЫЛИ ОБНУЛЕНЫ | 🆘</b>
💭 | Причина: <i>{text}</i>
⛔️ | Администратором: <a href='tg://user?id={user_id}'>{user_name}</a> 
       """, parse_mode='html')
       return

    if user_status == 'Owner':
       await message.bot.send_message(message.chat.id, f"""
⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> 
⚙️ |Действие: Обнуление по ID
💈 |Причина: {text} 
👨 |Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>
       """, parse_mode='html')
       cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE users SET depozit = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE users SET ethereum = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE mine SET iron = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE mine SET metall = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE mine SET bronza = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE farm SET linen = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE farm SET cotton = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE house SET house = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE house SET basement = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE cars SET cars = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE cars SET hp = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE cars SET benz = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET stavka_games = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET stavka_bank = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET stavka_bonus = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET stavka_depozit = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET time_pick = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET time_rake = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET time_craft = {0} WHERE user_id = "{reply_user_id}"')
       cursor.execute(f'UPDATE bot_time SET time_kit = {0} WHERE user_id = "{reply_user_id}"')
       connect.commit()
       await message.bot.send_message(reply_user_id, f"""
<b>🆘 | <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>, ВЫ БЫЛИ ОБНУЛЕНЫ | 🆘</b>
💭 | Причина: <i>{text}</i>
⛔️ | Администратором: <a href='tg://user?id={user_id}'>{user_name}</a> 
       """, parse_mode='html')
       return
    else:
       await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная функция доступна от прав админитсратора \"ХЕЛПЕР АДМИН\"", parse_mode='html')



async def reset_handler(message):
    msg = message
    user_id = msg.from_user.id
    user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    
    

    if user_status == 'Owner':
       await message.bot.send_message(message.chat.id, f"⛔️ |Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Масовое обнуление\n💈 | Время: навсегда\n👨 |Игроку: Всем игрокам", parse_mode='html')
       cursor.execute(f'UPDATE users SET balance = {10000}')
       cursor.execute(f'UPDATE users SET user_name = "Игрок"')
       cursor.execute(f'UPDATE users SET bank = {1000}')
       cursor.execute(f'UPDATE users SET depozit = {0}')
       cursor.execute(f'UPDATE users SET rating = {0}')
       cursor.execute(f'UPDATE users SET ethereum = {100}')
       cursor.execute(f'UPDATE mine SET iron = {0}')
       cursor.execute(f'UPDATE mine SET metall = {0}')
       cursor.execute(f'UPDATE mine SET silver = {0}')
       cursor.execute(f'UPDATE mine SET bronza = {0}')
       cursor.execute(f'UPDATE mine SET gold = {0}')
       cursor.execute(f'UPDATE farm SET linen = {0}')
       cursor.execute(f'UPDATE farm SET cotton = {0}')
       cursor.execute(f'UPDATE house SET house = {0}')
       cursor.execute(f'UPDATE house SET basement = {0}')
       cursor.execute(f'UPDATE cars SET cars = {0}')
       cursor.execute(f'UPDATE cars SET hp = {0}')
       cursor.execute(f'UPDATE cars SET benz = {0}')
       cursor.execute(f'UPDATE bot_time SET stavka_games = {0} ')
       cursor.execute(f'UPDATE bot_time SET stavka_bank = {0} ')
       cursor.execute(f'UPDATE bot_time SET stavka_bonus = {0} ')
       cursor.execute(f'UPDATE bot_time SET stavka_depozit = {0} ')
       cursor.execute(f'UPDATE bot_time SET time_pick = {0} ')
       cursor.execute(f'UPDATE bot_time SET time_rake = {0} ')
       cursor.execute(f'UPDATE bot_time SET time_craft = {0} ')
       cursor.execute(f'UPDATE bot_time SET time_kit = {0} ')

       connect.commit()
       full_name = msg.from_user.full_name
       print(f'{full_name} сделал масовое обнуление')
       return
    else:
       await message.reply( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная функция доступна только с категории администратора \"OWNER\"", parse_mode='html')
