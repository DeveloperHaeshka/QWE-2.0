from aiogram.types import message
from db import cursor, connect
from button.inline import gamevbmenu
import time
import random

async def football_handler(message):
       msg = message
       user_id = msg.from_user.id

       games = cursor.execute("SELECT game from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = int(games[0])

       user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       summ = int(message.text.split()[1])
       summ2 = '{:,}'.format(summ)

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       if balance >= 999999999999999999999999999999999999999999999999999999999999999999:
          balance = 999999999999999999999999999999999999999999999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance)

       rx = random.randint(0,9550)
       period = 5
       get = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(rx) in range(0,2900):
                   i = summ - summ * 0.2
                   i2 = int(i)
                   i3 = '{:,}'.format(i2)
                   await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
⚽️ | Игра: Футбол
🎟 | Ставка: {summ2}$
🧾 | Проигрыш: Промах! - {i3}$ [0.2X]
""", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET balance = {balance - i2} WHERE user_id = {user_id}')
                   connect.commit()
                if int(rx) in range(2901,6000):
                   i = summ - summ * 0.4
                   i2 = int(i)
                   i3 = '{:,}'.format(i2)
                   await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
⚽️ | Игра: Футбол
🎟 | Ставка: {summ2}$
🧾 | Проигрыш: Штанга! - {i3}$ [0.4X]
""", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET balance = {balance - i2} WHERE user_id = {user_id}')
                   connect.commit()
                if int(rx) in range(6001,8000):
                   i = summ - summ * 0.8
                   i2 = int(i)
                   i3 = '{:,}'.format(i2)
                   await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
⚽️ | Игра: Футбол
🎟 | Ставка: {summ2}$
🧾 | Проигрыш: Перекладина! - {i3}$ [0.8X]
""", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET balance = {balance - i2} WHERE user_id = {user_id}')
                   connect.commit()
                if int(rx) in range(8001,9200):
                   i = summ * 1.4
                   i2 = int(i)
                   i3 = '{:,}'.format(i2)
                   await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
⚽️ | Игра: Футбол
🎟 | Ставка: {summ2}$
🧾 | Выигрыш: Гол! - {i3}$ [1.4X]
""", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET balance = {balance + i2} WHERE user_id = {user_id}')
                   connect.commit()
                if int(rx) in range(9201,9500):
                   i = summ * 2.3
                   i2 = int(i)
                   i3 = '{:,}'.format(i2)
                   await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
⚽️ | Игра: Футбол
🎟 | Ставка: {summ2}$
🧾 | Выигрыш: Девятка! - {i3}$ [2.3X]
""", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET balance = {balance + i2} WHERE user_id = {user_id}')
                   connect.commit()
                if int(rx) in range(9501,9550):
                   i = summ * 4.3
                   i2 = int(i)
                   i3 = '{:,}'.format(i2)
                   await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
⚽️ | Игра: Футбол
🎟 | Ставка: {summ2}$
🧾 | Выигрыш: Крестовина! - {i3}$ [4.3X]
""", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET balance = {balance + i2} WHERE user_id = {user_id}')
                   connect.commit()
             else:
                await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число", parse_mode='html')     
          else:
             await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас нехватает средств!", parse_mode='html')     
       else:
          await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно раз в 5 секунд ", parse_mode='html')



async def football_info_handler(message):
       msg = message
       user_id = msg.from_user.id
   
       user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       await message.bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот вся информация за игру "Футбол" ⚽️

📌 | Пример: Футбол\Фб [ставка] | Футбол 1

⚖️ | Шансы:
🟥 | 29% - Промах - [0.2Х]
🟥 | 31% - Штанга - [0.4Х]
🟥 | 20% - Перекладина - [0.8X]
🟩 | 12% - Гол - [1.4X]
🟩 | 3% - Девятка - [2.3X]
🟩 | 1% - Крестовина - [4.3X]
""", parse_mode='html')
