from email.message import Message
from aiogram.types import message

from db import cursor, connect

async def balance_handler(message: Message):
    msg = message
    user_id = msg.from_user.id
    
    chat_id = message.chat.id
    pref = cursor.execute("SELECT pref from users where user_id = ?",(message.from_user.id,)).fetchone()
    pref = str(pref[0])

    avatarka = cursor.execute("SELECT avatarka from avatarka where user_id = ?",(message.from_user.id,)).fetchone()
    avatarka = avatarka[0]

    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
    balance = int(balance[0])
    balance2 = '{:,}'.format(balance)
    bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
    bank = int(bank[0])
    bank2 = '{:,}'.format(bank)
    ethereum = cursor.execute("SELECT ethereum from users where user_id = ?",(message.from_user.id,)).fetchone()
    ethereum = int(ethereum[0])
    ethereum2 = '{:,}'.format(ethereum)

    c = 999999999999999999999999999999999999999999999999999999999999999999
    if balance >= 999999999999999999999999999999999999999999999999999999999999999999:
        balance = 999999999999999999999999999999999999999999999999999999999999999999
        cursor.execute(f'UPDATE users SET balance = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
        connect.commit()
        balance2 = '{:,}'.format(balance) 
    else:
        pass
    if bank >= 999999999999999999999999999999999999999999999999999999999999999999:
        bank = 999999999999999999999999999999999999999999999999999999999999999999
        cursor.execute(f'UPDATE users SET bank = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
        connect.commit()
        bank2 = '{:,}'.format(bank)
    else:
        pass
    if ethereum >= 999999999999999999999999999999999999999999999999999999999999999999:
        ethereum = 999999999999999999999999999999999999999999999999999999999999999999
        cursor.execute(f'UPDATE users SET ethereum = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
        connect.commit()
        ethereum2 = '{:,}'.format(ethereum)
    else:
        pass

    if avatarka == 'apper':
        ava = open('apper.jpg', 'rb')
        await message.bot.send_photo(message.chat.id, ava, f"👫 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a> \n✏️ | Префикс: {pref} \n💰 | Деньги: {balance2}$ \n🏦 | Банк: {bank2}$\n🟣 | Эфириум: {ethereum2}🟪", parse_mode='html')
        return
    
    if avatarka == 'admin':
        ava = open('админ.jpg', 'rb')
        await message.bot.send_photo(message.chat.id, ava, f"👫 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a> \n✏️ | Префикс: {pref} \n💰 | Деньги: {balance2}$ \n🏦 | Банк: {bank2}$\n🟣 | Эфириум: {ethereum2}🟪", parse_mode='html')
        return
    
    if avatarka == 'girl':
        ava = open('girl.jpg', 'rb')
        await message.bot.send_photo(message.chat.id, ava, f"👫 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a> \n✏️ | Префикс: {pref} \n💰 | Деньги: {balance2}$ \n🏦 | Банк: {bank2}$\n🟣 | Эфириум: {ethereum2}🟪", parse_mode='html')
        return
    
    if avatarka == 'cheat':
        ava = open('cheat.jpg', 'rb')
        await message.bot.send_photo(message.chat.id, ava, f"👫 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a> \n✏️ | Префикс: {pref} \n💰 | Деньги: {balance2}$ \n🏦 | Банк: {bank2}$\n🟣 | Эфириум: {ethereum2}🟪", parse_mode='html')
        return
    
    if avatarka == 'dyp':
        ava = open('дюп.jpg', 'rb')
        await message.bot.send_photo(message.chat.id, ava, f"👫 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a> \n✏️ | Префикс: {pref} \n💰 | Деньги: {balance2}$ \n🏦 | Банк: {bank2}$\n🟣 | Эфириум: {ethereum2}🟪", parse_mode='html')
        return
    
    if avatarka == 'strach':
        ava = open('страж.jpg', 'rb')
        await message.bot.send_photo(message.chat.id, ava, f"👫 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a> \n✏️ | Префикс: {pref} \n💰 | Деньги: {balance2}$ \n🏦 | Банк: {bank2}$\n🟣 | Эфириум: {ethereum2}🟪", parse_mode='html')
        return


    await message.bot.send_message(message.chat.id, f"👫 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a> \n✏️ | Префикс: {pref} \n💰 | Деньги: {balance2}$ \n🏦 | Банк: {bank2}$\n🟣 | Эфириум: {ethereum2}🟪", parse_mode='html')
