from email.message import Message
from aiogram.types import message
from db import cursor, connect
from button.inline import gamevbmenu
import time
import random

async def gamevb_info_handler(message):
       msg = message
       user_id = msg.from_user.id
   
       user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       await message.bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот вся информация за игру "Game-VB" 🧊

📌 | Пример: /gamevb

⚠️ | ВАЖНО: Это игра, в которой нету ставки. В этой игре вы играете сразу на весь свой баланс

⚖️ | Шансы:
🟥 | 70% - LOSER - [0.1X]
🟩 | 30% - WIN - [1.5X]
       """, parse_mode='html')



async def gamevb_callback_handler(message: Message):
    user_id = message.from_user.id
    callback = message
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
    balance = int(balance[0])

    game = cursor.execute("SELECT game from users where user_id = ?",(callback.from_user.id,)).fetchone()
    game = int(game[0])

    balance2 = '{:,}'.format(balance)


    rx = random.randint(0, 10000)

    period = 5
    get = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (callback.from_user.id,)).fetchone()
    last_stavka = f"{int(get[0])}"
    stavkatime = time.time() - float(last_stavka)
    if stavkatime > period:
        if balance > 0:
            if int(rx) in range(0, 7000):
                i = balance - balance * 0.1
                i2 = int(i)
                i3 = '{:,}'.format(i2)
                await callback.message.answer(  f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
🧊 | Игра: GAME-VB
🎟 | Ставка: {balance2}$
🧾 | Проигрыш: {i3}$ [0.1X]            
    """, parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - i2} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = {user_id}')
                connect.commit()
                return
            if int(rx) in range(7001, 10000):
                i = balance * 1.5
                i2 = int(i)
                i3 = '{:,}'.format(i2)
                await callback.message.answer( f"""
🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>
🧊 | Игра: GAME-VB
🎟 | Ставка: {balance2}$
🧾 | Выигрыш: {i3}$ [1.5X]            
    """, parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + i2} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = {user_id}')
                connect.commit()
                return
        else:
            await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас недостаточно средств! ", parse_mode='html')
    else:
        await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно раз в 5 секунд", parse_mode='html')         




async def gamevb_handler(message: Message):
    msg = message
    user_id = msg.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    period = 5

    balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
    balance = int(balance[0])

    get = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
    last_stavka = f"{int(get[0])}"
    stavkatime = time.time() - float(last_stavka)
    if stavkatime > period:
        if balance > 0:
            await message.reply(f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вы уверены что хотите сыграть в GAME-VB ? 🧊

ℹ️ | В этой игре вы играете сразу на весь <b>баланс</b>

↘️ Выберите одну кнопку ниже         
    """,reply_markup=gamevbmenu,  parse_mode='html')
        else:
            await message.reply( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас недостаточно средств! ", parse_mode='html')
    else:
        await message.reply( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно раз в 5 секунд", parse_mode='html')         

