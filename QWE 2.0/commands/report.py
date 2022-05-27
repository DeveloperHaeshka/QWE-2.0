from email.message import Message
from aiogram.types import message
from db import cursor, connect


async def report_info_handler(message: Message):
       msg = message
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await message.bot.send_message(message.chat.id , f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот информация за систему репортов ⛔️

⚠️ | Правила по использованию репортов
      1️⃣ | Материться, оскорблять кого-либо, проявлять неуважение к администрации и тому подобное.
      2️⃣ | Капсить, писать неразборчиво, использовать спам, писать один и тот-же текст несколько раз получивши на него ответ.
      3️⃣ | Всячески дразнить администрацию и отвлекать от работы.
      4️⃣ | Запрещено интересоваться/писать вещи которые ни коем образом ни относятся к игре
      5️⃣ | Запрещена реклама в любом её проявлении
      6️⃣ | Запрещено обращаться к своим друзьям администраторам по личным вопросам
      7️⃣ | Запрещено клеветать на игроков, обвинять их в нарушениях, которые они не совершали.
      8️⃣ | Репорт работает по принципу - Вопрос/Просьба/Жалоба (исключение - Приветствие) и не иначе. Иные формы обращения будут оставаться без ответа и будет выдано наказание.

⚠️ | Форма отправки репорта - /report [сообщение]

⛔️Прошу вас соблюдать правила отправки репорта
       """, parse_mode='html')




async def report_handler(message: Message):
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_id = message.from_user.id

    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    text = message.text[7:]
    
    if text == '':
       await message.reply( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, репорт не может быть пустым", parse_mode='html')
       return
    rows = cursor.execute('SELECT user_id FROM users where user_status = "Helper_Admin"').fetchall()
    for row in rows:
       await message.bot.send_message(row[0], f"<b>🆘ВАМ ПРИШЁЛ РЕПОРТ🆘</b>\n👨 | Отправитель: <a href='tg://user?id={user_id}'>{user_name}</a>\n💬 |Сообщение: <i>{text}</i>", parse_mode='html')

    await message.bot.send_message(1887634547,f"""
<b>🆘ВАМ ПРИШЁЛ РЕПОРТ🆘</b>
👨 | Отправитель: <a href='tg://user?id={user_id}'>{user_name}</a>  
💬 |Сообщение: <i>{text}</i>
    """, parse_mode='html')  
    await message.reply(  f"✅ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш репорт был успешно отправлен администрации", parse_mode='html')
