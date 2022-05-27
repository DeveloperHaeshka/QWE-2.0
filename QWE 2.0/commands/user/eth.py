from aiogram.types import message
from db import cursor, connect
from pycoingecko import CoinGeckoAPI

api = CoinGeckoAPI()

async def eth_handler(message):
    try:
        user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_name = user_name[0]
        user_id = message.from_user.id
        
        i = str(message.text.split()[1])
        d = int(message.text.split()[2])
        d2 = '{:,}'.format(d)
        c = api.get_price(ids='ethereum', vs_currencies='usd')['ethereum']['usd']
        c2 = int(c)
        c3 = '{:,}'.format(c2)

        ethereum = cursor.execute("SELECT ethereum from users where user_id = ?", (message.from_user.id,)).fetchone()
        ethereum = int(ethereum[0])

        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))

        summ = d * c2
        summ2 = '{:,}'.format(summ)

        if summ >= 999999999999999999999999999999999999999999999999999999999999999999:
            await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>,  достигнул лимит, 999 гвинт")
            return

        if i == 'купить':
            if summ <= balance:
                if d > 0:
                    await message.bot.send_message(message.chat.id, f" 💸 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {d2} эфириума 🟣 за {summ2}$", parse_mode='html')
                    cursor.execute(f'UPDATE users SET ethereum = {ethereum + d}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET balance = {balance - summ}  WHERE user_id = "{user_id}"')
                    connect.commit()
                else:
                    await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя покупать отрицательное число ", parse_mode='html')
            else:
                await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств ", parse_mode='html')
        if i == 'продать':
            if d <= ethereum:
                if d > 0:
                    await message.bot.send_message(message.chat.id, f" 💸 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {d2} эфириума 🟣 за {summ2}$", parse_mode='html')
                    cursor.execute(f'UPDATE users SET ethereum = {ethereum - d}  WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET balance = {balance + summ}  WHERE user_id = "{user_id}"')
                    connect.commit()
                else:
                    await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя покупать отрицательное число ", parse_mode='html')
            else:
                await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств ", parse_mode='html')          
    except IndexError:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       c = api.get_price(ids='ethereum', vs_currencies='usd')['ethereum']['usd']
       c2 = int(c)
       c3 = '{:,}'.format(c2)

       await message.bot.send_message(message.chat.id,f"🟪 | <a href='tg://user?id={user_id}'>{user_name}</a>, курс эфириума: {c3}🟣", parse_mode='html')
    


