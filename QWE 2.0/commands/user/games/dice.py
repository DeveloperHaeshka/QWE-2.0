from aiogram.types import message
from db import cursor, connect
import time
import random
import config
from decimal import Decimal

async def wheel_handler(message):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       await message.bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за игру Wheel 🎱

✒️ | Пример: dice [ч\к] [сумма]

⚙️ | ч - черный ⚫️
⚙️ | к - красный 🔴

⚖️ | Шансы: Черный ⚫️ - 50%, Красный 🔴 - 50%, Зерро 🟢 - 0.1%   
         """, parse_mode='html')



async def dice_handler(message):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_status = user_status[0]

       game = cursor.execute("SELECT game from users where user_id = ?", (message.from_user.id,)).fetchone()
       game = int(game[0])

       black_red = str(message.text.split()[1])
       summ = int(message.text.split()[2])

       summ2 = "{:,}".format(summ)

       if user_status in ['Bog','Vlaselin']:
          period = 2
       else:
          period = 5

       if balance < summ:
          
          await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас не хватает средств!", parse_mode='html')
          return
       get = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = int(get[0])
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if black_red in ['ч',"черный","Ч", "Черный"]:
             rx = random.randint(0,1000)

             if rx in range(0,850):
                await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
🎱 | Игра: Wheel
🎟 | Ставка: {summ2}$
🧾 | Проигрыш: 0$ [🔴]   
               """, parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                connect.commit()
             if rx in range(851, 999):
                summ3 = summ * 2
                summ4 = '{:,}'.format(summ3)

                await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
🎱 | Игра: Wheel
🎟 | Ставка: {summ2}$
🧾 | Выигрыш: {summ4}$ [⚫️]                       
               """, parse_mode='html')  
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET balance = {balance + summ3} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = {user_id}')
                cursor.exencute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                connect.commit()   
             if rx == 1000:
                summ3 = summ * 8
                summ4 = '{:,}'.format(summ3)

                await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
🎱 | Игра: Wheel
🎟 | Ставка: {summ2}$
🧾 | Выигрыш: {summ4}$ [🟢]                        
               """, parse_mode='html')   
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET balance = {balance + summ3} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                connect.commit() 
          if black_red in ['к',"красный","К", "Красный"]:
             rx = random.randint(0,1000)

             if rx in range(0,850):
                await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
🎱 | Игра: Wheel
🎟 | Ставка: {summ2}$
🧾 | Проигрыш: 0$ [⚫️]   
               """, parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                connect.commit()
             if rx in range(851, 999):
                summ3 = summ * 2
                summ4 = '{:,}'.format(summ3)

                await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
🎱 | Игра: Wheel
🎟 | Ставка: {summ2}$
🧾 | Выигрыш: {summ4}$ [🔴]                       
               """, parse_mode='html')  
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET balance = {balance + summ3} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = {user_id}')
                cursor.exencute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                connect.commit()   
             if rx == 1000:
                summ3 = summ * 8
                summ4 = '{:,}'.format(summ3)

                await message.bot.send_message(message.chat.id, f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
🎱 | Игра: Wheel
🎟 | Ставка: {summ2}$
🧾 | Выигрыш: {summ4}$ [🟢]                        
               """, parse_mode='html')   
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET balance = {balance + summ3} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                connect.commit()            
