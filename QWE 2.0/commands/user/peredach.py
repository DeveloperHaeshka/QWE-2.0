from aiogram.types import message
from db import cursor, connect
import random
import config

async def dach_handler(message):
       if not message.reply_to_message:
          await message.reply("Эта команда должна быть ответом на сообщение!")
          return
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.full_name 
       rname =  msg.reply_to_message.from_user.full_name 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = str(reply_user_name[0])

       reply_user_id = msg.reply_to_message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = int(msg.text.split()[1])
       perevod2 = '{:,}'.format(perevod)
       print(f"{name} перевел: {perevod} игроку {rname}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])

       
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if perevod > 0:
          if balance >= perevod:  
             await message.bot.send_message(config.owner_id, f"👨 | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ | Действие: Передача денег\n💈 | Сумма: {perevod2}$\n👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

             await message.reply_to_message.reply(f"👨 | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ | Действие: Передача денег\n💈 | Сумма: {perevod2}$\n👨 | Игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
             connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f"<a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')

       if perevod <= 0:
          await message.reply( f"<a href='tg://user?id={user_id}'>{user_name}</a>, нельзя перевести отрицательное число! {rloser}", parse_mode='html')  



async def peredach_handler(message):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.full_name 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_status = str(user_status[0])

       perevod = int(msg.text.split()[1])
       id_perevod = int(msg.text.split()[2])
       
       name_id_perevod = 'Аккаунт'

       perevod2 = '{:,}'.format(perevod)
       print(f"{name} перевел: {perevod} игроку на ID: {id_perevod}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       balance2 = cursor.execute(f"SELECT balance from users where user_id = {id_perevod}").fetchone()
       balance2 = round(int(balance2[0]))
       if perevod > 0:
          if balance >= perevod:  
             if user_status in ['Admin', 'Helper_Admin']:
               await message.bot.send_message(config.owner_id, f"👨 | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ | Действие: Передача денег по ID\n💈 | Сумма: {perevod2}\n👨 | Игроку: <a href='tg://user?id={id_perevod}'>{name_id_perevod}</a>", parse_mode='html')

             await message.bot.send_message(id_perevod, f"👨 | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ | Действие: Передача денег по ID\n💈 | Сумма: {perevod2}\n👨 | Игроку: <a href='tg://user?id={id_perevod}'>{name_id_perevod}</a>", parse_mode='html')
             await message.reply(f"👨 | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ | Действие: Передача денег по ID\n💈 | Сумма: {perevod2}\n👨 | Игроку: <a href='tg://user?id={id_perevod}'>{name_id_perevod}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{id_perevod}"')
             connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if perevod <= 0:
          await message.reply( f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')  


