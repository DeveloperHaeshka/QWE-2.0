from aiogram.types import message
from db import cursor, connect
import time
import random
import config
from decimal import Decimal


async def plinko_handler(message):
    try:
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        games = cursor.execute("SELECT game from users where user_id = ?", (message.from_user.id,)).fetchone()
        games = int(games[0])

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0,937)
        rwin = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
        user_name = str(user_name[0])
        name = msg.from_user.full_name 
        summ = int(msg.text.split()[1])
        summ2 = '{:,}'.format(summ)
        print(f"{name} поставил в казино: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))

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
                    if int(rx) in range(0,100):
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await message.bot.send_message(chat_id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n◾️ | Игра: Плинко\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: 0$ [x0]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot_time SET stavka_games=? WHERE user_id=?', (time.time(), user_id,))
                        connect.commit()   
                        return                           
                    if int(rx) in range(101,300):
                        c = Decimal(summ - summ * 0.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await message.bot.send_message(chat_id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n◾️ | Игра: Плинко\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {c2}$ [x0.25]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot_time SET stavka_games=? WHERE user_id=?', (time.time(), user_id,))
                        connect.commit()  
                        return   
                    if int(rx) in range(301,600):
                        c = Decimal(summ * 0.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await message.bot.send_message(chat_id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n◾️ | Игра: Плинко\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {c2}$ [x0.5]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot_time SET stavka_games=? WHERE user_id=?', (time.time(), user_id,))
                        connect.commit() 
                        return  
                    if int(rx) in range(601,850):
                        c = Decimal(summ - summ * 0.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await message.bot.send_message(chat_id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n◾️ | Игра: Плинко\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {c2}$ [x0.75]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot_time SET stavka_games=? WHERE user_id=?', (time.time(), user_id,))
                        connect.commit() 
                        return  
                    if int(rx) in range(851,900):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n◾️ | Игра: Плинко\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {c2}$ [x2]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot_time SET stavka_games=? WHERE user_id=?', (time.time(), user_id,))
                        connect.commit() 
                        return 
                    if int(rx) in range(901,930):
                        c = Decimal(summ * 3)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await message.bot.send_message(chat_id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n◾️ | Игра: Плинко\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {c2}$ [x3]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot_time SET stavka_games=? WHERE user_id=?', (time.time(), user_id,))
                        connect.commit() 
                        return
                    if int(rx) in range(931,932):
                        c = Decimal(summ * 29)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await message.bot.send_message(chat_id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n◾️ | Игра: Плинко\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {c2}$ [x29]", parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 29)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot_time SET stavka_games=? WHERE user_id=?', (time.time(), user_id,))
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = "{user_id}"')
                        connect.commit()
                    if int(rx) in range(933,937):
                        c = Decimal(summ * 10)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await message.bot.send_message(chat_id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n◾️ | Игра: Плинко\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {c2}$ [x10]", parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot_time SET stavka_games=? WHERE user_id=?', (time.time(), user_id,))
                        connect.commit() 
                        return 
                elif summ <= 1:
                    await message.bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}", parse_mode='html')                                      
            elif int(balance) <= int(summ):
                await message.bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
        else:
            await message.bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, извини. но играть можно только каждые 5️⃣ секунд. {rloser}", parse_mode='html')
            return
    except IndexError:
        return