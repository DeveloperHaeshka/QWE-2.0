from unittest import async_case
from aiogram.types import message
from db import cursor, connect
import time
import random
import config
from decimal import Decimal

async def coob_handler(message):
            try:
                user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
                user_name = user_name[0]
                user_id = message.from_user.id

                balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
                balance = int(balance[0])

                game = cursor.execute("SELECT game from users where user_id = ?", (message.from_user.id,)).fetchone()
                game = int(game[0])
                
                rx = random.randint(0,700)

                chil = int(message.text.split()[1])
                summ = int(message.text.split()[2])
                summ2 = '{:,}'.format(summ)
                
                
                
                summ_win = summ * 3
                summ_win2 = '{:,}'.format(summ_win)

                if balance >= 999999999999999999999999999999999999999999999999999999999999999999:
                    balance = 999999999999999999999999999999999999999999999999999999999999999999
                    cursor.execute(f'UPDATE users SET balance = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
                    connect.commit()
                    balance2 = '{:,}'.format(balance)

                period = 5
                get = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
                last_stavka = int(get[0])
                stavkatime = time.time() - float(last_stavka)
                if chil <= 6:
                    if summ <= balance:
                        if stavkatime > period:
                            if int(rx) in range(0,100):
                                if chil == 1:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲1 - {summ2}$\n🧾 | Выигрыш: 🎲1 - {summ_win2}$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET balance = {balance + summ_win}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                                else:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲{chil} - {summ2}$\n🧾 | Выигрыш: 🎲1 - 0$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                            if int(rx) in range(101,200):
                                if chil == 2:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲2 - {summ2}$\n🧾 | Выигрыш: 🎲2 - {summ_win2}$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET balance = {balance + summ_win}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                                else:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲{chil} - {summ2}$\n🧾 | Выигрыш: 🎲2 - 0$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                            if int(rx) in range(201,300):
                                if chil == 3:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲3 - {summ2}$\n🧾 | Выигрыш: 🎲3 - {summ_win2}$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET balance = {balance + summ_win}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                                else:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲{chil} - {summ2}$\n🧾 | Выигрыш: 🎲3 - 0$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                            if int(rx) in range(401,500):
                                if chil == 4:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲4 - {summ2}$\n🧾 | Выигрыш: 🎲4 - {summ_win2}$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET balance = {balance + summ_win}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                                else:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲{chil} - {summ2}$\n🧾 | Выигрыш: 🎲4 - 0$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                            if int(rx) in range(501,600):
                                if chil == 5:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲5 - {summ2}$\n🧾 | Выигрыш: 🎲5 - {summ_win2}$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET balance = {balance + summ_win}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                                else:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲{chil} - {summ2}$\n🧾 | Выигрыш: 🎲5 - 0$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                            if int(rx) in range(601,700):
                                if chil == 6:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲6 - {summ2}$\n🧾 | Выигрыш: 🎲6 - {summ_win2}$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET balance = {balance + summ_win}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1}  WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                                else:
                                    await message.bot.send_message(message.chat.id, f"🤵‍♂ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🎲 | Игра: Кубик\n🎟 | Ставка: 🎲{chil} - {summ2}$\n🧾 | Выигрыш: 🎲6 - 0$", parse_mode='html')
                                    cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE users SET game = {game + 1} WHERE user_id = "{user_id}"')
                                    cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()}  WHERE user_id = "{user_id}"')
                                    connect.commit()
                        else:
                            await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Играть можно раз в 5 секунд", parse_mode='html')
                    else:
                        await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нехватает средств!", parse_mode='html')
                else:
                    await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данного числа нету в кубике!", parse_mode='html')
            except IndexError:
                await message.bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Ошибка! Пример Кубик 6 1000", parse_mode='html')

