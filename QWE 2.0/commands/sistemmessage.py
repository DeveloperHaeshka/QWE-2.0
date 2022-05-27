from aiogram.types import message
from db import cursor, connect
import time

async def sistem_message_handler(message):
    try:
        text = ' '.join(message.text.split()[2:])

        msg = message
        user_id = msg.from_user.id
        user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_name = str(user_name[0])

        reply_user_id = int(message.text.split()[1])
        reply_user_name = cursor.execute(f"SELECT user_name from users where user_id = {reply_user_id}").fetchone()
        reply_user_name = str(reply_user_name[0])

        period = 5
        get = cursor.execute("SELECT stavka FROM time_sms WHERE user_id = ?", (message.from_user.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)

        if len(text) > 35:
            await message.reply(f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, сообщение не может быть более чем 35 символов ", parse_mode='html')
            return
        if stavkatime > period:
            await message.reply(user_id, f"💬 | [Я ➡️ <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>] {text}", parse_mode='html')
            await message.reply(reply_user_id, f"💬 | [<a href='tg://user?id={user_id}'>{user_name}</a> ➡️ Я] {text}", parse_mode='html')
            cursor.execute(f'UPDATE time_sms SET stavka = {time.time()} WHERE user_id = {user_id}')
            connect.commit()
            return
        else:
            await message.reply( f"🆘 | Игрок, сообщение писать можно раз в 5 секунд", parse_mode='html')
            return
    except:
        await message.reply( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! Либо вы не правильно ID, или данный игрок не играет в бота", parse_mode='html')
        return

