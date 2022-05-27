from db import cursor, connect
from email.message import Message
import random
import time
from decimal import Decimal

async def spin_handler(message: Message):
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        games = cursor.execute("SELECT game from users where user_id = ?", (message.from_user.id,)).fetchone()
        games = int(games[0])

        balance2 = '{:,}'.format(balance)
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id
        rx = random.randint(0, 1001)
        msg = message
        user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
        user_name = str(user_name[0])
        name = msg.from_user.full_name
        summ = int(message.text.split()[1])


        summ2 = '{:,}'.format(summ)
        print(f"{name} поставил в спин: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5 
        get = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        loz = ['💩|👑|👑','💩|🖕|👑','💎|🖕|👑','💎|💣|🍌','👑|🍌|🖕','💎|🍓|💣']
        win = ['💎|🍓|🍌','👑|💎|🍓','🍓|👑|💎','💎|🍓|🍌','💎|🍓|🍓','🍌|🍌|💎']
        Twin = ['💎|💎|💎','🍓|🍓|🍓','👑|👑|👑','🍌|🍌|🍌']
        smtwin = ['🤯','🤩','😵','🙀']
        smwin = ['🙂', '😋', '😄', '🤑', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rsmtwin = random.choice(smtwin)
        rsmtwin2 = random.choice(smtwin)
        rtwin = random.choice(Twin)
        rloser = random.choice(loser)
        rloser2 = random.choice(loser)
        rwin = random.choice(win)
        rloz = random.choice(loz)
        rsmwin = random.choice(smwin)
        rsmwin2 = random.choice(smwin)
        if balance >= 999999999999999999999999999999999999999999999999999999999999999999:
            balance = 999999999999999999999999999999999999999999999999999999999999999999
            cursor.execute(f'UPDATE users SET balance = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            balance2 = '{:,}'.format(balance)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(0, 350):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)

                        await message.bot.send_message(chat_id,
                                               f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎰 | Игра: Спин\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {rwin} - {c2}$",
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot_time SET stavka_games=? WHERE user_id=?', (time.time(), user_id,))
                        connect.commit()
                        return

        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(351, 1000):
                        c = Decimal(summ * 0)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await message.bot.send_message(chat_id,
                                               f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎰 | Игра: Спин\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {rloz} - {c2}$",
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 0)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot_time SET stavka_games=? WHERE user_id=?', (time.time(), user_id,))
                        connect.commit()
                        return
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) == 1001:
                        c = Decimal(summ * 25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await message.bot.send_message(chat_id,
                                               f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎰 | Игра: Спин\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {rwin} - {c2}$ - Джекпот",
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 25)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET game = {games + 1} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot_time SET stavka_games=? WHERE user_id=?', (time.time(), user_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await message.bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}",
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await message.bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
        else:
            await message.bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, извини. но играть можно только каждые 5️⃣ секунд. {rloser}",
                                       parse_mode='html')
