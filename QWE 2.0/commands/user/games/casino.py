from aiogram.types import message
from db import cursor, connect
from button.inline import gamevbmenu
import time
import random
import config
from decimal import Decimal


async def casino_handler(message):
    try:
        msg = message
        user_id = msg.from_user.id

        games = cursor.execute("SELECT game from users where user_id = ?", (message.from_user.id,)).fetchone()
        games = int(games[0])

        user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
        user_name = str(user_name[0])

        summ = int(msg.text.split()[1])
        summ2 = '{:,}'.format(summ)

        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))

        rx = random.randint(0,10216)
        if balance >= 999999999999999999999999999999999999999999999999999999999999999999:
            balance = 999999999999999999999999999999999999999999999999999999999999999999
            cursor.execute(f'UPDATE users SET balance = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            balance2 = '{:,}'.format(balance)
        period = 5
        get = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(0, 2500):
                        i = summ - summ * 0.3
                        i2 = int(i)
                        i3 = '{:,}'.format(i2)
                        await message.bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Проигрыш: {i3}$ [0.3X]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - i2} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                        connect.commit() 
                    if int(rx) in range(2501, 6500):
                        i = summ - summ * 0.5
                        i2 = int(i)
                        i3 = '{:,}'.format(i2)
                        await message.bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Проигрыш: {i3}$ [0.5X]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - i2} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                        connect.commit() 
                    if int(rx) in range(6500, 7500):
                        i = summ 
                        i2 = int(i)
                        i3 = '{:,}'.format(i2)
                        await message.bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Деньги остаються при вас [1X]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                        connect.commit() 
                    if int(rx) in range(7501, 9500):
                        i = summ * 1.5
                        i2 = int(i)
                        i3 = '{:,}'.format(i2)
                        await message.bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {i3}$ [1.5X]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET balance = {balance + i2} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                        connect.commit() 
                    if int(rx) in range(9501, 10000):
                        i = summ * 2.8
                        i2 = int(i)
                        i3 = '{:,}'.format(i2)
                        await message.bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {i3}$ [2.8X]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET balance = {balance + i2} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                        connect.commit() 
                    if int(rx) in range(10001, 10200):
                        i = summ * 5
                        i2 = int(i)
                        i3 = '{:,}'.format(i2)
                        await message.bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {i3}$ [5X]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET balance = {balance + i2} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                        connect.commit() 
                    if int(rx) in range(10201, 10210):
                        i = summ * 10
                        i2 = int(i)
                        i3 = '{:,}'.format(i2)
                        await message.bot.send_message(config.owner_id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {i3}$ [10X]", parse_mode='html')

                        await message.bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {i3}$ [10X]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET balance = {balance + i2} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                        connect.commit() 
                    if int(rx) in range(10211, 10215):
                        i = summ * 41
                        i2 = int(i)
                        i3 = '{:,}'.format(i2)
                        await message.bot.send_message(config.owner_id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {i3}$ [41X]", parse_mode='html')

                        await message.bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {i3}$ [41X]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET balance = {balance + i2} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                        connect.commit() 
                    if int(rx) == 10216:
                        i = summ * 100
                        i2 = int(i)
                        i3 = '{:,}'.format(i2)
                        await message.bot.send_message(config.owner_id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {i3}$ [100X]", parse_mode='html')

                        await message.bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🤵‍♀️ | Игра: Казино\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {i3}$ [100X]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET balance = {balance + i2} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = {user_id}')
                        cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                        connect.commit()   
                else:
                    await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число", parse_mode='html')     
            else:
                await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас нехватает средств!", parse_mode='html')     
        else:
            await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно раз в 5 секунд ", parse_mode='html')
    except IndexError:
        await message.reply(f'''
<a href='tg://user?id={user_id}'>{user_name}</a> ,  вот информация за казино 🤵

⚠️ | Команда: Казино [Ставка]

▶️ | Возможные Выигрыши и проигрыши: ⛔️[0.3Х] ⛔️[0.5Х] ❎[1Х] ✅[1.5Х] ✅[2.8Х] ✅[5Х] ✅[10Х] ✅[41Х] ✅[100Х]

⚖️ | Шансы:
      ⛔️ | 0.3Х - 25%
      ⛔️ | 0.5Х - 40%
      ❎ | 1Х - 25%
      ✅ | 1.5Х - 20%
      ✅ | 2.8Х - 5%
      ✅ | 5Х - 2%
      ✅ | 10Х - 0.1%
      ✅ | 41Х - 0.05%
      ✅ | 100Х - 0.01%

⏳ | Ограничения по времени: 5 секунд

        ''', parse_mode='html')