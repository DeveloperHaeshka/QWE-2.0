from email.message import Message
from aiogram.types import message
from db import cursor, connect
import random
import time

async def bank_ograb_handler(message):
    u = message.text.split()[1]
    if u == 'банк':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       
       x = random.randint(1,3)
       period = 86400 #86400 s 24h
       get = cursor.execute("SELECT stavka_bank FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = int(get[0])
       stavkatime = time.time() - float(last_stavka)
       rx = random.randint(1000000,25000000)
       rx2 = '{:,}'.format(rx)
       if stavkatime > period:
          if int(x) in range(2,3):
             await message.bot.send_message(message.chat.id, f"🏦 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно ограбили банк на {rx2}$ ✅", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + rx} WHERE user_id ="{user_id}"')
             cursor.execute(f'UPDATE bot_time SET stavka_bank = {time.time()} WHERE user_id = "{user_id}"')
             connect.commit()
          else:
             await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам не удалось ограбить банк", parse_mode='html')
       else:
          await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ограбить банк можно раз в 24ч⏳", parse_mode='html')


async def bank_down_handler(message: Message):
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       name = msg.from_user.last_name
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       bank_s = int(msg.text.split()[2])
       print(f"{name} снял с банка: {bank_s}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_s)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       if bank_s > 0:
          if bank >= bank_s:
             await message.bot.send_message(message.chat.id,
                                    f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли с банковского счёта {bank2}$ {rwin}",
                                    parse_mode='html')
             cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"')
             connect.commit()

          elif int(bank) < int(bank_s):
             await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств на банковском счету! {rloser}",
                                    parse_mode='html')


async def bank_up_handler(message: Message):
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       name = msg.from_user.last_name
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       bank_p = int(msg.text.split()[2])

       if bank_p >= 999999999999999999999999999999999999999999999999999999999999999999:
          await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>,  нельзя ложить в банк больше лимита")
          return

       print(f"{name} положил в банк: {bank_p}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_p)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       period = 180
       get = cursor.execute(f"SELECT stavka FROM time_bank WHERE user_id = {user_id}").fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if bank_p > 0:
             if balance >= bank_p:
                await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно положили в банк {bank2}$ {rwin}",
                                        parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE time_bank SET stavka = {time.time()} WHERE user_id = {user_id}')
                connect.commit()

             elif int(balance) < int(bank_p):
                await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , недостаточно средств! {rloser}", parse_mode='html')

          if bank_p <= 0:
             await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , нельзя положить в банк отрицательное число! {rloser}",
                                     parse_mode='html')
       else:
          await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ложить в банк можно раз в 3 минуты", parse_mode='html')


async def depozit_handler(message: Message):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       i = str(msg.text.split()[1])
       summ = int(msg.text.split()[2])
       summ2 = '{:,}'.format(summ)

       user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_status = str(user_status[0])
       depozit = cursor.execute("SELECT depozit from users where user_id = ?", (message.from_user.id,)).fetchone()
       depozit = int(depozit[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       
       period = 259200 #259200s 3d
       get = cursor.execute("SELECT stavka_depozit FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if i == 'положить':
          if summ <= balance :
             if summ > 0:
                if stavkatime > period:
                   await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно положили на депозит {summ2}$ 🔐", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ}  WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET depozit = {depozit + summ}  WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE bot_time SET stavka_depozit = {time.time()}  WHERE user_id = {user_id}')
                   connect.commit()
                   return
                else:
                   await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , извините но ложить, снимать с депозита можно раз в 3 дня ⌛️", parse_mode='html')
             else:
                await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , нельзя ложить отрицательное число {rloser}", parse_mode='html')
          else:
             await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , недостаточно средств {rloser}", parse_mode='html')
       if i == 'снять':
          if summ <= depozit :
             if summ > 0:
                if stavkatime > period:
                   await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно сняли с депозита {summ2}$ 🔐", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance + summ}  WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE users SET depozit = {depozit - summ}  WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE bot_time SET stavka_depozit = {time.time()}  WHERE user_id = {user_id}')
                   connect.commit()
                   return
                else:
                   await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , извините но ложить, снимать с депозита можно раз в 3 дня ⌛️", parse_mode='html')
             else:
                await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , нельзя снимать отрицательное число {rloser}", parse_mode='html')
          else:
             await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , недостаточно средств {rloser}", parse_mode='html')
          


async def procent_handler(message: Message):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       i2 = str(msg.text.split()[1])
       summ = int(msg.text.split()[2])
       summ2 = '{:,}'.format(summ)

       user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
       user_status = str(user_status[0])
       depozit = cursor.execute("SELECT depozit from users where user_id = ?", (message.from_user.id,)).fetchone()
       depozit = int(depozit[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if user_status == 'Player':
          procent = '6%'
          i = 6
          stats_depozit = 'Обычный'
       if user_status == 'Vip':
          procent = '9%'
          i = 9
          stats_depozit = 'Вип'
       if user_status == 'Premium':
          procent = '13%'
          i = 13
          stats_depozit = 'Премиум'
       if user_status == 'Platina':
          procent = '17%'
          i = 17
          stats_depozit = 'Платина'
       if user_status == 'Helper':
          procent = '21%'
          i = 21
          stats_depozit = 'Хелпер'
       if user_status == 'Sponsor':
          procent = '24%'
          i = 24
          stats_depozit = 'Спонсор'
       if user_status == 'Osnovatel':
          procent = '27%'
          i = 27
          stats_depozit = 'Основатель'
       if user_status == 'Vladelec':
          procent = '29%'
          i = 29
          stats_depozit = 'Владелец'
       if user_status == 'Bog':
          procent = '32%'
          i = 32
          stats_depozit = 'Бог'
       if user_status == 'Vlaselin':
          procent = '36%'
          i = 36
          stats_depozit = 'Властелин'

       else:
          procent = '6%'
          i = 6
          stats_depozit = 'Обычный'
          
          money_vivod = depozit / i
          money_vivod2 = int(money_vivod)
          money_vivod3 = '{:,}'.format(money_vivod2)
       period = 259200 #259200s 3d
       get = cursor.execute("SELECT stavka_depozit FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if i2 == 'снять':
          if summ <= money_vivod2 :
             if summ > 0:
                if stavkatime > period:
                   await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно сняли проценты с депозита {summ2}$ 💵", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance + summ}  WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE bot_time SET stavka_depozit = {time.time()}  WHERE user_id = {user_id}')
                   connect.commit()
                   return
                else:
                   await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , извините но снимать с процентов депозита можно раз в 3 дня ⌛️", parse_mode='html')
             else:
                await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , нельзя снимать отрицательное число {rloser}", parse_mode='html')
          else:
             await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , недостаточно средств {rloser}", parse_mode='html')


async def bank_handler(message: Message):
    try:
        msg = message
        chat_id = message.chat.id
        
        user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_name = str(user_name[0])

        user_id = msg.from_user.id
        user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
        bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
        bank_hran = cursor.execute("SELECT bank2 from users where user_id = ?",(message.from_user.id,)).fetchone()
        bank = int(bank[0])
        balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
        balance = int(balance[0])
        depozit = cursor.execute("SELECT depozit from users where user_id = ?",(message.from_user.id,)).fetchone()
        depozit = int(depozit[0])
        bank_hran = int(bank_hran[0])
        bank_hran2 = '{:,}'.format(bank_hran)
        bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
        bank = int(bank[0])
        depozit2 = '{:,}'.format(depozit)
        bank2 = '{:,}'.format(bank)
        if user_status == 'Player':
            procent = '6%'
            i = 6
            stats_depozit = 'Обычный'
        if user_status == 'Vip':
            procent = '9%'
            i = 9
            stats_depozit = 'Вип'
        if user_status == 'Premium':
            procent = '13%'
            i = 13
            stats_depozit = 'Премиум'
        if user_status == 'Platina':
            procent = '17%'
            i = 17
            stats_depozit = 'Платина'
        if user_status == 'Helper':
            procent = '21%'
            i = 21
            stats_depozit = 'Хелпер'
        if user_status == 'Sponsor':
            procent = '24%'
            i = 24
            stats_depozit = 'Спонсор'
        if user_status == 'Osnovatel':
            procent = '27%'
            i = 27
            stats_depozit = 'Основатель'
        if user_status == 'Vladelec':
            procent = '29%'
            i = 29
            stats_depozit = 'Владелец'
        if user_status == 'Bog':
            procent = '32%'
            i = 32
            stats_depozit = 'Бог'
        if user_status == 'Vlaselin':
            procent = '36%'
            i = 36
            stats_depozit = 'Властелин'

        else:
            procent = '6%'
            i = 6
            stats_depozit = 'Обычный'
            
            money_vivod = depozit / i
            money_vivod2 = int(money_vivod)
            money_vivod3 = '{:,}'.format(money_vivod2)

        c = 999999999999999999999999999999999999999999999999999999999999999999
        if bank >= 999999999999999999999999999999999999999999999999999999999999999999:
            bank = 999999999999999999999999999999999999999999999999999999999999999999
            cursor.execute(f'UPDATE users SET bank = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            bank2 = '{:,}'.format(bank)
        else:
            pass
        if bank_hran >= 999999999999999999999999999999999999999999999999999999999999999999:
            bank_hran = 999999999999999999999999999999999999999999999999999999999999999999
            cursor.execute(f'UPDATE users SET bank2 = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            bank_hran2 = '{:,}'.format(bank_hran)
        else:
            pass
        if depozit >= 999999999999999999999999999999999999999999999999999999999999999999:
            depozit = 999999999999999999999999999999999999999999999999999999999999999999
            cursor.execute(f'UPDATE users SET depozit = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            depozit2 = '{:,}'.format(depozit)

        i = str(msg.text.split()[1])
        summ = int(msg.text.split()[2])


        if i in ['снять', "Снять"]:
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            bank2 = '{:,}'.format(summ)

            if summ > 0:
                if bank >= summ:
                    await message.bot.send_message(message.chat.id,
                                            f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли с банковского счёта {bank2}$ {rwin}",
                                            parse_mode='html')
                    cursor.execute(f'UPDATE users SET bank = {bank - summ} WHERE user_id = "{user_id}"')
                    cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
                    connect.commit()

                elif int(bank) < int(bank_s):
                    await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств на банковском счету! {rloser}",
                                            parse_mode='html')


        if i in ['Положить', "положить"]:
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            loser = ['😔', '😕', '😣', '😞', '😢']
            rloser = random.choice(loser)
            period = 180
            bank2 = '{:,}'.format(summ)
            get = cursor.execute(f"SELECT stavka FROM time_bank WHERE user_id = {user_id}").fetchone()
            last_stavka = f"{int(get[0])}"
            stavkatime = time.time() - float(last_stavka)
            if stavkatime > period:
                if summ > 0:
                    if balance >= summ:
                        await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно положили в банк {bank2}$ {rwin}",
                                                parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE users SET bank = {bank + summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE time_bank SET stavka = {time.time()} WHERE user_id = {user_id}')
                        connect.commit()

                    elif int(balance) < int(summ):
                        await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , недостаточно средств! {rloser}", parse_mode='html')

                if summ <= 0:
                    await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , нельзя положить в банк отрицательное число! {rloser}",
                                            parse_mode='html')
            else:
                await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ложить в банк можно раз в 3 минуты", parse_mode='html')
    except IndexError:
        await message.bot.send_message(message.chat.id,f"<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные о вашем банке 🏦\n\n👨‍💼 | Владелец: {user_name}\n🏛 | Основной счёт: {bank2}$\n💼 | Хранительный счёт: {bank_hran2}$\n🔐 | Деньги на депозите: {depozit2}$\n     💎 Статус депозита: {stats_depozit}\n     📈 Процент под депозит: {procent}\n      💵 Деньги на вывод: {money_vivod3}$", parse_mode='html')
