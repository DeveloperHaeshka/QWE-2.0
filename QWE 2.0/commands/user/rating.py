from aiogram.types import message
from db import cursor, connect
import random

async def rating_up_handler(message):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       summ = int(msg.text.split()[1])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       rating2 = '{:,}'.format(summ)
       c = summ * 150000000

       if (summ + rating) >= 999999999999999999999999999999999999999999999999999999999999999999:
          await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>,  нельзя покупать рейтинг больше лимита")
          return

       c2 = '{:,}'.format(c)
       if summ > 0:
        if int(balance) >= int(summ * 150000000):
          await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы повысили количество вашего рейтинга на {rating2}💎 за {c2}$! {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
          connect.commit()

 
        if int(balance) < int(summ * 150000000):
          await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')

       if summ <= 0:
         await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')


async def rating_down_handler(message):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       summ = int(msg.text.split()[1])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       c = summ * 100000000
       c2 = '{:,}'.format(c)
       rating2 = '{:,}'.format(summ)
       if summ > 0:
        if int(rating) >= int(summ):
          await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы понизили количество вашего рейтинга на {rating2}💎 за {c2}$! {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
          connect.commit()

        if int(rating) < int(summ):
          await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, у вас недостаточно рейтинга для его продажи! {rloser}", parse_mode='html')

       if summ <= 0:
          await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, нельзя продать отрицательное число! {rloser}", parse_mode='html')


async def rating_handler(message):
       msg = message
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                    (message.from_user.id,)).fetchone()
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       bank = int(bank[0])
       rating = int(rating[0])
       rating2 = '{:,}'.format(rating)
       rey = ['👑','✨','✏️']
       ranrey = random.choice(rey)
       
      
       await message.bot.send_message(message.chat.id, f"💎 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш рейтинг - {rating2}", parse_mode='html')

