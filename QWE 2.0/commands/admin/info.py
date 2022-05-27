from email.message import Message
from aiogram.types import message
from db import cursor, connect

async def info_handler(message: Message):
    msg = message
    user_id = msg.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    if not message.reply_to_message:
       await message.reply( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, эта команда должна быть ответом на сообщение", parse_mode='html')
       return
       
    user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_status = str(user_status[0])

    reply_user_id = message.reply_to_message.from_user.id

    balance = cursor.execute(f"SELECT balance from users where user_id = {reply_user_id}").fetchone()
    balance = int(balance[0])
    balance2 = '{:,}'.format(balance)

    reply_user_name = cursor.execute(f"SELECT user_name from users where user_id = {reply_user_id}").fetchone()
    reply_user_name = str(reply_user_name[0])

    bank = cursor.execute(f"SELECT bank from users where user_id = {reply_user_id}").fetchone()
    bank = int(bank[0])
    bank3 = '{:,}'.format(bank)

    user_tg_name = message.reply_to_message.from_user.get_mention(as_html=True)

    reply_user_status = cursor.execute(f"SELECT user_status from users where user_id = {reply_user_id}").fetchone()
    reply_user_status = str(reply_user_status[0])

    ethereum = cursor.execute(f"SELECT ethereum from users where user_id = {reply_user_id}").fetchone()
    ethereum = int(ethereum[0])
    ethereum2 = '{:,}'.format(ethereum)

    rating = cursor.execute(f"SELECT rating from users where user_id = {reply_user_id}").fetchone()
    rating = int(rating[0])
    rating2 = '{:,}'.format(rating)

    status_block = cursor.execute(f"SELECT status_block from users where user_id = {reply_user_id}").fetchone()
    status_block = str(status_block[0])

    time_register = cursor.execute(f"SELECT time_register from users where user_id = {reply_user_id}").fetchone()
    time_register = time_register[0]

    pref = cursor.execute(f"SELECT pref from users where user_id = {reply_user_id}").fetchone()
    pref = str(pref[0])

    donate_coins = cursor.execute(f"SELECT donate_coins from users where user_id = {reply_user_id}").fetchone()
    donate_coins = int(donate_coins[0])
    donate_coins2 = '{:,}'.format(donate_coins)

    bank2 = cursor.execute(f"SELECT bank2 from users where user_id = {reply_user_id}").fetchone()
    bank2 = int(bank2[0])
    bank22 = '{:,}'.format(bank2)

    depozit = cursor.execute(f"SELECT depozit from users where user_id = {reply_user_id}").fetchone()
    depozit = int(depozit[0])
    depozit2 = '{:,}'.format(depozit)

    if user_status in ['Owner', 'Helper_Admin', 'Admin']:
       await message.reply( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные о <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> :

💬 | Телеграм: {user_tg_name}
🟢 | Статус: {reply_user_status}
🟩 | Статус блокировки: {status_block}

👤 | Ник: {reply_user_name}
💰 | Баланс: {balance2}$
🏪 | Банковский счёт: {bank3}$
🏪 | Хранительный счёт: {bank22}$
🏛 | Депозит: {depozit2}$
🟪 | Эфириум: {ethereum2} 🟣
💎 | Рейтинг: {rating2} 💎
🪙 | Donate-Coins: {donate_coins2} 🪙

📆 | Дата регистрации: {time_register}     
       """, parse_mode='html')
    else:
        await message.reply(f'❗️ Данная команда доступна от прав администратора <b>ADMIN</b>', parse_mode='html')

async def info_id_handler(message: Message):
    msg = message
    user_id = msg.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    

    user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_status = str(user_status[0])

    reply_user_id = int(message.text.split()[1])

    balance = cursor.execute(f"SELECT balance from users where user_id = {reply_user_id}").fetchone()
    balance = int(balance[0])
    balance2 = '{:,}'.format(balance)

    reply_user_name = cursor.execute(f"SELECT user_name from users where user_id = {reply_user_id}").fetchone()
    reply_user_name = str(reply_user_name[0])

    bank = cursor.execute(f"SELECT bank from users where user_id = {reply_user_id}").fetchone()
    bank = int(bank[0])
    bank3 = '{:,}'.format(bank)

    reply_user_status = cursor.execute(f"SELECT user_status from users where user_id = {reply_user_id}").fetchone()
    reply_user_status = str(reply_user_status[0])

    ethereum = cursor.execute(f"SELECT ethereum from users where user_id = {reply_user_id}").fetchone()
    ethereum = int(ethereum[0])
    ethereum2 = '{:,}'.format(ethereum)

    rating = cursor.execute(f"SELECT rating from users where user_id = {reply_user_id}").fetchone()
    rating = int(rating[0])
    rating2 = '{:,}'.format(rating)

    status_block = cursor.execute(f"SELECT status_block from users where user_id = {reply_user_id}").fetchone()
    status_block = str(status_block[0])

    time_register = cursor.execute(f"SELECT time_register from users where user_id = {reply_user_id}").fetchone()
    time_register = time_register[0]

    pref = cursor.execute(f"SELECT pref from users where user_id = {reply_user_id}").fetchone()
    pref = str(pref[0])

    donate_coins = cursor.execute(f"SELECT donate_coins from users where user_id = {reply_user_id}").fetchone()
    donate_coins = int(donate_coins[0])
    donate_coins2 = '{:,}'.format(donate_coins)

    bank2 = cursor.execute(f"SELECT bank2 from users where user_id = {reply_user_id}").fetchone()
    bank2 = int(bank2[0])
    bank22 = '{:,}'.format(bank2)

    depozit = cursor.execute(f"SELECT depozit from users where user_id = {reply_user_id}").fetchone()
    depozit = int(depozit[0])
    depozit2 = '{:,}'.format(depozit)

    if user_status != ['Owner', 'Helper_Admin', 'Admin']:
       user_status2 = 'Пользователь'
    if user_status in ['Owner', 'Helper_Admin']:
       await message.reply( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные о <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> :

💬 | Телеграм: <a href='tg://user?id={reply_user_id}'>Аккаунт</a>
🟢 | Статус: {reply_user_status}
🟩 | Статус блокировки: {status_block}

👤 | Ник: {reply_user_name}
💰 | Баланс: {balance2}$
🏪 | Банковский счёт: {bank3}$
🏪 | Хранительный счёт: {bank22}$
🏛 | Депозит: {depozit2}$
🟪 | Эфириум: {ethereum2} 🟣
💎 | Рейтинг: {rating2} 💎
🪙 | Donate-Coins: {donate_coins2} 🪙

📆 | Дата регистрации: {time_register}     
       """, parse_mode='html')
    else:
        await message.reply(f'❗️ Данная команда доступна от прав администратора <b>HELPER ADMIN</b>', parse_mode='html')


