from aiogram.types import message
from db import cursor, connect
from decimal import Decimal

async def top_handler(message):
       list = cursor.execute(f"SELECT * FROM users ORDER BY rating DESC").fetchmany(10)
       top_list = []
       user_id = message.from_user.id
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       num = 0

       

       for user in list:
           if user[7] >= 999999999999999999999999999999999999999999999999999999999999999999:
              c6 = 999999999999999999999999999999999999999999999999999999999999999999
           else:
              c6 = user[7]

           

           num += 1

           if num == 1:
              num2 = '1️⃣'
              num3 = ' <b>💎ТОП 1💎</b> |'
           if num == 2:
              num2 = '2️⃣'
              num3 = ''
           if num == 3:
              num2 = '3️⃣'
              num3 = ''
           if num == 4:
              num2 = '4️⃣'
              num3 = ''
           if num == 5:
              num2 = '5️⃣'
              num3 = ''
           if num == 6:
              num2 = '6️⃣'
              num3 = ''
           if num == 7:
              num2 = '7️⃣'
              num3 = ''
           if num == 8:
              num2 = '8️⃣'
              num3 = ''
           if num == 9:
              num2 = '9️⃣'
              num3 = ''
           if num == 10:
              num2 = '🔟'
              num3 = ''
           c = Decimal(c6)
           c2 = '{:,}'.format(c)

           if user[3] == 'Owner':
             stats = ' ✅<b>РАЗРАБОТЧИК</b>✅ |'
           if user[3] == 'Admin':
             stats = ' ⛔️<b>АДМИН</b>⛔️ |'
           if user[3] == 'Helper_Admin':
             stats = ' ⚠️<b>HELPER АДМИН</b>⚠️ |'
           if user[3] in ['Player', 'Vip', 'Premium', 'Platina', 'Helper', 'Sponsor', 'Osnovatel', 'Vladelec', 'Bog', 'Vlaselin']:
             stats = ''
           
           top_list.append(f"{num2}. {user[1]} |{stats}{num3} ID: <code>{user[0]}</code> |  — {c2}💎 ")
       top = "\n".join(top_list)
       await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, топ 10 игроков бота:\n" + top, parse_mode='html')
