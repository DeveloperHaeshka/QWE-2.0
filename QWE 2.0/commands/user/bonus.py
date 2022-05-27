from aiogram.types import message
from db import cursor, connect
import random
import time

async def bonus_handler(message):
    u = message.text.split()[1]
    if u == 'бонус':
        user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_name = user_name[0]
        user_id = message.from_user.id

        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        period = 86400 #86400 s = 24h
        get = cursor.execute("SELECT stavka_bonus FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
        last_stavka = int(get[0])
        stavkatime = time.time() - float(last_stavka)
        
        rx = random.randint(1000000,25000000)
        rx2 = '{:,}'.format(rx)

        if stavkatime > period:
            await message.bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ежедневный бонус в сумме {rx2}$ 💵", parse_mode='html')
            cursor.execute(f'UPDATE users SET balance = {balance + rx}  WHERE user_id = "{user_id}"')
            cursor.execute(f'UPDATE bot_time SET stavka_bonus = {time.time()} WHERE user_id = "{user_id}"')
            connect.commit()
        else:
            await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, получать ежедневный бонус можно раз в 24ч⏳", parse_mode='html') 


