from aiogram.types import message
from db import cursor, connect
import time
import random
import config
from decimal import Decimal

async def chet_handler(message):
    try:
        user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_name = user_name[0]
        user_id = message.from_user.id

        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])

        game = cursor.execute("SELECT game from users where user_id = ?", (message.from_user.id,)).fetchone()
        game = int(game[0])

        rx = random.randint(0,100)

        summ = int(message.text.split()[1])
        summ2 = '{:,}'.format(summ)

        summ_win = summ * 2
        summ_win2 = '{:,}'.format(summ_win)

        period = 5
        get = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
        last_stavka = int(get[0])
        stavkatime = time.time() - float(last_stavka)

        if balance >= 999999999999999999999999999999999999999999999999999999999999999999:
            balance = 999999999999999999999999999999999999999999999999999999999999999999
            cursor.execute(f'UPDATE users SET balance = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            balance2 = '{:,}'.format(balance)

        if summ <= balance:
            if stavkatime > period:
                if int(rx) in range(0,65):
                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Чётное \ нечётное\n🎟 | Ставка: 🎲Чётное - {summ2}$\n🧾 | Выигрыш: 🎲Нечётное - 0$", parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = "{user_id}"')
                    connect.commit()
                if int(rx) in range(66,100):
                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Чётное \ нечётное\n🎟 | Ставка: 🎲Чётное - {summ2}$\n🧾 | Выигрыш: 🎲Чётное - {summ_win2}$", parse_mode='html')
                    cursor.execute(f'UPDATE users SET balance = {balance + summ_win} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = "{user_id}"')
                    connect.commit()
            else:
                await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Играть можно раз в 5 секунд", parse_mode='html')
        else:
            await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас не хватает средств!", parse_mode='html')
    except IndexError:
        await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Ошибка! Пример: Чётное 1000", parse_mode='html')



async def nechet_handler(message):
     try:
         user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
         user_name = user_name[0]
         user_id = message.from_user.id

         balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
         balance = int(balance[0])

         game = cursor.execute("SELECT game from users where user_id = ?", (message.from_user.id,)).fetchone()
         game = int(game[0])

         rx = random.randint(0,100)

         summ = int(message.text.split()[1])
         summ2 = '{:,}'.format(summ)

         if balance >= 999999999999999999999999999999999999999999999999999999999999999999:
            balance = 999999999999999999999999999999999999999999999999999999999999999999
            cursor.execute(f'UPDATE users SET balance = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            balance2 = '{:,}'.format(balance)

         summ_win = summ * 2
         summ_win2 = '{:,}'.format(summ_win)

         period = 5
         get = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
         last_stavka = int(get[0])
         stavkatime = time.time() - float(last_stavka)

         if summ <= balance:
            if stavkatime > period:
               if int(rx) in range(0,65):
                  await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Чётное \ нечётное\n🎟 | Ставка: 🎲Нечётное - {summ2}$\n🧾 | Выигрыш: 🎲Чётное - 0$", parse_mode='html')
                  cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
               if int(rx) in range(66,100):
                  await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Чётное \ нечётное\n🎟 | Ставка: 🎲Нечётное - {summ2}$\n🧾 | Выигрыш: 🎲Нечётное - {summ_win2}$", parse_mode='html')
                  cursor.execute(f'UPDATE users SET balance = {balance + summ_win} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
            else:
               await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Играть можно раз в 5 секунд", parse_mode='html')
         else:
            await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас не хватает средств!", parse_mode='html')
     except IndexError:
         await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Ошибка! Пример: Чётное 1000", parse_mode='html')
