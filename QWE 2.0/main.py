# -*-coding: utf-8 -*-
from aifc import Error
import logging
from ntpath import join
from colorama import Fore, Back, Style
from os import times
import sqlite3
import random
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import quote_html
from datetime import datetime, timedelta
from decimal import Decimal
from time import gmtime
from time import strptime
import asyncio
from bs4 import BeautifulSoup
import requests
from pycoingecko import CoinGeckoAPI

import config
import db
from db import cursor, connect
from triggers import Trigger

from commands.user.balance import balance_handler
from commands.user.games.gamevb import gamevb_handler, gamevb_callback_handler, gamevb_info_handler
from commands.sistemmessage import sistem_message_handler
from commands.admin.info import info_handler, info_id_handler
from commands.admin.chat.mute import mute_handler, unmute_handler
from commands.admin.chat.ban import ban_handler, unban_handler
from commands.report import report_handler, report_info_handler
from commands.admin.warn import unwarn_handler, unwarn_id_handler, warn_hendler, warn_id_hendler
from commands.admin.chat.channel_help import help_chat_admin_handler
from commands.admin.reset import reset_handler, reset_id_handler, obnyl_handler
from commands.admin.ban import unban_id_handler, unban_handler, ban_id_handler, ban_handler
from commands.start import start_handler
from commands.user.profile import profile_handler
from commands.user.bank import bank_down_handler, bank_up_handler, depozit_handler, procent_handler, bank_handler, bank_ograb_handler
from commands.admin.podel import podel_handler
from commands.admin.donat import donat_handler
from commands.admin.prava import per_prava_handler, off_prava_handler, v_helper_handler, v_admin_handler
from commands.admin.admins import admin_menu_handler
from commands.admin.ymnozh import ymnozh_handler
from commands.admin.vidach import vidach_handler
from commands.admin.zabrach import zabrach_handler
from commands.pravila import pravila_hendler
from commands.help import help_handler
from commands.user.games.spin import spin_handler
from commands.user.games.football import football_info_handler, football_handler
from commands.user.games.casino import casino_handler
from commands.user.games.plinko import plinko_handler
from commands.user.rating import rating_up_handler, rating_down_handler, rating_handler
from commands.user.peredach import dach_handler, peredach_handler
from commands.user.top import top_handler
from commands.user.nick import smena_nick_handler, smena_info_nick_handler
from commands.user.eth import eth_handler
from commands.user.bonus import bonus_handler
from commands.user.games.coob import coob_handler
from commands.user.games.chetnechet import chet_handler, nechet_handler
from commands.user.games.dice import wheel_handler, dice_handler


print(Fore.BLACK + Back.WHITE + """
-----------------------------------
| Разработчик: Хаешка             |
| Контакты разработчика:          |
|     Telegram: @haeshka_qwe      |
|     Instagram: @varseev.fx      |
-----------------------------------
|  Скрипт TG BOT: @qwegamebot     |
-----------------------------------

Запуск бота:


""")


logging.basicConfig(level=logging.INFO)

api = CoinGeckoAPI()

bot = Bot(token=config.token[1])
dp = Dispatcher(bot)


dp.register_message_handler(
        wheel_handler, Trigger(['wheel'])
)

dp.register_message_handler(
        dice_handler, Trigger(['dice'])
)

dp.register_message_handler(
        nechet_handler, Trigger(['нечётное', "нечетное"])
)

dp.register_message_handler(
        chet_handler, Trigger(['чётное', "четное"])
)

dp.register_message_handler(
        coob_handler, Trigger(['Кубик'])
)

dp.register_message_handler(
        bonus_handler, Trigger(['ежедневный'])
)

dp.register_message_handler(
        bank_ograb_handler, Trigger(['ограбить'])
)


dp.register_message_handler(
        eth_handler, Trigger(['эфириум'])
)

dp.register_message_handler(
        smena_nick_handler, Trigger(['+ник'])
)

dp.register_message_handler(
        smena_info_nick_handler, Trigger(['сменить ник'])
)

dp.register_message_handler(
        top_handler, Trigger(['топ'])
)

dp.register_message_handler(
        dach_handler, Trigger(['дать'])
)

dp.register_message_handler(
        peredach_handler, Trigger(['передать'])
)

dp.register_message_handler(
        rating_down_handler, Trigger(['-рейтинг'])
)

dp.register_message_handler(
        rating_up_handler, Trigger(['+рейтинг'])
)

dp.register_message_handler(
        rating_handler, Trigger(['рейтинг'])
)

dp.register_message_handler(
        plinko_handler, Trigger(['плинко'])
)

dp.register_message_handler(
        casino_handler, Trigger(['казино'])
)

dp.register_message_handler(
        football_info_handler, Trigger(['футбол'])
)

dp.register_message_handler(
        football_handler, Trigger(['фб'])
)

dp.register_message_handler(
        gamevb_info_handler, Trigger(['вб'])
)

dp.register_message_handler(
        spin_handler, Trigger(['спин'])
)

dp.register_message_handler(
        help_handler, commands=['help']
)


dp.register_message_handler(
        help_handler, Trigger(["помощь"])
)


dp.register_message_handler(
        obnyl_handler, Trigger(["обнулить"])
)

dp.register_message_handler(
        pravila_hendler, Trigger(["правила"])
)

dp.register_message_handler(
        zabrach_handler, Trigger(["забрать", '-'])
)

dp.register_message_handler(
        vidach_handler, Trigger(["выдать", '+'])
)

dp.register_message_handler(
        ymnozh_handler, Trigger(["умножить", '*'])
)

dp.register_message_handler(
        admin_menu_handler, Trigger(["админ"])
)

dp.register_message_handler(
        v_helper_handler, Trigger(["+хелпер"])
)

dp.register_message_handler(
        v_admin_handler, Trigger(["+админ"])
)

dp.register_message_handler(
        per_prava_handler, Trigger(["+права"])
)

dp.register_message_handler(
        off_prava_handler, Trigger(["-права"])
)

dp.register_message_handler(
        donat_handler, Trigger(["+донат"])
)

dp.register_message_handler(
        podel_handler, Trigger(["поделить"])
)

dp.register_message_handler(
        depozit_handler, Trigger(["депозит"])
)

dp.register_message_handler(
        procent_handler, Trigger(["процент"])
)

dp.register_message_handler(
        bank_handler, Trigger(["банк"])
)

dp.register_message_handler(
        report_info_handler, Trigger(["report", "репорт"])
)


dp.register_message_handler(
        profile_handler, Trigger(["п", "профиль"])
)

dp.register_message_handler(
        balance_handler, Trigger(["б", "баланс", "balance", "b"])
)

dp.register_callback_query_handler(
        gamevb_callback_handler, text="gamevb"
)

dp.register_message_handler(
        unban_id_handler, commands=['unban_id']
)

dp.register_message_handler(
        unban_handler, commands=['unban']
)

dp.register_message_handler(
        ban_id_handler, commands=['ban_id']
)

dp.register_message_handler(
        ban_handler, commands=['ban']
)

dp.register_message_handler(
        reset_id_handler, commands=['reset_id']
)

dp.register_message_handler(
        reset_handler, commands=['reset']
)

dp.register_message_handler(
        help_chat_admin_handler, commands=['help_admins']
)

dp.register_message_handler(
        warn_id_hendler, commands=['warn_id']
)

dp.register_message_handler(
        unwarn_id_handler, commands=['unwarn_id']
)

dp.register_message_handler(
        unwarn_handler, commands=['unwarn']
)

dp.register_message_handler(
        warn_hendler, commands=['warn']
)

dp.register_message_handler(
        unban_handler, commands=['channel_unban', 'unkick'], is_chat_admin=True
)

dp.register_message_handler(
        ban_handler, commands=['channel_ban', 'kick'], is_chat_admin=True
)

dp.register_message_handler(
        unmute_handler, commands=['channel_unmute', 'unmute'], is_chat_admin=True
)

dp.register_message_handler(
        mute_handler, commands=['channel_mute', 'mute'], is_chat_admin=True
)

dp.register_message_handler(
        info_id_handler, commands=['info_id']
)

dp.register_message_handler(
        info_handler, commands=['info']
)

dp.register_message_handler(
        sistem_message_handler, commands=['m']
)

dp.register_message_handler(
        gamevb_handler, commands=['gamevb', 'vb']
)

dp.register_message_handler(
        report_handler, commands=['report']
)

dp.register_message_handler(
        start_handler, commands=['start']
)
											
@dp.message_handler()
async def prof_user(message: types.Message):
    msg = message
    user_id = msg.from_user.id
    full_name = msg.from_user.full_name
    user_name = 'Игрок'
    user_status = "Player"
    status_block = 'off'
    stats_status = 'off'
    pref = 'Игрок'
    chat_id = message.chat.id
    result = time.localtime()
    status_console = 'off'
    avatarka_start = 'none'
    klan_index = 0
    status_family = 0

    if int(result.tm_mon) <= 9:
      p = "0"
    else:
      p = ''
    times = f'{result.tm_mday}.{p}{result.tm_mon}.{result.tm_year} | {result.tm_hour}:{result.tm_min}:{result.tm_sec}'
    times2 = str(times)

    cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
       cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (user_id, user_name, full_name, user_status, 10000, 0, 0, 0, status_block, times2, pref, 0, 0, 0, 0, stats_status))
       cursor.execute("INSERT INTO mine VALUES(?, ?, ?, ?, ?, ?, ?, ?);",(user_id, full_name,status_block, 0, 0, 0, 0, 0))
       cursor.execute("INSERT INTO farm VALUES(?, ?, ?, ?, ?);",(user_id, full_name,status_block, 0, 0))
       cursor.execute("INSERT INTO house VALUES(?, ?, ?, ?);",(user_id, user_name, 0, 0))
       cursor.execute("INSERT INTO cars VALUES(?, ?, ?, ?, ?);",(user_id, user_name, 0, 0, 0))
       cursor.execute("INSERT INTO user_case VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO bot_time VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", (user_id, 0, 0, 0, 0, 0, 0, 0, 0))
       cursor.execute("INSERT INTO promo1 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO warn VALUES(?, ?);",(user_id, 0))
       cursor.execute("INSERT INTO time_bank VALUES(?, ?);",(user_id, 0))
       cursor.execute("INSERT INTO ob_time VALUES(?, ?);",(user_id, 0))
       cursor.execute("INSERT INTO warn VALUES(?, ?);",(user_id, 0))
       cursor.execute("INSERT INTO time_prefix VALUES(?, ?);",(user_id, 0))
       cursor.execute("INSERT INTO time_sms VALUES(?, ?);",(user_id, 0))
       cursor.execute("INSERT INTO promo1 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO channel_pov VALUES(?, ?);",(user_id, 0))
       cursor.execute("INSERT INTO avatarka VALUES(?, ?);",(user_id, avatarka_start))
       cursor.execute("INSERT INTO reput VALUES(?, ?);",(user_id, 0))
       cursor.execute("INSERT INTO h_module VALUES(?, ?);",(user_id, 0))
       cursor.execute("INSERT INTO promo2 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo3 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo4 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo5 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo6 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo7 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo8 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo9 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo10 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo11 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo12 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo13 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo14 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo15 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo16 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo17 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo18 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo19 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo20 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo21 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo22 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo23 VALUES(?, ?, ?);",(user_id, 0, 0))
       connect.commit()
       print(f'Зарегестрировался в боте пользователь: {full_name}')
       reg = InlineKeyboardMarkup(row_width=1)
       register_help = InlineKeyboardButton(text='🆘 Помощь', callback_data='register_help')
       reg.add(register_help)

       name = message.from_user.get_mention(as_html=True)
       await bot.send_message(message.chat.id, f'''
👋 Привет, {name} 
Я бот для игры в различные игры.
Тебе выдан подарок в размере 10.000$.
Так же ты можешь добавить меня в беседу для игры с друзьями.
🆘 Чтобы узнать все команды введи "Помощь"
    ''', reply_markup=reg, parse_mode='html')
    else:
       status_console = 'off'
       avatarka_start = 'none'
       klan_index = 0
       status_family = 0
       cursor.execute("INSERT INTO promo24 VALUES(?, ?, ?);",(user_id, 0, 0))
       cursor.execute("INSERT INTO promo25 VALUES(?, ?, ?);",(user_id, 0, 0))
       connect.commit()
       
    
    

    
    
   
    

    status_block = cursor.execute("SELECT status_block from users where user_id = ?",(message.from_user.id,)).fetchone()
    status_block = str(status_block[0])

    if status_block == 'on':
       return

    if message.forward_date != None:
       msg = message
       user_id = msg.from_user.id
       
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , в боте запрещено пересылать сообщение!", parse_mode='html')
       return


    period = 2
    get = cursor.execute("SELECT stavka FROM ob_time WHERE user_id = ?",(message.from_user.id,)).fetchone()
    last_stavka = f"{int(get[0])}"
    stavkatime = time.time() - float(last_stavka)
    if stavkatime < period:
       return
    else:
       user_id = message.from_user.id
       cursor.execute(f'UPDATE ob_time SET stavka = {time.time()} WHERE user_id = {user_id}')
       connect.commit()



































############################################################ШАХТА############################################################
    if message.text.lower() == 'шахта':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       await bot.send_message(message.chat.id,f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот информация за шахту ⛏

⛏ | Руды на шахте:
      🪨 | Камень -  40%
      ⛓ | Железо - 30%
      🪙 | Серебро - 15%
      🎇 | Бронза - 10%
      ⚜️ | Золото - 5%

ℹ️ | Чтобы продать какую руду , воспользуйтесь командой \"Продать [Руда] [Количество]\"
ℹ️ | Чтобы копать руду воспользуйтесь командой \"Копать руду\"       
       """, parse_mode='html')
    if message.text.startswith('продать'):
      try:
         user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
         user_name = user_name[0]
         user_id = message.from_user.id

         balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
         balance = int(balance[0])

         # iron, silver, bronza, gold
         iron = cursor.execute("SELECT iron from mine where user_id = ?", (message.from_user.id,)).fetchone()
         iron = int(iron[0])
         
         metall = cursor.execute("SELECT metall from mine where user_id = ?", (message.from_user.id,)).fetchone()
         metall = int(metall[0])

         silver = cursor.execute("SELECT silver from mine where user_id = ?", (message.from_user.id,)).fetchone()
         silver = int(silver[0])

         bronza = cursor.execute("SELECT bronza from mine where user_id = ?", (message.from_user.id,)).fetchone()
         bronza = int(bronza[0])

         gold = cursor.execute("SELECT gold from mine where user_id = ?", (message.from_user.id,)).fetchone()
         gold = int(gold[0])

         rud = str(message.text.split()[1])

         c = int(message.text.split()[2])

         summ = c * 25000
         summ2 = '{:,}'.format(summ)
         if rud == 'камень':
            if c <= iron:
               summ = c * 25000
               summ2 = '{:,}'.format(summ)
               await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c} камень 🪨 за {summ2}$", parse_mode='html')
               cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
               cursor.execute(f'UPDATE mine SET iron = {iron - c} WHERE user_id = "{user_id}"')
               connect.commit()
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько руды!", parse_mode='html')
         if rud == 'железо':
            if c <= metall:
               summ = c * 45000
               summ2 = '{:,}'.format(summ)
               await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c} железо ⛓ за {summ2}$", parse_mode='html')
               cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
               cursor.execute(f'UPDATE mine SET metall = {metall - c} WHERE user_id = "{user_id}"')
               connect.commit()
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько руды!", parse_mode='html')

         if rud == 'серебро':
            if c <= silver:
               summ = c * 125000
               summ2 = '{:,}'.format(summ)
               await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c} серебро 🪙 за {summ2}$", parse_mode='html')
               cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
               cursor.execute(f'UPDATE mine SET silver = {silver - c} WHERE user_id = "{user_id}"')
               connect.commit()
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько руды!", parse_mode='html')
         if rud == 'бронзу':
            if c <= bronza:
               summ = c * 200000
               summ2 = '{:,}'.format(summ)
               await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c} бронзы 🎇 за {summ2}$", parse_mode='html')
               cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
               cursor.execute(f'UPDATE mine SET bronza = {bronza - c} WHERE user_id = "{user_id}"')
               connect.commit()
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько руды!", parse_mode='html')

         if rud == 'золото':
            if c <= gold:
               summ = c * 500000
               summ2 = '{:,}'.format(summ)
               await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c} золото ⚜️ за {summ2}$", parse_mode='html')
               cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
               cursor.execute(f'UPDATE mine SET bronza = {bronza - c} WHERE user_id = "{user_id}"')
               connect.commit()
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько руды!", parse_mode='html')
      except IndexError:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Ошибка! Пример: Продать [камень, железо, серебро, бронзу, золото, лён, хлопок] 1", parse_mode='html')

    if message.text.startswith('Продать'):
      try:
         user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
         user_name = user_name[0]
         user_id = message.from_user.id

         balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
         balance = int(balance[0])

         # iron, silver, bronza, gold
         iron = cursor.execute("SELECT iron from mine where user_id = ?", (message.from_user.id,)).fetchone()
         iron = int(iron[0])
         
         metall = cursor.execute("SELECT metall from mine where user_id = ?", (message.from_user.id,)).fetchone()
         metall = int(metall[0])

         silver = cursor.execute("SELECT silver from mine where user_id = ?", (message.from_user.id,)).fetchone()
         silver = int(silver[0])

         bronza = cursor.execute("SELECT bronza from mine where user_id = ?", (message.from_user.id,)).fetchone()
         bronza = int(bronza[0])

         gold = cursor.execute("SELECT gold from mine where user_id = ?", (message.from_user.id,)).fetchone()
         gold = int(gold[0])

         rud = str(message.text.split()[1])

         c = int(message.text.split()[2])

         summ = c * 25000
         summ2 = '{:,}'.format(summ)
         if rud == 'камень':
            if c <= iron:
               summ = c * 25000
               summ2 = '{:,}'.format(summ)
               await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c} камень 🪨 за {summ2}$", parse_mode='html')
               cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
               cursor.execute(f'UPDATE mine SET iron = {iron - c} WHERE user_id = "{user_id}"')
               connect.commit()
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько руды!", parse_mode='html')
         if rud == 'железо':
            if c <= metall:
               summ = c * 45000
               summ2 = '{:,}'.format(summ)
               await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c} железо ⛓ за {summ2}$", parse_mode='html')
               cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
               cursor.execute(f'UPDATE mine SET metall = {metall - c} WHERE user_id = "{user_id}"')
               connect.commit()
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько руды!", parse_mode='html')

         if rud == 'серебро':
            if c <= silver:
               summ = c * 125000
               summ2 = '{:,}'.format(summ)
               await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c} серебро 🪙 за {summ2}$", parse_mode='html')
               cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
               cursor.execute(f'UPDATE mine SET silver = {silver - c} WHERE user_id = "{user_id}"')
               connect.commit()
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько руды!", parse_mode='html')
         if rud == 'бронзу':
            if c <= bronza:
               summ = c * 200000
               summ2 = '{:,}'.format(summ)
               await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c} бронзы 🎇 за {summ2}$", parse_mode='html')
               cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
               cursor.execute(f'UPDATE mine SET bronza = {bronza - c} WHERE user_id = "{user_id}"')
               connect.commit()
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько руды!", parse_mode='html')

         if rud == 'золото':
            if c <= gold:
               summ = c * 500000
               summ2 = '{:,}'.format(summ)
               await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c} золото ⚜️ за {summ2}$", parse_mode='html')
               cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
               cursor.execute(f'UPDATE mine SET gold = {gold - c} WHERE user_id = "{user_id}"')
               connect.commit()
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько руды!", parse_mode='html')
      except IndexError:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Ошибка! Пример: Продать [камень, железо, серебро, бронзу, золото, лён, хлопок] 1", parse_mode='html')

    if message.text.lower() == 'копать руду':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       pick = cursor.execute("SELECT pick from mine where user_id = ?", (message.from_user.id,)).fetchone()
       pick = pick[0]

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       rx = random.randint(0,100)

      # iron, silver, bronza, gold
       iron = cursor.execute("SELECT iron from mine where user_id = ?", (message.from_user.id,)).fetchone()
       iron = int(iron[0])
       
       metall = cursor.execute("SELECT metall from mine where user_id = ?", (message.from_user.id,)).fetchone()
       metall = int(metall[0])

       silver = cursor.execute("SELECT silver from mine where user_id = ?", (message.from_user.id,)).fetchone()
       silver = int(silver[0])

       bronza = cursor.execute("SELECT bronza from mine where user_id = ?", (message.from_user.id,)).fetchone()
       bronza = int(bronza[0])

       gold = cursor.execute("SELECT gold from mine where user_id = ?", (message.from_user.id,)).fetchone()
       gold = int(gold[0])
       
       rx_iron = random.randint(15,20)
       rx_metall = random.randint(10,15)
       rx_silver = random.randint(5,10)
       rx_bronza = random.randint(0,5)
       
       if pick == 'Cherick':
          period = 3
       else:
          period = 5
       get = cursor.execute("SELECT time_pick FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = int(get[0])
       stavkatime = time.time() - float(last_stavka)

       if pick == 'Cherick':
          if stavkatime > period:
             if int(rx) in range(0,40):
                await bot.send_message(message.chat.id, f"🪨 | Вы успешно выкопали {rx_iron * 2} камня", parse_mode='html')
                cursor.execute(f'UPDATE mine SET iron = {iron + rx_iron * 2} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(41,70):
                await bot.send_message(message.chat.id, f"⛓ | Вы успешно выкопали {rx_metall * 2} железа", parse_mode='html')
                cursor.execute(f'UPDATE mine SET metall = {metall + rx_metall * 2} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(71,85):
                await bot.send_message(message.chat.id, f"🪙 | Вы успешно выкопали {rx_silver * 2} серебра", parse_mode='html')
                cursor.execute(f'UPDATE mine SET silver = {silver + rx_silver * 2} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(86,95):
                await bot.send_message(message.chat.id, f"🎇 | Вы успешно выкопали {rx_bronza * 2} бронзы", parse_mode='html')
                cursor.execute(f'UPDATE mine SET bronza = {bronza + rx_bronza * 2} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(96,100):
                await bot.send_message(message.chat.id, f"⚜️ | Вы успешно выкопали 2 золото", parse_mode='html')
                cursor.execute(f'UPDATE mine SET gold = {gold + 2} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! собирать руду можно раз в {period} секунд!", parse_mode='html')
             return

       if pick == 'Zerro':
          if stavkatime > period:
             if int(rx) in range(0,40):
                await bot.send_message(message.chat.id, f"🪨 | Вы успешно выкопали {rx_iron * 2} камня", parse_mode='html')
                cursor.execute(f'UPDATE mine SET iron = {iron + rx_iron * 2} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(41,70):
                await bot.send_message(message.chat.id, f"⛓ | Вы успешно выкопали {rx_metall * 2} железа", parse_mode='html')
                cursor.execute(f'UPDATE mine SET metall = {metall + rx_metall * 2} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(71,85):
                await bot.send_message(message.chat.id, f"🪙 | Вы успешно выкопали {rx_silver * 2} серебра", parse_mode='html')
                cursor.execute(f'UPDATE mine SET silver = {silver + rx_silver * 2} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(86,95):
                await bot.send_message(message.chat.id, f"🎇 | Вы успешно выкопали {rx_bronza * 2} бронзы", parse_mode='html')
                cursor.execute(f'UPDATE mine SET bronza = {bronza + rx_bronza * 2} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(96,100):
                await bot.send_message(message.chat.id, f"⚜️ | Вы успешно выкопали 2 золото", parse_mode='html')
                cursor.execute(f'UPDATE mine SET gold = {gold + 2} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! собирать руду можно раз в {period} секунд!", parse_mode='html')
             return

       if pick == 'on':
          if stavkatime > period:
             if int(rx) in range(0,40):
                await bot.send_message(message.chat.id, f"🪨 | Вы успешно выкопали {rx_iron} камня", parse_mode='html')
                cursor.execute(f'UPDATE mine SET iron = {iron + rx_iron} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(41,70):
                await bot.send_message(message.chat.id, f"⛓ | Вы успешно выкопали {rx_metall} железа", parse_mode='html')
                cursor.execute(f'UPDATE mine SET metall = {metall + rx_metall} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(71,85):
                await bot.send_message(message.chat.id, f"🪙 | Вы успешно выкопали {rx_silver} серебра", parse_mode='html')
                cursor.execute(f'UPDATE mine SET silver = {silver + rx_silver} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(86,95):
                await bot.send_message(message.chat.id, f"🎇 | Вы успешно выкопали {rx_bronza} бронзы", parse_mode='html')
                cursor.execute(f'UPDATE mine SET bronza = {bronza + rx_bronza} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
             if int(rx) in range(96,100):
                await bot.send_message(message.chat.id, f"⚜️ | Вы успешно выкопали 1 золото", parse_mode='html')
                cursor.execute(f'UPDATE mine SET gold = {gold + 1} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE bot_time SET time_pick = {time.time()} WHERE user_id = "{user_id}"')
                connect.commit()
                return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! собирать руду можно раз в {period} секунд!", parse_mode='html')
             return
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! у вас нету кирки, что бы купить кирку введите команду \"Купить кирку\"", parse_mode='html')
          return
          




    if message.text.lower() == 'продать кирку':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       
       pick = cursor.execute("SELECT pick from mine where user_id = ?", (message.from_user.id,)).fetchone()
       pick = pick[0]

       if pick == 'Cherick':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! вы не можете продать кирку Cherick", parse_mode='html')

       if pick == 'Zerro':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! вы не можете продать кирку Zerro", parse_mode='html')

       if pick == 'off':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! у вас и так нету кирки, что бы купить кирку введите команду \"Купить кирку\"", parse_mode='html')

       if pick == 'on':
          await bot.send_message(message.chat.id, f"⛏ | Вы продали кирку за 5.000$ ", parse_mode='html')
          cursor.execute(f'UPDATE mine SET pick = "off" WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET balance = {balance + 5000} WHERE user_id = "{user_id}"')
          connect.commit()
    if message.text.lower() == 'купить кирку':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       
       pick = cursor.execute("SELECT pick from mine where user_id = ?", (message.from_user.id,)).fetchone()
       pick = pick[0]


       if pick == 'Cherick':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! у вас уже есть кирка Cherick", parse_mode='html')

       if pick == 'Zerro':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! у вас уже есть кирка Zerro", parse_mode='html')


       if pick == 'on':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! у вас уже есть кирка, что бы продать кирку введите команду \"Продать кирку\"", parse_mode='html')

       if pick == 'off':
          if balance >= 5000:
             await bot.send_message(message.chat.id, f"⛏ | Вы купили кирку за 5.000$ ", parse_mode='html')
             cursor.execute(f'UPDATE mine SET pick = "on" WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET balance = {balance - 5000} WHERE user_id = "{user_id}"')
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас не хватает средств!", parse_mode='html')



#################################################ФЕРМА#################################################
    if message.text.lower() in ['ферма', 'фермы']:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id 

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот информация за ферму 🌾

🌾 | Доступный урожай:
      🍃 | Лён =  5-10
      🌿 | Хлопок = 5-10

ℹ️ | Чтобы собрать какой то урожай, воспользуйтесь командой \"Собрать [лён\ хлопок]
ℹ️ | Чтобы продать какой-то урожай, воспользуйтесь командой \" Продать [лён\хлопок] [Количество]       
       """, parse_mode='html')
    if message.text.startswith('продать хлопок'):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       
       cotton = cursor.execute("SELECT cotton from farm where user_id = ?", (message.from_user.id,)).fetchone()
       cotton = int(cotton[0])
       
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       c = int(message.text.split()[2])
       c2 = '{:,}'.format(c)
       
       summ = c * 150000
       summ2 = '{:,}'.format(summ)

       if c <= cotton:
          await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c2} хлопка 🌿 за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE farm SET cotton = {cotton - с} WHERE user_id = "{user_id}"')
          connect.commit()
       else:
          await bot.send_message(message.chat.id,f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько ресурсов!", parse_mode='html')

    if message.text.startswith('Продать хлопок'):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       
       cotton = cursor.execute("SELECT cotton from farm where user_id = ?", (message.from_user.id,)).fetchone()
       cotton = int(cotton[0])
       
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       c = int(message.text.split()[2])
       c2 = '{:,}'.format(c)
       
       summ = c * 150000
       summ2 = '{:,}'.format(summ)

       if c <= cotton:
          await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c2} хлопка 🌿 за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE farm SET cotton = {cotton - с} WHERE user_id = "{user_id}"')
          connect.commit()
       else:
          await bot.send_message(message.chat.id,f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько ресурсов!", parse_mode='html')


    if message.text.startswith('продать лён'):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       
       linen = cursor.execute("SELECT linen from farm where user_id = ?", (message.from_user.id,)).fetchone()
       linen = int(linen[0])
       
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       c = int(message.text.split()[2])
       c2 = '{:,}'.format(c)
       
       summ = c * 150000
       summ2 = '{:,}'.format(summ)

       if c <= linen:
          await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c2} лён 🍃 за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE farm SET linen = {linen - с} WHERE user_id = "{user_id}"')
          connect.commit()
       else:
          await bot.send_message(message.chat.id,f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько ресурсов!", parse_mode='html')

    if message.text.startswith('Продать лён'):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       
       linen = cursor.execute("SELECT linen from farm where user_id = ?", (message.from_user.id,)).fetchone()
       linen = int(linen[0])
       
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       colic = int(message.text.split()[2])
       c2 = '{:,}'.format(colic)
       
       summ = c * 150000
       summ2 = '{:,}'.format(summ)

       if colic <= linen:
          await bot.send_message(message.chat.id, f"💸 | Вы успешно продали {c2} лён 🍃 за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE farm SET linen = {linen - colic} WHERE user_id = "{user_id}"')
          connect.commit()
       else:
          await bot.send_message(message.chat.id,f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету столько ресурсов!", parse_mode='html')
    
    
    if message.text.startswith('cобрать'):
       try:
         user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
         user_name = user_name[0]
         user_id = message.from_user.id

         rake = cursor.execute("SELECT rake from farm where user_id = ?", (message.from_user.id,)).fetchone()
         rake = rake[0]

         linen = cursor.execute("SELECT linen from farm where user_id = ?", (message.from_user.id,)).fetchone()
         linen = int(linen[0])

         cotton = cursor.execute("SELECT cotton from farm where user_id = ?", (message.from_user.id,)).fetchone()
         cotton = int(cotton[0])

         rud = str(message.text.split()[1])

         rx_linen = random.randint(5,10)

      
         if rake == 'Cherick':
             period = 2
         else:
            period = 5
         get = cursor.execute("SELECT time_rake FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
         last_stavka = int(get[0])
         stavkatime = time.time() - float(last_stavka)
         
         if stavkatime > period:
            if rake == 'Cherick':
               if rud == 'лён':
                  await bot.send_message(message.chat.id, f"🍃 | Вы успешно собрали {rx_linen * 2} лёна", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET linen = {linen + rx_linen * 2} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
               if rud == 'хлопок':
                  await bot.send_message(message.chat.id, f"🌿 | Вы успешно собрали {rx_linen} хлопка", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET cotton = {cotton + rx_linen} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
            if rake == 'Zerro':
               if rud == 'лён':
                  await bot.send_message(message.chat.id, f"🍃 | Вы успешно собрали {rx_linen * 2} лёна", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET linen = {linen + rx_linen * 2} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
               if rud == 'хлопок':
                  await bot.send_message(message.chat.id, f"🌿 | Вы успешно собрали {rx_linen} хлопка", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET cotton = {cotton + rx_linen} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
            if rake == 'on':
               if rud == 'лён':
                  await bot.send_message(message.chat.id, f"🍃 | Вы успешно собрали {rx_linen} лёна", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET linen = {linen + rx_linen} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
               if rud == 'хлопок':
                  await bot.send_message(message.chat.id, f"🌿 | Вы успешно собрали {rx_linen} хлопка", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET cotton = {cotton + rx_linen} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! у вас нету граблей, что бы купить грабли введите команду \"Купить грабли\"", parse_mode='html')
               return
         
         else:
            await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! собирать урожай можно раз в {period} секунд!", parse_mode='html')     
            return      
       except IndexError:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Ошибка! Пример: Собрать [лён, хлопок]", parse_mode='html')

    if message.text.startswith('Собрать'):
       try:
         user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
         user_name = user_name[0]
         user_id = message.from_user.id

         rake = cursor.execute("SELECT rake from farm where user_id = ?", (message.from_user.id,)).fetchone()
         rake = rake[0]

         linen = cursor.execute("SELECT linen from farm where user_id = ?", (message.from_user.id,)).fetchone()
         linen = int(linen[0])

         cotton = cursor.execute("SELECT cotton from farm where user_id = ?", (message.from_user.id,)).fetchone()
         cotton = int(cotton[0])

         rud = str(message.text.split()[1])

         rx_linen = random.randint(5,10)

      

         if rake == 'Cherick':
             period = 2
         else:
            period = 5
         get = cursor.execute("SELECT time_rake FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
         last_stavka = int(get[0])
         stavkatime = time.time() - float(last_stavka)
         
         if stavkatime > period:
            if rake == 'Cherick':
               if rud == 'лён':
                  await bot.send_message(message.chat.id, f"🍃 | Вы успешно собрали {rx_linen * 2} лёна", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET linen = {linen + rx_linen * 2} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
               if rud == 'хлопок':
                  await bot.send_message(message.chat.id, f"🌿 | Вы успешно собрали {rx_linen} хлопка", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET cotton = {cotton + rx_linen} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
            if rake == 'Zerro':
               if rud == 'лён':
                  await bot.send_message(message.chat.id, f"🍃 | Вы успешно собрали {rx_linen * 2} лёна", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET linen = {linen + rx_linen * 2} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
               if rud == 'хлопок':
                  await bot.send_message(message.chat.id, f"🌿 | Вы успешно собрали {rx_linen} хлопка", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET cotton = {cotton + rx_linen} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
            if rake == 'on':
               if rud == 'лён':
                  await bot.send_message(message.chat.id, f"🍃 | Вы успешно собрали {rx_linen} лёна", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET linen = {linen + rx_linen} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
               if rud == 'хлопок':
                  await bot.send_message(message.chat.id, f"🌿 | Вы успешно собрали {rx_linen} хлопка", parse_mode='html')
                  cursor.execute(f'UPDATE farm SET cotton = {cotton + rx_linen} WHERE user_id = "{user_id}"')
                  cursor.execute(f'UPDATE bot_time SET time_rake = {time.time()} WHERE user_id = "{user_id}"')
                  connect.commit()
                  return
            else:
               await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! у вас нету граблей, что бы купить грабли введите команду \"Купить грабли\"", parse_mode='html')
               return
         
         else:
            await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! собирать урожай можно раз в {period} секунд!", parse_mode='html')   
            return        
       except IndexError:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Ошибка! Пример: Собрать [лён, хлопок]", parse_mode='html')
          
    if message.text.lower() == 'продать грабли':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       
       rake = cursor.execute("SELECT rake from farm where user_id = ?", (message.from_user.id,)).fetchone()
       rake = rake[0]

       if rake == 'off':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! у вас и так нету граблей, чтобы купить грабли введите команду \"Купить грабли\"", parse_mode='html')

       if rake == 'Zerro':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Но вы не можете продать грабли Zerro", parse_mode='html')

       if rake == 'Cherick':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Но вы не можете продать грабли Cherick", parse_mode='html')




       if rake == 'on':
         await bot.send_message(message.chat.id, f"⛏ | Вы продали грабли за 5.000$ ", parse_mode='html')
         cursor.execute(f'UPDATE farm SET rake = "off" WHERE user_id = "{user_id}"')
         cursor.execute(f'UPDATE users SET balance = {balance + 5000} WHERE user_id = "{user_id}"')
         connect.commit()

    if message.text.lower() == 'купить грабли':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       
       rake = cursor.execute("SELECT rake from farm where user_id = ?", (message.from_user.id,)).fetchone()
       rake = rake[0]

       if rake == 'on':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! у вас уже есть грабли, что бы продать грабли введите команду \"Продать грабли\"", parse_mode='html')

       if rake == 'Zerro':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! у вас уже есть грабли", parse_mode='html')
 
       if rake == 'Cherick':
          await bot.send_message(message.chat.id , f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! у вас уже есть грабли", parse_mode='html')


       if rake == 'off':
          if balance >= 5000:
             await bot.send_message(message.chat.id, f"⛏ | Вы купили грабли за 5.000$ ", parse_mode='html')
             cursor.execute(f'UPDATE farm SET rake = "on" WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET balance = {balance - 5000} WHERE user_id = "{user_id}"')
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас не хватает средств!", parse_mode='html')



###############################################ИНВЕНТАРЬ####################################################################

    if message.text.lower() == 'инвентарь':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       
       loser = ['😐', '😕','😟','😔','😓']
       rloser = random.choice(loser)

       farm = 0
       men = 0
       ob = 0

       linen = cursor.execute("SELECT linen from farm where user_id = ?", (message.from_user.id,)).fetchone()
       linen = int(linen[0])
       linen_f = '{:,}'.format(linen)

       cotton = cursor.execute("SELECT cotton from farm where user_id = ?", (message.from_user.id,)).fetchone()
       cotton = int(cotton[0])
       cotton_f = '{:,}'.format(cotton)

       iron = cursor.execute("SELECT iron from mine where user_id = ?", (message.from_user.id,)).fetchone()
       iron = int(iron[0])
       iron_f = '{:,}'.format(iron)

       metall = cursor.execute("SELECT metall from mine where user_id = ?", (message.from_user.id,)).fetchone()
       metall = int(metall[0])
       metall_f = '{:,}'.format(metall)

       silver = cursor.execute("SELECT silver from mine where user_id = ?", (message.from_user.id,)).fetchone()
       silver = int(silver[0])
       silver_f = '{:,}'.format(silver)

       bronza = cursor.execute("SELECT bronza from mine where user_id = ?", (message.from_user.id,)).fetchone()
       bronza = int(bronza[0])
       bronza_f = '{:,}'.format(bronza)

       gold = cursor.execute("SELECT gold from mine where user_id = ?", (message.from_user.id,)).fetchone()
       gold = int(gold[0])
       gold_f = '{:,}'.format(gold)

       if iron > 0:
          iron2 = f'    🪨 | Камня: {iron_f} шт\n'
          men = men + 1
          ob = ob + 1
       else:
          iron2 = ''

       if metall > 0:
          metall2 = f'    ⛓ | Железа: {metall_f} шт\n'
          men = men + 1
          ob = ob + 1
       else:
          metall2 = ''
      
       if silver > 0:
          silver2 = f'    🪙 | Серебра: {silver_f} шт\n'
          men = men + 1
          ob = ob + 1
       else:
          silver2 = ''

       if bronza > 0:
          bronza2 = f'    🎇 | Бронзы: {bronza_f} шт\n'
          men = men + 1
          ob = ob + 1
       else:
          bronza2 = ''

       if gold > 0:
          gold2 = f'    ⚜️ | Золота: {gold_f} шт\n'
          men = men + 1
          ob = ob + 1
       else:
          gold2 = ''

       if men > 0:
          men_2 = '\n⛏ | Шахта\n'
       else:
          men_2 = ''
       
       if linen > 0:
          linen2 = f'      🍃 | Лён: {linen_f} шт\n'
          farm = farm + 1
          ob = ob + 1
       else:
          linen2 = ''

       if cotton > 0:
          cotton2 = f'      🌿 | Хлопок: {cotton_f} шт\n'
          farm = farm + 1
          ob = ob + 1
       else:
          cotton2 = ''

       if farm > 0:
          farm2 = '🌾 | Ферма\n'
       else:
          farm2 = ''

       if ob == 0:
          ob2 = f'Вещи отсутствуют {rloser}'
       else:
          ob2 = ''
      
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот ваш инвентарь:\n{ob2}{men_2}{iron2}{metall2}{silver2}{bronza2}{gold2}\n{farm2}{linen2}{cotton2}", parse_mode='html')

    if message.text.startswith('гонка'):

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       
       loser = ['😐', '😕','😟','😔','😓']
       rloser = random.choice(loser)

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       cars = cursor.execute("SELECT cars from cars where user_id = ?", (message.from_user.id,)).fetchone()
       cars = cars[0]

       hp = cursor.execute("SELECT hp from cars where user_id = ?", (message.from_user.id,)).fetchone()
       hp = int(hp[0])

       benz = cursor.execute("SELECT benz from cars where user_id = ?", (message.from_user.id,)).fetchone()
       benz = int(benz[0])

       summ = int(message.text.split()[1])
       summ2 = '{:,}'.format(summ)

       if cars == 1:
          cars_name = 'Самокат'
          cars_summ = 10000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 2:
          cars_name = 'Велосипед'
          cars_summ = 15000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 3:
          cars_name = 'Гироскутер'
          cars_summ = 30000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 4:
          cars_name = 'Сегвей'
          cars_summ = 50000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 5:
          cars_name = 'Мопед'
          cars_summ = 90000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 6:
          cars_name = 'Мотоцикл'
          cars_summ = 100000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 7:
          cars_name = 'ВАЗ 2109'
          cars_summ = 250000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 8:
          cars_name = 'Квадроцикл'
          cars_summ = 400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 9:
          cars_name = 'Багги'
          cars_summ = 600000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 10:
          cars_name = 'Вездеход'
          cars_summ = 900000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 11:
          cars_name = 'Лада Xray'
          cars_summ = 1400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 12:
          cars_name = 'Audi Q7'
          cars_summ = 2500000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 13:
          cars_name = 'BMW X6'
          cars_summ = 6000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 14:
          cars_name = 'Toyota FT-HS'
          cars_summ = 8000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 15:
          cars_name = 'BMW Z4 M'
          cars_summ = 10000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 16:
          cars_name = 'Subaru WRX STI'
          cars_summ = 40000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 17:
          cars_name = 'Lamborghini Veneno'
          cars_summ = 100000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 18:
          cars_name = 'Tesla Roadster'
          cars_summ = 300000000000
          cars_summ2 = '{:,}'.format(cars_summ)


       rx = random.randint(0,1000)
       rx2 = random.randint(1,25)
       summ3 = summ * 2
       summ4 = '{:,}'.format(summ3)

       if summ < 1:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя играть на отрицательное число")
          return

       period = 5
       getе = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = int(getе[0])
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if summ <= balance:
             if cars > 0:
                if hp > 0:
                   if benz > 0:
                      if int(rx) in range(0,600):
                         await bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🏎 | Игра: Гонки\n🚘 | Машина: {cars_name}\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: 0$", parse_mode='html')
                         cursor.execute(f'UPDATE cars SET hp = {hp - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET benz = {benz - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                         connect.commit()
                      if int(rx) in range(601, 1000):
                         await bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🏎 | Игра: Гонки\n🚘 | Машина: {cars_name}\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {summ4}$", parse_mode='html')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE users SET balance = {balance + summ * 2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET hp = {hp - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET benz = {benz - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                         connect.commit()
                   else:
                      await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас закончился бензин в автомобиле", parse_mode='html')
                else:
                   await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас поломался автомобиль , вы не можете участвовать в гонках", parse_mode='html')
             else:
                await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Какие гонки без автомобиля? Купите автомобиль", parse_mode='html') 
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас нехватает средств", parse_mode='html') 
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! играй можно раз в {period} секунд", parse_mode='html') 


    if message.text.startswith('Гонка'):

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       
       loser = ['😐', '😕','😟','😔','😓']
       rloser = random.choice(loser)

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       cars = cursor.execute("SELECT cars from cars where user_id = ?", (message.from_user.id,)).fetchone()
       cars = cars[0]

       hp = cursor.execute("SELECT hp from cars where user_id = ?", (message.from_user.id,)).fetchone()
       hp = int(hp[0])

       benz = cursor.execute("SELECT benz from cars where user_id = ?", (message.from_user.id,)).fetchone()
       benz = int(benz[0])

       summ = int(message.text.split()[1])
       summ2 = '{:,}'.format(summ)

       if cars == 1:
          cars_name = 'Самокат'
          cars_summ = 10000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 2:
          cars_name = 'Велосипед'
          cars_summ = 15000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 3:
          cars_name = 'Гироскутер'
          cars_summ = 30000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 4:
          cars_name = 'Сегвей'
          cars_summ = 50000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 5:
          cars_name = 'Мопед'
          cars_summ = 90000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 6:
          cars_name = 'Мотоцикл'
          cars_summ = 100000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 7:
          cars_name = 'ВАЗ 2109'
          cars_summ = 250000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 8:
          cars_name = 'Квадроцикл'
          cars_summ = 400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 9:
          cars_name = 'Багги'
          cars_summ = 600000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 10:
          cars_name = 'Вездеход'
          cars_summ = 900000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 11:
          cars_name = 'Лада Xray'
          cars_summ = 1400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 12:
          cars_name = 'Audi Q7'
          cars_summ = 2500000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 13:
          cars_name = 'BMW X6'
          cars_summ = 6000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 14:
          cars_name = 'Toyota FT-HS'
          cars_summ = 8000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 15:
          cars_name = 'BMW Z4 M'
          cars_summ = 10000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 16:
          cars_name = 'Subaru WRX STI'
          cars_summ = 40000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 17:
          cars_name = 'Lamborghini Veneno'
          cars_summ = 100000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 18:
          cars_name = 'Tesla Roadster'
          cars_summ = 300000000000
          cars_summ2 = '{:,}'.format(cars_summ)


       rx = random.randint(0,1000)
       rx2 = random.randint(1,25)
       summ3 = summ * 2
       summ4 = '{:,}'.format(summ3)
       
       if summ < 1:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя играть на отрицательное число")
          return

       period = 5
       getе = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = int(getе[0])
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if summ <= balance:
             if cars > 0:
                if hp > 0:
                   if benz > 0:
                      if int(rx) in range(0,600):
                         await bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🏎 | Игра: Гонки\n🚘 | Машина: {cars_name}\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: 0$", parse_mode='html')
                         cursor.execute(f'UPDATE cars SET hp = {hp - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET benz = {benz - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                         connect.commit()
                      if int(rx) in range(601, 1000):
                         await bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🏎 | Игра: Гонки\n🚘 | Машина: {cars_name}\n🎟 | Ставка: {summ2}$\n🧾 | Выигрыш: {summ4}$", parse_mode='html')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE users SET balance = {balance + summ * 2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET hp = {hp - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET benz = {benz - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                         connect.commit()
                   else:
                      await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас закончился бензин в автомобиле", parse_mode='html')
                else:
                   await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас поломался автомобиль , вы не можете участвовать в гонках", parse_mode='html')
             else:
                await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Какие гонки без автомобиля? Купите автомобиль", parse_mode='html') 
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас нехватает средств", parse_mode='html') 
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! играй можно раз в {period} секунд", parse_mode='html') 
        



######################################################Привилегии \ Донат меню##############################################
    if message.text.lower() == 'донат':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id 

       donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?", (message.from_user.id,)).fetchone()
       donate_coins = int(donate_coins[0])
       donate_coins2 = '{:,}'.format(donate_coins)

       donate_menu = InlineKeyboardMarkup(row_width=2)
       privilegii = InlineKeyboardButton(text='📝 Привилегии', callback_data='privilegii')
       case = InlineKeyboardButton(text='🎁 Кейсы', callback_data='case')
       adms = InlineKeyboardButton(text='⛔️ Права администратора', callback_data='adms')
       donate_menu.add(privilegii, adms, case)
       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, добро пожаловать в донат-меню 🔱

🪙 | Donate-coins - {donate_coins2} 

ℹ️ | 1 Donate-coins = 2Р

🔎 | Категории:
      1️⃣ | Привилегии
      2️⃣ | Права администратора

ℹ️ | Чтобы купить Donate-coins, обратитесь к владельцу бота <a href='t.me/haeshka_qwe_per/'>Хаешка</a> 

↘️ Виберите категории по кнопкам ниже   
       """, reply_markup=donate_menu, parse_mode='html')
    if message.text.lower() == 'властелин':

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id  

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за привилегию ВЛАСТЕЛИН 🤎

🛒 | При покупке:
        1️⃣ | Бонус-кит ВЛАСТЕЛИН
        2️⃣ | Префикс ВЛАСТЕЛИН
        3️⃣ | 50.000.000$
        4️⃣ | 150 Рейтинга
        5️⃣ | Money-case 5 шт.
        6️⃣ | Donate-case 1 шт.
        7️⃣ | Способность менять себе префикс
        8️⃣ | Способность менять игрокам префикс
        9️⃣ | Ограничение на время в играх становиться 2 секунды

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ВЛАСТЕЛИН
        2️⃣ | Префикс ВЛАСТЕЛИН
        3⃣ | Способность менять себе префикс
        4⃣ | Способность менять игрокам префикс
        5⃣ | Ограничение на время в играх становиться 2 секунды

🛒 Чтобы купить привилегию , ввойдите в Donate-menu с помощю команды \"Донат\"
       """, parse_mode='html') 


    if message.text.lower() == 'бог':

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id  

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за привилегию БОГ 🤍

🛒 | При покупке:
        1️⃣ | Бонус-кит БОГ
        2️⃣ | Префикс БОГ
        3️⃣ | 25.000.000$
        4️⃣ | 100 Рейтинга
        5️⃣ | Money-case 5 шт.
        6️⃣ | Donate-case 1 шт.
        7️⃣ | Способность менять себе префикс
        8️⃣ | Способность менять игрокам префикс
        9️⃣ | Ограничение на время в играх становиться 2 секунды

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит БОГ
        2️⃣ | Префикс БОГ
        3⃣ | Способность менять себе префикс
        4⃣ | Способность менять игрокам префикс
        5⃣ | Ограничение на время в играх становиться 2 секунды

🛒 Чтобы купить привилегию , ввойдите в Donate-menu с помощю команды \"Донат\"
       """, parse_mode='html') 


    if message.text.lower() == 'владелец':

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id  

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за привилегию ВЛАДЕЛЕЦ 🖤

🛒 | При покупке:
        1️⃣ | Бонус-кит ВЛАДЕЛЕЦ
        2️⃣ | Префикс ВЛАДЕЛЕЦ
        3️⃣ | 10.000.000$
        4️⃣ | 74 Рейтинга
        5️⃣ | Money-case 5 шт.
        6️⃣ | Donate-case 1 шт.
        7️⃣ | Способность менять себе префикс
        8️⃣ | Способность менять игрокам префикс

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ВЛАДЕЛЕЦ
        2️⃣ | Префикс ВЛАДЕЛЕЦ
        3⃣ | Способность менять себе префикс
        4⃣ | Способность менять игрокам префикс

🛒 Чтобы купить привилегию , ввойдите в Donate-menu с помощю команды \"Донат\"
       """, parse_mode='html') 


    if message.text.lower() == 'основатель':

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id  

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за привилегию ОСНОВАТЕЛЬ 💜

🛒 | При покупке:
        1️⃣ | Бонус-кит ОСНОВАТЕЛЬ
        2️⃣ | Префикс ОСНОВАТЕЛЬ
        3️⃣ | 4.000.000$
        4️⃣ | 54 Рейтинга
        5️⃣ | Money-case 5 шт.
        6️⃣ | Donate-case 1 шт.
        7️⃣ | Способность менять себе префикс

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ОСНОВАТЕЛЬ
        2️⃣ | Префикс ОСНОВАТЕЛЬ
        3⃣ | Способность менять себе префикс

🛒 Чтобы купить привилегию , ввойдите в Donate-menu с помощю команды \"Донат\"
       """, parse_mode='html') 


    if message.text.lower() == 'спонсор':

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id  

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за привилегию СПОНСОР 💙

🛒 | При покупке:
        1️⃣ | Бонус-кит СПОНСОР
        2️⃣ | Префикс СПОНСОР
        3️⃣ | 3.000.000$
        4️⃣ | 25 Рейтинга
        5️⃣ | Money-case 5 шт.
        6️⃣ | Способность менять себе префикс

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит СПОНСОР
        2️⃣ | Префикс СПОНСОР
        3⃣ | Способность менять себе префикс

🛒 Чтобы купить привилегию , ввойдите в Donate-menu с помощю команды \"Донат\"   
       """, parse_mode='html') 


    if message.text.lower() == 'хелпер':

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id  

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за привилегию ХЕЛПЕР 💚

🛒 | При покупке:
        1️⃣ | Бонус-кит ХЕЛПЕР
        2️⃣ | Префикс ХЕЛПЕР
        3️⃣ | 750.000$
        4️⃣ | 20 Рейтинга
        5️⃣ | Money-case 3 шт.
        6️⃣ | Способность менять себе префикс

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ХЕЛПЕР
        2️⃣ | Префикс ХЕЛПЕР
        3⃣ | Способность менять себе префикс

🛒 Чтобы купить привилегию , ввойдите в Donate-menu с помощю команды \"Донат\"   
       """, parse_mode='html') 


    if message.text.lower() == 'платина':

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id  

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за привилегию ПЛАТИНА 💛

🛒 | При покупке:
        1️⃣ | Бонус-кит ПЛАТИНА
        2️⃣ | Префикс ПЛАТИНА
        3️⃣ | 550.000$
        4️⃣ | 10 Рейтинга
        5️⃣ | Money-case 1 шт.

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ПЛАТИНА
        2️⃣ | Префикс ПЛАТИНА

🛒 Чтобы купить привилегию , ввойдите в Donate-menu с помощю команды \"Донат\"     
       """, parse_mode='html') 


    if message.text.lower() == 'премиум':

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id  

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за привилегию ПРЕМИУМ 🧡

🛒 | При покупке:
        1️⃣ | Бонус-кит ПРЕМИУМ
        2️⃣ | Префикс ПРЕМИУМ
        3️⃣ | 300.000$

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ПРЕМИУМ
        2️⃣ | Префикс ПРЕМИУМ

🛒 Чтобы купить привилегию , ввойдите в Donate-menu с помощю команды \"Донат\"     
       """, parse_mode='html') 
    
    if message.text.lower() == 'вип':

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id  

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за привилегию ВИП ❤️

🛒 | При покупке:
        1️⃣ | Бонус-кит ВИП
        2️⃣ | Префикс ВИП
        3️⃣ | 250.000$

🎁 | При использовании Donate-Case:
       1️⃣ | Бонус-кит ВИП
       2️⃣ | Префикс ВИП

🛒 Чтобы купить привилегию , ввойдите в Donate-menu с помощю команды \"Донат\"       
       """, parse_mode='html')  





###################################### КИТ-БОНУСЫ ##################################################
    if message.text.lower() == 'получить кит-бонус':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id 

       user_status = cursor.execute('SELECT user_status from users where user_id = ?', (message.from_user.id,)).fetchone()
       user_status = user_status[0]

       balance = cursor.execute('SELECT balance from users where user_id = ?', (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       rating = cursor.execute('SELECT rating from users where user_id = ?', (message.from_user.id,)).fetchone()
       rating = int(rating[0])

       ethereum = cursor.execute('SELECT ethereum from users where user_id = ?', (message.from_user.id,)).fetchone()
       ethereum = int(ethereum[0])

       metall = cursor.execute('SELECT metall from mine where user_id = ?', (message.from_user.id,)).fetchone()
       metall = int(metall[0])

       silver = cursor.execute('SELECT silver from mine where user_id = ?', (message.from_user.id,)).fetchone()
       silver = int(silver[0])

       bronza = cursor.execute('SELECT bronza from mine where user_id = ?', (message.from_user.id,)).fetchone()
       bronza = int(bronza[0])

       gold = cursor.execute('SELECT gold from mine where user_id = ?', (message.from_user.id,)).fetchone()
       gold = int(gold[0])
       period = 43200 #43200 s = 12h
       get = cursor.execute("SELECT time_kit FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно получили свой кит-бонус", parse_mode='html')
          time.sleep(0.5)
          if user_status == 'Player':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ⛓ 99 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 5 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 100🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 5} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET metall = {metall + 99} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 100} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Vip':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 5,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 🪙 57 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 15 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 200🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 5000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 15} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET silver = {silver + 57} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 200} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Premium':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 10,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 🪙 101 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 25 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 250🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 10000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 25} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET silver = {silver + 101} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 250} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Platina':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 15,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 🪙 125 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 50 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 300🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 15000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 50} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET silver = {silver + 125} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 300} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Helper':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 25,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 🎇 50 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 100 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 500🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 25000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 100} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET bronza = {bronza + 50} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Sponsor':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 150,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 🎇 150 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1.000🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 150000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET bronza = {bronza + 150} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 1000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Osnovatel':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 400,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ⚜️ 15 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1.000🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 400000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET gold = {gold + 15} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 1000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Vladelec':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 700,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ⚜️ 50 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1.000🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 700000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET gold = {gold + 50} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 1000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Bog':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 10.000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ⚜️ 150 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1.000🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 10000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET gold = {gold + 150} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 1000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return

          if user_status == 'Vlaselin':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 100.000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ⚜️ 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1.000🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 100000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET gold = {gold + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 1000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, администрация бота не может получать кит-бонус", parse_mode='html') 
             return   
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, получать кит-бонус можно раз в 12ч", parse_mode='html')


    if message.text.lower() == 'получить кит бонус':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id 

       user_status = cursor.execute('SELECT user_status from users where user_id = ?', (message.from_user.id,)).fetchone()
       user_status = user_status[0]

       balance = cursor.execute('SELECT balance from users where user_id = ?', (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       rating = cursor.execute('SELECT rating from users where user_id = ?', (message.from_user.id,)).fetchone()
       rating = int(rating[0])

       ethereum = cursor.execute('SELECT ethereum from users where user_id = ?', (message.from_user.id,)).fetchone()
       ethereum = int(ethereum[0])

       metall = cursor.execute('SELECT metall from mine where user_id = ?', (message.from_user.id,)).fetchone()
       metall = int(metall[0])

       silver = cursor.execute('SELECT silver from mine where user_id = ?', (message.from_user.id,)).fetchone()
       silver = int(silver[0])

       bronza = cursor.execute('SELECT bronza from mine where user_id = ?', (message.from_user.id,)).fetchone()
       bronza = int(bronza[0])

       gold = cursor.execute('SELECT gold from mine where user_id = ?', (message.from_user.id,)).fetchone()
       gold = int(gold[0])
       period = 43200 #43200 s = 12h
       get = cursor.execute("SELECT time_kit FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно получили свой кит-бонус", parse_mode='html')
          time.sleep(0.5)
          if user_status == 'Player':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ⛓ 99 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 5 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 100🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 5} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET metall = {metall + 99} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 100} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Vip':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 5,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 🪙 57 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 15 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 200🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 5000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 15} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET silver = {silver + 57} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 200} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Premium':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 10,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 🪙 101 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 25 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 250🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 10000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 25} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET silver = {silver + 101} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 250} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Platina':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 15,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 🪙 125 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 50 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 300🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 15000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 50} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET silver = {silver + 125} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 300} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Helper':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 25,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 🎇 50 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 100 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 500🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 25000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 100} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET bronza = {bronza + 50} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Sponsor':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 150,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 🎇 150 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1.000🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 150000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET bronza = {bronza + 150} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 1000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Osnovatel':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 400,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ⚜️ 15 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1.000🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 400000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET gold = {gold + 15} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 1000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Vladelec':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 700,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ⚜️ 50 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1.000🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 700000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET gold = {gold + 50} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 1000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'Bog':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 10.000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ⚜️ 150 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1.000🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 10000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET gold = {gold + 150} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 1000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return

          if user_status == 'Vlaselin':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 100.000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ⚜️ 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500 шт.", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1.000🟪", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 100000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET gold = {gold + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 1000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, администрация бота не может получать кит-бонус", parse_mode='html') 
             return   
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, получать кит-бонус можно раз в 12ч", parse_mode='html')


    if message.text.lower() in ['кит-бонусы', 'кит бонусы', 'кит бонус', 'кит-бонус']:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id 

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные о кит-бонусах 🎁

🎀 | Игрок:
      💰 | 1,000,000,000,000$
      ⛓ | 99 шт.
      💎 | 5 шт.
      🟣 | 100🟪

❤️ | Вип:
      💰 | 5,000,000,000,000$
      🪙 | 57 шт.
      💎 | 15 шт.
      🟣 | 200🟪

🧡 | Премиум:
      💰 | 10,000,000,000,000$
      🪙 | 101 шт.
      💎 |  25 шт.
      🟣 | 250🟪

💛 | Платина:
      💰 | 15,000,000,000,000$
      🪙 | 125 шт.
      💎 |  50 шт.
      🟣 | 300🟪

💚 | Хелпер:
      💰 | 25,000,000,000,000$
      🎇 | 50 шт.
      💎 |  100 шт.
      🟣 | 500🟪

💙 | Спонсор:
      💰 | 150,000,000,000,000$
      🎇 | 150 шт.
      💎 |  500 шт.
      🟣 | 1.000🟪

💜 | Основатель:
      💰 | 400,000,000,000,000$
      ⚜️ | 15 шт.
      💎 |  500 шт.
      🟣 | 1.000🟪

🖤 | ВЛАДЕЛЕЦ:
      💰 | 700,000,000,000,000$
      ⚜️ | 50 шт.
      💎 |  500 шт.
      🟣 | 1.000🟪

🤍 | БОГ:
      💰 | 10.000,000,000,000,000$
      ⚜️ | 150 шт.
      💎 |  500 шт.
      🟣 | 1.000🟪

🤎 | ВЛАСТЕЛИН:
      💰 | 100.000,000,000,000,000$
      ⚜️ | 500 шт.
      💎 |  500 шт.
      🟣 | 1.000🟪

ℹ️ Чтобы получить кит-бонус введите команду \"Получить кит-бонус\" 
ℹ️ Кит-бонус получить можно раз в 12ч      
       """, parse_mode='html')

####################################### ТОП Мажоров#######################################

    if message.text.lower() in ['топ багочей', 'топ мажоров', 'топ б']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       list = cursor.execute(f"SELECT * FROM users ORDER BY balance DESC").fetchmany(10)
       top_list = []

       num = 0

       for user in list:
          if int(user[4]) < 0:
             balance3 = 0
          if int(user[4]) in range(1000, 999999):
             balance1 = user[4] / 1000
             balance2 = int(balance1)
             balance3 = f'{balance2} тыс'

          if int(user[4]) in range(1000000, 999999999):
             balance1 = user[4] / 1000000
             balance2 = int(balance1)
             balance3 = f'{balance2} млн'
 
          if int(user[4]) in range(1000000000, 999999999999):
             balance1 = user[4] / 1000000000
             balance2 = int(balance1)
             balance3 = f'{balance2} млрд'
 
          if int(user[4]) in range(1000000000000, 999999999999999):
             balance1 = user[4] / 1000000000000
             balance2 = int(balance1)
             balance3 = f'{balance2} трлн'

          if int(user[4]) in range(1000000000000000, 999999999999999999):
             balance1 = user[4] / 1000000000000000
             balance2 = int(balance1)
             balance3 = f'{balance2} квдр'

          if int(user[4]) in range(1000000000000000000, 999999999999999999999):
             balance1 = user[4] / 1000000000000000000
             balance2 = int(balance1)
             balance3 = f'{balance2} квнт'

          if int(user[4]) in range(1000000000000000000000, 999999999999999999999999):
             balance1 = user[4] / 1000000000000000000000
             balance2 = int(balance1)
             balance3 = f'{balance2} скст' 
          if int(user[4]) in range(1000000000000000000000000, 999999999999999999999999):
             balance1 = user[4] / 1000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} трикс'
          if int(user[4]) >= 1000000000000000000000000000:
             balance1 = user[4] / 1000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} твинкс'  
          if int(user[4]) in range(1000000000000000000000000000000, 999999999999999999999999999999999):
             balance1 = user[4] / 1000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} септ'
          if int(user[4]) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
             balance1 = user[4] / 1000000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} октл'
          if int(user[4]) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
             balance1 = user[4] / 1000000000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} нонл'
          if int(user[4]) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
             balance1 = user[4] / 1000000000000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} декал'
          if int(user[4]) in range(1000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999):
             balance1 = user[4] / 1000000000000000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} эндк'
          if int(user[4]) in range(1000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999):
             balance1 = user[4] / 1000000000000000000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} доктл'
          if int(user[4]) in range(1000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999) :
             balance1 = user[4] / 1000000000000000000000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} гугл'
          if int(user[4]) in range(1000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999) :
             balance1 = user[4] / 1000000000000000000000000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} кинд'
          if int(user[4]) in range(1000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999) :
             balance1 = user[4] / 1000000000000000000000000000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} трипт'
          if int(user[4]) in range(1000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999) :
             balance1 = user[4] / 1000000000000000000000000000000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} срист'
          if int(user[4]) in range(1000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999):
             balance1 = user[4] / 1000000000000000000000000000000000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} манит'
          if int(user[4]) >= 1000000000000000000000000000000000000000000000000000000000000000:
             balance1 = user[4] / 1000000000000000000000000000000000000000000000000000000000000000
             balance2 = round(balance1)
             balance3 = f'{balance2} гвинт'

            
          num += 1

          if num == 1:
             num2 = '1️⃣'
             num3 = ' <b>💰ТОП 1💰</b> |'
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
          
          if user[3] == 'Owner':
             stats = ' ✅<b>РАЗРАБОТЧИК</b>✅ |'
          if user[3] == 'Admin':
             stats = ' ⛔️<b>АДМИН</b>⛔️ |'
          if user[3] == 'Helper_Admin':
             stats = ' ⚠️<b>HELPER АДМИН</b>⚠️ |'
          if user[3] in ['Player', 'Vip', 'Premium', 'Platina', 'Helper', 'Sponsor', 'Osnovatel', 'Vladelec', 'Bog', 'Vlaselin']:
             stats = ''


          top_list.append(f"{num2} {user[1]} |{stats}{num3} 🔎 ID: <code>{user[0]}</code> | ${balance3} ")

       top = "\n".join(top_list)
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот топ 10 богачей в боте:\n" + top, parse_mode='html')

############################## СИСТЕМА СООБЩЕНИЙ ####################################

    if message.text.lower() in ['система с', "система сообщений", "с сообщений", "с сообщение", "сс", "с с"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за систему сообщений 💬

ℹ️ | Пример команды: /m [ID] [сообщение]

⚠️ | Система сообщений была разработана для связи с игроками, у которых SMS SPAM BAN TELEGRAM        
       """, parse_mode='html')








##############################СИСТЕМА "К" ########################################

    if message.text.lower() in ['система к', 'к']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот информация за систему "К" ⚙️

🔩 | Информация:
<code>1 к</code> - 1.000$ - тыщ.
<code>1 кк</code> - 1.000.000$ - млн.
<code>1 ккк</code> - 1.000.000.000$ - млрд.
<code>1 кккк</code> - 1.000.000.000.000$ - трлн.
<code>1 ккккк</code> - 1.000.000.000.000.000$ - кврд.
<code>1 кккккк</code> - 1.000.000.000.000.000.000$ - квнт.
<code>1 ккккккк</code> - 1.000.000.000.000.000.000.000$ - скст.
<code>1 кккккккк</code> - 1.000.000.000.000.000.000.000.000$ трикс.
<code>1 ккккккккк</code> - 1.000.000.000.000.000.000.000.000.000$ твинкс.
<code>1 кккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000$ септ.
<code>1 ккккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000.000$ октл.
<code>1 кккккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000.000.000$ нонл.
<code>1 ккккккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000.000.000.000$ декал.
<code>1 кккккккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000.000.000.000.000$ эндк.
<code>1 ккккккккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000$ доктл.
<code>1 кккккккккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000$ гугл.
<code>1 ккккккккккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000$ кинд.
<code>1 кккккккккккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000$ трипт.
<code>1 ккккккккккккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000$ срист.
<code>1 кккккккккккккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000$ манит.
<code>1 ккккккккккккккккккккк</code> - 1.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000$ гвинт.

ℹ️ | <b>Система "К" , работает только на командах с маленькой буквы, с маленькой, вы можете водит точные цифры ставки, передачи и так далее ...</b>
    """, parse_mode='html')




###################################### аватарки #######################################
    if message.text.lower() in ['убрать аву', "убрать аватарку", "удалить аву", "удалить аватарку"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0]) 

       await bot.send_message(message.chat.id, f"🪣 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно удалили свою аватарку", parse_mode='html')
       cursor.execute(f'UPDATE avatarka SET avatarka = "none" WHERE user_id = {user_id}')
       connect.commit()


    if message.text.lower() in ['ава', 'аватарки', "аватарка", "фото"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       strach_photo = open('страж.jpg', 'rb')

       cheat_photo = open('cheat.jpg', 'rb')

       apper_photo = open('apper.jpg', 'rb')

       dyp_photo = open('дюп.jpg', 'rb')

       girl_photo = open('girl.jpg', 'rb')

       admin_photo = open('админ.jpg', 'rb')

       ava_strach = InlineKeyboardMarkup(row_width=1)
       ava_strach2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_strach')
       ava_strach.add(ava_strach2)

       ava_cheat = InlineKeyboardMarkup(row_width=1)
       ava_cheat2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_cheat')
       ava_cheat.add(ava_cheat2)

       ava_apper = InlineKeyboardMarkup(row_width=1)
       ava_apper2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_apper')
       ava_apper.add(ava_apper2)

       ava_dyp = InlineKeyboardMarkup(row_width=1)
       ava_dyp2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_dyp')
       ava_dyp.add(ava_dyp2)

       ava_girl = InlineKeyboardMarkup(row_width=1)
       ava_girl2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_girl')
       ava_girl.add(ava_girl2)

       ava_admin = InlineKeyboardMarkup(row_width=1)
       ava_admin2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_admin')
       ava_admin.add(ava_admin2)

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, добро пожаловать в меню аватарок 🗾

ℹ️ | Всего аватарок: 4

ℹ️ | Доступные аватарки: ДЮППЕР, СТРАЖ, АППЕР, ЧИТЕР, ДЕВУШКА

⛔️ | Админ: АДМИН

ℹ️ | Аватарка ставиться на баланс

↘️ | Виберите одну аватарок ниже 
       """, parse_mode='html')
       await bot.send_photo(message.chat.id, strach_photo, '', reply_markup=ava_strach)
       await bot.send_photo(message.chat.id, cheat_photo, '', reply_markup=ava_cheat)
       await bot.send_photo(message.chat.id, apper_photo, '', reply_markup=ava_apper)
       await bot.send_photo(message.chat.id, dyp_photo, '', reply_markup=ava_dyp)
       await bot.send_photo(message.chat.id, girl_photo, '', reply_markup=ava_girl)
       await bot.send_photo(message.chat.id, admin_photo, '', reply_markup=ava_admin)




###################################### РЕПУТАЦИЯ + ###################################

    if message.text.lower() in ['+', '++', '+++', 'кросс', "молодец", "имба"]:
       user_id = message.from_user.id

       reply_user_id = message.reply_to_message.from_user.id
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = user_name[0]

       reput = cursor.execute("SELECT reput from reput where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reput = int(reput[0])

       if reply_user_id == user_id:
          await bot.send_message(message.chat.id, f"📝 Жулик, не голосуй", parse_mode='html')
          return

       await bot.send_message(message.chat.id, f"📊 | Вы успешно повысили репутацию  <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> . Теперь его репутация: {reput + 1}", parse_mode='html')
       cursor.execute(f'UPDATE reput SET reput = {reput + 1} WHERE user_id = {reply_user_id}')
       connect.commit()


###################################### РП КОМАНДЫ ####################################

    if message.text.lower() in ["рп-команды", "РП-команды"]:
       user_name = message.from_user.get_mention(as_html=True)
       await bot.send_message(message.chat.id, f"{user_name}, список РП-команд:\n🤗 | Обнять\n👏 | Похлопать\n👨‍💻 | Заскамить\n☕️ | Пригласить на чай\n👉👌 | Изнасиловать\n🤝 | Взять за руку\n📱 | Подарить айфон\n✋ | Дать пять\n😬 | Укусить\n🤛 | Ударить\n🤲 | Прижать\n💋 | Чмок\n💋 | Поцеловать\n😼 | Кусь\n🤲 | Прижать\n🔪 | Убить\n🤜 | Уебать\n💰 | Украсть\n🔞 | Выебать\n👅 | Отсосать\n👅 | Отлизать\n🔞 | Трахнуть\n🔥 | Сжечь", parse_mode='html')

    if message.text.lower() in ["чмок", "Чмок"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💋 | {user_name} чмокнул(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["кусь", "Кусь"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"😼 | {user_name} кусьнул(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["обнять", "Обнять"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤗 | {user_name} обнял(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["поцеловать", "Поцеловать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💋 | {user_name} поцеловал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["дать пять", "Дать пять"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"✋ | {user_name} дал(-а) пять {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["подарить айфон", "Подарить айфон"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"📱 | {user_name} подарил(-а) айфон {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["ударить", "Ударить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤛 | {user_name} ударил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["заскамить", "Заскамить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👨‍💻 | {user_name} заскамил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["прижать", "Прижать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤲 | {user_name} прижал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["укусить", "Укусить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"😬 | {user_name} укусил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["взять за руку", "Взять за руку"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤝 | {user_name} взял(-а) за руку {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["прижать", "Прижать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤲 | {user_name} прижал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["похлопать", "Похлопать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👏 | {user_name} похлопал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["изнасиловать", "Изнасиловать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👉👌 | {user_name} изнасиловал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["пригласить на чай", "Пригласить на чай"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"☕️ | {user_name} пригласил(-а) на чай {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["убить", "Убить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔪 | {user_name} убил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["уебать", "Уебать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤜 | {user_name} уебал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["украсть", "Украсть"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💰 | {user_name} украл(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["отсосать", "Отсосать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👅 | {user_name} отсосал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["отлизать", "Отлизать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👅 | {user_name} отлизал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["выебать", "Выебать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔞 | {user_name} выебал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["сжечь", "Сжечь"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔥 | {user_name} сжёг {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["трахнуть", "Трахнуть"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔞 | {user_name} трахнул(-а) {reply_user_name}", parse_mode='html')
########################################PROMO#########################################
    if message.text.lower() in ['промокод #qwe', '#qwe']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #100sub', '#100sub']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')


    if message.text.lower() in ['промокод #222sub', '#222sub']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #nohack', '#nohack']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #crazy', '#crazy']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')


    if message.text.lower() in ['промокод #googl', '#googl']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')


    if message.text.lower() in ['промокод #sistem_k', '#sistem_k']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')


    if message.text.lower() in ['промокод #500sub', '#500sub']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #case_money', '#case_money']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #1500sub', '#1500sub']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #1k', '#1k']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #vipe', '#vipe']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')
    if message.text.lower() in ['промокод #haeshka', '#haeshka']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #haehka_kloyn', '#haehka_kloyn']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #sorry', '#sorry']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #update', '#update']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #sms', '#sms']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #300sub', '#300sub']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')

    if message.text.lower() in ['промокод #dc', '#dc']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')


    if message.text.lower() in ['промокод #case', '#case']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')



    if message.text.lower() in ['промокод #2к', '#2к']:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       members = cursor.execute(f"SELECT members from promo25 where user_id = {user_id}").fetchone()
       members = int(members[0])

       balance = cursor.execute(f"SELECT balance from users where user_id = {user_id}").fetchone()
       balance = int(balance[0])

       ob_members = cursor.execute("SELECT ob_members from promo25").fetchone()
       ob_members = int(ob_members[0])
       
       if ob_members < 50:
          if members == 0:
             await bot.send_message(message.chat.id, f"🖲 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно воспользовались промокодом #2к ", parse_mode='html')
             await bot.send_message(message.chat.id, f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам было зачислено 5 квдр.", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 5000000000000000} where user_id = {user_id}')
             cursor.execute(f'UPDATE promo25 SET members = {1} where user_id = {user_id}')
             cursor.execute(f'UPDATE promo25 SET ob_members = {ob_members + 1}')
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы уже воспользовались этим промокодом", parse_mode='html')
             return
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данный промокод больше не действителен", parse_mode='html')





########################################        Смена префикса          ######################################
    if message.text.startswith('Поменять префикс'):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = str(user_status[0])

       prefix = ' '.join(message.text.split()[2:])
       if len(prefix) <= 20:
          if user_status in ['Helper', 'Sponsor', 'Osnovatel', 'Vladelec', 'Bog', 'Vlaselin', 'Admin', 'Helper_Admin', 'Owner']:
             await bot.send_message(message.chat.id, f"🔒 | Вы успешно сменили свой префикс на {prefix}")
             cursor.execute(f'UPDATE users SET pref = "{prefix}" WHERE user_id = {user_id}')
             connect.commit()
             return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, менять префикс можно только от привилегии \"ХЕЛПЕР\"", parse_mode='html')
             return
       else:
          await bot.send_message(message.chat.id, f"🆘 | Игрок, менять префикс не может быть более 20 символов!", parse_mode='html')
          return

    if message.text.startswith('поменять префикс'):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = str(user_status[0])

       prefix = ' '.join(message.text.split()[2:])
       if len(prefix) <= 20:
          if user_status in ['Helper', 'Sponsor', 'Osnovatel', 'Vladelec', 'Bog', 'Vlaselin', 'Admin', 'Helper_Admin', 'Owner']:
             await bot.send_message(message.chat.id, f"🔒 | Вы успешно сменили свой префикс на {prefix}")
             cursor.execute(f'UPDATE users SET pref = "{prefix}" WHERE user_id = {user_id}')
             connect.commit()
             return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, менять префикс можно только от привилегии \"ХЕЛПЕР\"", parse_mode='html')
             return
       else:
          await bot.send_message(message.chat.id, f"🆘 | Игрок, менять префикс не может быть более 20 символов!", parse_mode='html')
          return

    if message.text.startswith('Cменить игроку префикс'):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       reply_user_id = message.reply_to_message.from_user.id
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = str(user_name[0])

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = str(user_status[0])

       prefix = ' '.join(message.text.split()[3:])
       if len(prefix) <= 20:
          period = 900
          get = cursor.execute("SELECT stavka FROM time_prefix WHERE user_id = ?", (message.from_user.id,)).fetchone()
          last_stavka = f"{int(get[0])}"
          stavkatime = time.time() - float(last_stavka)
          if stavkatime > period:
             if user_status in ['Vladelec', 'Bog', 'Vlaselin', 'Admin', 'Helper_Admin', 'Owner']:
                await bot.send_message(message.chat.id, f"🔒 | Вы успешно сменили игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> префикс на {prefix}", parse_mode='html')
                cursor.execute(f'UPDATE users SET pref = "{prefix}" WHERE user_id = {reply_user_id}')
                cursor.execute(f'UPDATE time_prefix SET stavka = "{time.time()}" WHERE user_id = {reply_user_id}')
                connect.commit()
                return
             else:
                await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, менять префикс можно только от привилегии \"ВЛАДЕЛЕЦ\"", parse_mode='html')
                return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, менять игроку ник можно раз в 15 минут", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"🆘 | Игрок, менять префикс не может быть более 20 символов!", parse_mode='html')
          return
    
    if message.text.startswith('cменить игроку префикс'):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       reply_user_id = message.reply_to_message.from_user.id
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = str(user_name[0])

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = str(user_status[0])

       prefix = ' '.join(message.text.split()[3:])
       if len(prefix) <= 20:
          period = 900
          get = cursor.execute("SELECT stavka FROM time_prefix WHERE user_id = ?", (message.from_user.id,)).fetchone()
          last_stavka = f"{int(get[0])}"
          stavkatime = time.time() - float(last_stavka)
          if stavkatime > period:
             if user_status in ['Vladelec', 'Bog', 'Vlaselin', 'Admin', 'Helper_Admin', 'Owner']:
                await bot.send_message(message.chat.id, f"🔒 | Вы успешно сменили игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> префикс на {prefix}", parse_mode='html')
                cursor.execute(f'UPDATE users SET pref = "{prefix}" WHERE user_id = {reply_user_id}')
                cursor.execute(f'UPDATE time_prefix SET stavka = "{time.time()}" WHERE user_id = {reply_user_id}')
                connect.commit()
                return
             else:
                await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, менять префикс можно только от привилегии \"ВЛАДЕЛЕЦ\"", parse_mode='html')
                return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, менять игроку ник можно раз в 15 минут", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"🆘 | Игрок, менять префикс не может быть более 20 символов!", parse_mode='html')
          return
         
    
    if message.text.startswith('cменить префикс'):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = str(user_status[0])

       prefix = ' '.join(message.text.split()[2:])
       if len(prefix) <= 20:
          if user_status in ['Helper', 'Sponsor', 'Osnovatel', 'Vladelec', 'Bog', 'Vlaselin', 'Admin', 'Helper_Admin', 'Owner']:
             await bot.send_message(message.chat.id, f"🔒 | Вы успешно сменили свой префикс на {prefix}")
             cursor.execute(f'UPDATE users SET pref = "{prefix}" WHERE user_id = {user_id}')
             connect.commit()
             return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, менять префикс можно только от привилегии \"ХЕЛПЕР\"", parse_mode='html')
             return
       else:
          await bot.send_message(message.chat.id, f"🆘 | Игрок, менять префикс не может быть более 20 символов!", parse_mode='html')
          return

    if message.text.startswith('Сменить префикс'):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = str(user_status[0])

       prefix = ' '.join(message.text.split()[2:])
       if len(prefix) <= 20:
          if user_status in ['Helper', 'Sponsor', 'Osnovatel', 'Vladelec', 'Bog', 'Vlaselin', 'Admin', 'Helper_Admin', 'Owner']:
             await bot.send_message(message.chat.id, f"🔒 | Вы успешно сменили свой префикс на {prefix}")
             cursor.execute(f'UPDATE users SET pref = "{prefix}" WHERE user_id = {user_id}')
             connect.commit()
             return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, менять префикс можно только от привилегии \"ХЕЛПЕР\"", parse_mode='html')
             return
       else:
          await bot.send_message(message.chat.id, f"🆘 | Игрок, менять префикс не может быть более 20 символов!", parse_mode='html')
          return









#####################################################      КЕЙСЫ             ####################################################
    if message.text.lower() in ["открыть кейсы", "открыть кейс"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       money_case = cursor.execute(f'SELECT case_money from user_case where user_id = {user_id}').fetchone()
       money_case = int(money_case[0])

       donate_case = cursor.execute(f'SELECT case_donate from user_case where user_id = {user_id}').fetchone()
       donate_case = int(donate_case[0])

       ob_member = 0

       if money_case > 0:
          ob_member += 1
       else:
          pass

       if donate_case > 0:
          ob_member += 1
       else:
          pass

       if ob_member < 1:
          await bot.send_message(message.chat.id, f"""
🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету не каких кейсов 
          """,parse_mode='html')
          return
       
       case_shop1 = InlineKeyboardMarkup(row_width=2)
       money_case1 = InlineKeyboardButton(text='Открыть Money-Case 💸', callback_data='up_money_case')
       donate_case2 = InlineKeyboardButton(text='Открыть Donate-Case 🧧', callback_data='up_donate_case')
       case_shop1.add(money_case1, donate_case2)

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот ваши кейсы 🎁

💸 | Money-Case - {money_case} шт.
🧧 | Donate-Case - {donate_case} шт.

↘️ Виберите один из кейсов, который хотите открыть 
       """,reply_markup=case_shop1, parse_mode='html')

    if message.text.lower() == 'кейсы':
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       money_case = cursor.execute(f'SELECT case_money from user_case where user_id = {user_id}').fetchone()
       money_case = int(money_case[0])

       donate_case = cursor.execute(f'SELECT case_donate from user_case where user_id = {user_id}').fetchone()
       donate_case = int(donate_case[0])
      
       ob_members = 0

       if donate_case > 0:
          ob_members += 1
          donate_case2 = f'      🧧 | Donate-Case - {donate_case} шт.\n'
       else:
          donate_case2 = ''

       if money_case > 0:
          ob_members += 1
          money_case2 = f'      💸 | Money-Case - {money_case} шт.\n'
       else:
          money_case2 = ''

       if ob_members > 0:
          casee = '🎁 | Ваши кейсы:\n'
       else:
          casee = '😟 | У вас нету кейсов...'

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за кейсы 🎁

💸 | Money-Case - 50 Donate-Coins 🪙
🧧 | Donate-Case - 100 Donate-Coins 🪙

{casee}{donate_case2}{money_case2}

🖲 | Чтобы открыть один из кейсов, напишите команду \"Открыть кейсы\"
       """, parse_mode='html')





#################################################### !канал ################################
    if message.text.lower() in ['канал', "!канал", "channel"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       channel_pov = cursor.execute("SELECT members from channel_pov where user_id = ?", (message.from_user.id,)).fetchone()
       channel_pov = int(channel_pov[0])

       if channel_pov > 0:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы уже получили деньги за подписку")
          return
       
       sub_pov = InlineKeyboardMarkup(row_width=1)
       channel_push = InlineKeyboardButton(text='КАНАЛ 🔈', url='https://t.me/qwechannel')
       channel_poverk = InlineKeyboardButton(text='ПРОВЕРИТЬ ✅', callback_data='channel_poverk')
       sub_pov.add(channel_push, channel_poverk)

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>,, вот условия задание 💠

🔈 | Подписаться на канал

💰 | Приз: 500.000.000.000.000.000$

↘️ Виберите одну кнопку ниже...       
       """, reply_markup=sub_pov, parse_mode='html')
       user_channel_status = await bot.get_chat_member(chat_id="@qwechannel", user_id=message.from_user.id)
       if user_channel_status['status'] != 'left':
          print('GOOD')
       else:
          print('Luser')


@dp.callback_query_handler(text='gamevb')

@dp.callback_query_handler(text='ava_admin')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_status = str(user_status[0])

   if user_status in ['Admin', 'Helper_Admin', 'Owner']:
      await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"АДМИН\"", parse_mode='html')
      cursor.execute(f'UPDATE avatarka SET avatarka = "admin" WHERE user_id = {user_id}')
      connect.commit()
      return
   else:
      await callback.message.answer( f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику <a href='t.me/haeshka_qwe_per/'>Хаешка</a>  ⚠️", parse_mode='html')

@dp.callback_query_handler(text='ava_girl')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"ДЕВУШКА\"", parse_mode='html')
   cursor.execute(f'UPDATE avatarka SET avatarka = "girl" WHERE user_id = {user_id}')
   connect.commit()

@dp.callback_query_handler(text='ava_dyp')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"ДЮППЕР\"", parse_mode='html')
   cursor.execute(f'UPDATE avatarka SET avatarka = "dyp" WHERE user_id = {user_id}')
   connect.commit()

@dp.callback_query_handler(text='ava_apper')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"АППЕР\"", parse_mode='html')
   cursor.execute(f'UPDATE avatarka SET avatarka = "apper" WHERE user_id = {user_id}')
   connect.commit()

@dp.callback_query_handler(text='ava_cheat')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"ЧИТЕР\"", parse_mode='html')
   cursor.execute(f'UPDATE avatarka SET avatarka = "cheat" WHERE user_id = {user_id}')
   connect.commit()

@dp.callback_query_handler(text='ava_strach')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"СТРАЖ\"", parse_mode='html')
   cursor.execute(f'UPDATE avatarka SET avatarka = "strach" WHERE user_id = {user_id}')
   connect.commit()

@dp.callback_query_handler(text='channel_poverk')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
   balance = int(balance[0])
   user_channel_status = await bot.get_chat_member(chat_id="@qwechannel", user_id=callback.from_user.id)

   channel_pov = cursor.execute("SELECT members from channel_pov where user_id = ?", (callback.from_user.id,)).fetchone()
   channel_pov = int(channel_pov[0])

   if channel_pov > 0:
      await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы уже получили деньги за подписку", parse_mode='html')
      return

   if user_channel_status['status'] != 'left':
      await callback.message.answer( f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно подписались на канал ✅", parse_mode='html')
      await callback.message.answer( f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили приз в размере  500.000.000.000.000.000$", parse_mode='html')
      cursor.execute(f'UPDATE channel_pov SET members = {1} WHERE user_id = {user_id}')
      cursor.execute(f'UPDATE users SET balance = {balance + 500000000000000000} WHERE user_id = {user_id}')
      connect.commit()
   else:
      await callback.message.answer( f"❌ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не подписались на канал, попробуйте снова", parse_mode='html')

@dp.callback_query_handler(text='owner_cash')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за OWNER ⛔️

1️⃣ | Выдача валюты
2️⃣ | Отбор валюты
3️⃣ | Умножение валюты
4️⃣ | Обнуление
5️⃣ | Выдача бана
6️⃣ | Выдача разбана
7️⃣ |Поделить баланс
8️⃣ | Выдача прав администратора "ADMIN"
9️⃣ | Выдача прав администратора "HELPER-ADMIN"
🔟 | Выдача Donate-Coins
1️⃣1️⃣ | МАССОВОЕ ОБНУЛЕНИЕ
1️⃣2️⃣ | Выдача бана по ID
1️⃣3️⃣ | Выдача разбана по ID
1️⃣4️⃣ | Выдача варна
1️⃣5️⃣ | Отбор варна 
1️⃣6️⃣ | Выдача варна по ID
1️⃣7️⃣ | Отбор варна по ID
1️⃣8️⃣ | Возможность посмотреть профиль игрока
1️⃣9️⃣ | Возможность посмотреть профиль игрока по ID
2️⃣0️⃣ | Возможность выдать права администратора "OWNER"
2️⃣1️⃣ | ДОСТУП К КОНСОЛИ БОТА
2️⃣2️⃣ | ДОСТУП К РЕПОРТАМ

🛒 Для покупки администраторских прав , обратитесь к Владельцу бота - <a href="t.me/haeshka_qwe_per/">Хаешка</a>
    """,  parse_mode='html' )


@dp.callback_query_handler(text='helper_admins_cash')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за HELPER-ADMIN ⛔️

1️⃣ | Выдача валюты
2️⃣ | Отбор валюты
3️⃣ | Умножение валюты
4️⃣ | Обнуление
5️⃣ | Выдача бана
6️⃣ | Выдача разбана
7️⃣ | Поделить баланс
8️⃣ | Просмотр профила 
9️⃣ | Просмотр профиля по ID 
🔟 | Выдача варна 
1️⃣1️⃣ | Отбор варна
1️⃣2️⃣ | Выдача бана по ID
1️⃣3️⃣ | Выдача разбана по ID
1️⃣4️⃣ | Выдача варна по ID
1️⃣5️⃣ | Отбор варна по ID
1️⃣6️⃣ | Обнуление по ID
1️⃣7️⃣ | ДОСТУП К КОНСОЛИ БОТА
1️⃣8️⃣ | ДОСТУП К РЕПОРТАМ

🛒 Для покупки администраторских прав , обратитесь к Владельцу бота - <a href='t.me/haeshka_qwe_per/'>Хаешка</a> 
    """,  parse_mode='html' )

@dp.callback_query_handler(text='admins_cash')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за ADMIN ⛔️

1️⃣ | Выдача валюты
2️⃣ | Отбор валюты
3️⃣ | Умножение валюты
4️⃣ | Обнуление
5️⃣ | Просмотр профиля игрока
6️⃣ | Поделить баланс

🛒 Для покупки администраторских прав , обратитесь к Владельцу бота - <a href='t.me/haeshka_qwe_per/'>Хаешка</a> 
    """,  parse_mode='html' )

@dp.callback_query_handler(text='adms')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    admins_menu_cash = InlineKeyboardMarkup(row_width=2)
    admins_cash = InlineKeyboardButton(text='⛔️ ADMIN', callback_data='admins_cash')
    helper_admins_cash = InlineKeyboardButton(text='⛔️ HELPER-ADMIN', callback_data='helper_admins_cash')
    owner_cash = InlineKeyboardButton(text='⛔️ OWNER', callback_data='owner_cash')
    admins_menu_cash.add(admins_cash, helper_admins_cash, owner_cash)
    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за статусы администраторов⛔️

1️⃣ | ADMIN - 400Р
4️⃣ | HELPER-ADMIN - 1.500Р
5️⃣ | OWNER - 5.000Р

↘️ Чтобы посмотреть возможности , виберите статус ниже   
    """,reply_markup=admins_menu_cash,  parse_mode='html' )
  
@dp.callback_query_handler(text='cash_vlaselin')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    pref = cursor.execute("SELECT pref from users where user_id = ?",(callback.from_user.id,)).fetchone()
    pref = pref[0]
    
    case_donate = cursor.execute("SELECT case_donate from user_case where user_id = ?",(callback.from_user.id,)).fetchone()
    case_donate = int(case_donate[0])

    case_money = cursor.execute("SELECT case_money from user_case where user_id = ?",(callback.from_user.id,)).fetchone()
    case_money = int(case_money[0])
    
    balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
    balance = int(balance[0])
    
    rating = cursor.execute("SELECT rating from users where user_id = ?",(callback.from_user.id,)).fetchone()
    rating = int(rating[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])
    
    if donate_coins >= 300:
       await callback.message.answer( f"✅ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили привилегию ВЛАСТЕЛИН ", parse_mode='html' )
       cursor.execute(f'UPDATE users SET user_status = "Vlaselin" where user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_money = {case_money + 5} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_donate = {case_donate + 1} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET rating = {rating + 10000000} where user_id = {user_id}')
       cursor.execute(f'UPDATE users SET balance = {balance + 500000000000000} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "ВЛАСТЕЛИН 🤎" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET donate_coins = {donate_coins - 300} WHERE user_id = {user_id}') 
       connect.commit()
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас нехватает Donate-coins", parse_mode='html' )

@dp.callback_query_handler(text='vlastelin')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])



    vlaselin_menu = InlineKeyboardMarkup(row_width=1)
    cash_vlaselin = InlineKeyboardButton(text='🛒 Купить', callback_data='cash_vlaselin')
    
    vlaselin_menu.add(cash_vlaselin)
    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные за привилегию ВЛАСТЕЛИН 🤎

🛒 | При покупке:
        1️⃣ | Бонус-кит ВЛАСТЕЛИН
        2️⃣ | Префикс ВЛАСТЕЛИН
        3️⃣ | 50.000.000$
        4️⃣ | 150 Рейтинга
        5️⃣ | Money-case 5 шт.
        6️⃣ | Donate-case 1 шт.
        7️⃣ | Способность менять себе префикс
        8️⃣ | Способность менять игрокам префикс
        9️⃣ | Ограничение на время в играх становиться 2 секунды

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ВЛАСТЕЛИН
        2️⃣ | Префикс ВЛАСТЕЛИН
        3⃣ | Способность менять себе префикс
        4⃣ | Способность менять игрокам префикс
        5⃣ | Ограничение на время в играх становиться 2 секунды

🛒 Чтобы купить привилегию , виберите кнопку купить ниже
    """, reply_markup=vlaselin_menu,  parse_mode='html')


@dp.callback_query_handler(text='cash_bog')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    pref = cursor.execute("SELECT pref from users where user_id = ?",(callback.from_user.id,)).fetchone()
    pref = pref[0]
    
    case_donate = cursor.execute("SELECT case_donate from user_case where user_id = ?",(callback.from_user.id,)).fetchone()
    case_donate = int(case_donate[0])

    case_money = cursor.execute("SELECT case_money from user_case where user_id = ?",(callback.from_user.id,)).fetchone()
    case_money = int(case_money[0])
    
    balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
    balance = int(balance[0])
    
    rating = cursor.execute("SELECT rating from users where user_id = ?",(callback.from_user.id,)).fetchone()
    rating = int(rating[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])
    
    if donate_coins >= 300:
       await callback.message.answer( f"✅ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили привилегию БОГ", parse_mode='html' )
       cursor.execute(f'UPDATE users SET user_status = "Bog" where user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_money = {case_money + 5} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_donate = {case_donate + 1} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET rating = {rating + 10000000} where user_id = {user_id}')
       cursor.execute(f'UPDATE users SET balance = {balance + 500000000000000} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "БОГ 🤍" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET donate_coins = {donate_coins - 300} WHERE user_id = {user_id}') 
       connect.commit()
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас нехватает Donate-coins", parse_mode='html' )

@dp.callback_query_handler(text='bog')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])



    bog_menu = InlineKeyboardMarkup(row_width=1)
    cash_bog = InlineKeyboardButton(text='🛒 Купить', callback_data='cash_bog')
    
    bog_menu.add(cash_bog)
    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные за привилегию БОГ 🤍

🛒 | При покупке:
        1️⃣ | Бонус-кит БОГ
        2️⃣ | Префикс БОГ
        3️⃣ | 25.000.000$
        4️⃣ | 100 Рейтинга
        5️⃣ | Money-case 5 шт.
        6️⃣ | Donate-case 1 шт.
        7️⃣ | Способность менять себе префикс
        8️⃣ | Способность менять игрокам префикс
        9️⃣ | Ограничение на время в играх становиться 2 секунды

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит БОГ
        2️⃣ | Префикс БОГ
        3⃣ | Способность менять себе префикс
        4⃣ | Способность менять игрокам префикс
        5⃣ | Ограничение на время в играх становиться 2 секунды

🛒 Чтобы купить привилегию , виберите кнопку купить ниже
    """, reply_markup=bog_menu,  parse_mode='html')


@dp.callback_query_handler(text='cash_vladelec')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    pref = cursor.execute("SELECT pref from users where user_id = ?",(callback.from_user.id,)).fetchone()
    pref = pref[0]
    
    case_donate = cursor.execute("SELECT case_donate from user_case where user_id = ?",(callback.from_user.id,)).fetchone()
    case_donate = int(case_donate[0])

    case_money = cursor.execute("SELECT case_money from user_case where user_id = ?",(callback.from_user.id,)).fetchone()
    case_money = int(case_money[0])
    
    balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
    balance = int(balance[0])
    
    rating = cursor.execute("SELECT rating from users where user_id = ?",(callback.from_user.id,)).fetchone()
    rating = int(rating[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])
    
    if donate_coins >= 250:
       await callback.message.answer( f"✅ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили привилегию ВЛАДЕЛЕЦ  ", parse_mode='html' )
       cursor.execute(f'UPDATE users SET user_status = "Vladelec" where user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_money = {case_money + 5} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_donate = {case_donate + 1} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET rating = {rating + 1000000} where user_id = {user_id}')
       cursor.execute(f'UPDATE users SET balance = {balance + 100000000000000} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "ВЛАДЕЛЕЦ 🖤" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET donate_coins = {donate_coins - 250} WHERE user_id = {user_id}') 
       connect.commit()
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас нехватает Donate-coins", parse_mode='html' )

@dp.callback_query_handler(text='vladelec')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])



    vladelec_menu = InlineKeyboardMarkup(row_width=1)
    cash_vladelec = InlineKeyboardButton(text='🛒 Купить', callback_data='cash_vladelec')
    
    vladelec_menu.add(cash_vladelec)
    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> ,  вот данные за привилегию ВЛАДЕЛЕЦ 🖤

🛒 | При покупке:
        1️⃣ | Бонус-кит ВЛАДЕЛЕЦ
        2️⃣ | Префикс ВЛАДЕЛЕЦ
        3️⃣ | 10.000.000$
        4️⃣ | 74 Рейтинга
        5️⃣ | Money-case 5 шт.
        6️⃣ | Donate-case 1 шт.
        7️⃣ | Способность менять себе префикс
        8️⃣ | Способность менять игрокам префикс

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ВЛАДЕЛЕЦ
        2️⃣ | Префикс ВЛАДЕЛЕЦ
        3⃣ | Способность менять себе префикс
        4⃣ | Способность менять игрокам префикс

🛒 Чтобы купить привилегию , виберите кнопку купить ниже
    """, reply_markup=vladelec_menu,  parse_mode='html')


@dp.callback_query_handler(text='cash_osnovatel')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    pref = cursor.execute("SELECT pref from users where user_id = ?",(callback.from_user.id,)).fetchone()
    pref = pref[0]
    
    
    case_donate = cursor.execute("SELECT case_donate from user_case where user_id = ?",(callback.from_user.id,)).fetchone()
    case_donate = int(case_donate[0])
    
    case_money = cursor.execute("SELECT case_money from user_case where user_id = ?",(callback.from_user.id,)).fetchone()
    case_money = int(case_money[0])
    
    balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
    balance = int(balance[0])
    
    rating = cursor.execute("SELECT rating from users where user_id = ?",(callback.from_user.id,)).fetchone()
    rating = int(rating[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])
    
    if donate_coins >= 170:
       await callback.message.answer( f"✅ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили привилегию ОСНОВАТЕЛЬ ", parse_mode='html' )
       cursor.execute(f'UPDATE users SET user_status = "Osnovatel" where user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_money = {case_money + 5} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_donate = {case_donate + 1} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET rating = {rating + 100000} where user_id = {user_id}')
       cursor.execute(f'UPDATE users SET balance = {balance + 20000000000000} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "ОСНОВАТЕЛЬ 💜" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET donate_coins = {donate_coins - 170} WHERE user_id = {user_id}') 
       connect.commit()
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас нехватает Donate-coins", parse_mode='html' )

@dp.callback_query_handler(text='osnovatel')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])



    osnovatel_menu = InlineKeyboardMarkup(row_width=1)
    cash_osnovatel = InlineKeyboardButton(text='🛒 Купить', callback_data='cash_osnovatel')
    
    osnovatel_menu.add(cash_osnovatel)
    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные за привилегию ОСНОВАТЕЛЬ 💜

🛒 | При покупке:
        1️⃣ | Бонус-кит ОСНОВАТЕЛЬ
        2️⃣ | Префикс ОСНОВАТЕЛЬ
        3️⃣ | 4.000.000$
        4️⃣ | 54 Рейтинга
        5️⃣ | Money-case 5 шт.
        6️⃣ | Donate-case 1 шт.
        7️⃣ | Способность менять себе префикс

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ОСНОВАТЕЛЬ
        2️⃣ | Префикс ОСНОВАТЕЛЬ
        3⃣ | Способность менять себе префикс

🛒 Чтобы купить привилегию , виберите кнопку купить ниже
    """, reply_markup=osnovatel_menu,  parse_mode='html')


@dp.callback_query_handler(text='cash_sponsor')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    pref = cursor.execute("SELECT pref from users where user_id = ?",(callback.from_user.id,)).fetchone()
    pref = pref[0]
    
    
    case_money = cursor.execute("SELECT case_money from user_case where user_id = ?",(callback.from_user.id,)).fetchone()
    case_money = int(case_money[0])
    
    balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
    balance = int(balance[0])
    
    rating = cursor.execute("SELECT rating from users where user_id = ?",(callback.from_user.id,)).fetchone()
    rating = int(rating[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])
    
    if donate_coins >= 155:
       await callback.message.answer( f"✅ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили привилегию СПОНСОР", parse_mode='html' )
       cursor.execute(f'UPDATE users SET user_status = "Sponsor" where user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_money = {case_money + 5} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET rating = {rating + 10000} where user_id = {user_id}')
       cursor.execute(f'UPDATE users SET balance = {balance + 5000000000000} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "СПОНСОР 💙" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET donate_coins = {donate_coins - 155} WHERE user_id = {user_id}') 
       connect.commit()
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас нехватает Donate-coins", parse_mode='html' )

@dp.callback_query_handler(text='sponsor')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])



    sponsor_menu = InlineKeyboardMarkup(row_width=1)
    cash_sponsor = InlineKeyboardButton(text='🛒 Купить', callback_data='cash_sponsor')
    
    sponsor_menu.add(cash_sponsor)
    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные за привилегию СПОНСОР 💙

🛒 | При покупке:
        1️⃣ | Бонус-кит СПОНСОР
        2️⃣ | Префикс СПОНСОР
        3️⃣ | 3.000.000$
        4️⃣ | 25 Рейтинга
        5️⃣ | Money-case 5 шт.
        6️⃣ | Способность менять себе префикс

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит СПОНСОР
        2️⃣ | Префикс СПОНСОР
        3⃣ | Способность менять себе префикс

🛒 Чтобы купить привилегию , виберите кнопку купить ниже
    """, reply_markup=sponsor_menu,  parse_mode='html')



@dp.callback_query_handler(text='cash_helper')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    pref = cursor.execute("SELECT pref from users where user_id = ?",(callback.from_user.id,)).fetchone()
    pref = pref[0]
    
    
    case_money = cursor.execute("SELECT case_money from user_case where user_id = ?",(callback.from_user.id,)).fetchone()
    case_money = int(case_money[0])
    
    balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
    balance = int(balance[0])
    
    rating = cursor.execute("SELECT rating from users where user_id = ?",(callback.from_user.id,)).fetchone()
    rating = int(rating[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])
    
    if donate_coins >= 100:
       await callback.message.answer( f"✅ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили привилегию ХЕЛПЕР", parse_mode='html' )
       cursor.execute(f'UPDATE users SET user_status = "Helper" where user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_money = {case_money + 3} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET rating = {rating + 1300} where user_id = {user_id}')
       cursor.execute(f'UPDATE users SET balance = {balance + 700000000000} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "ХЕЛПЕР 💚" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET donate_coins = {donate_coins - 100} WHERE user_id = {user_id}') 
       connect.commit()
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас нехватает Donate-coins", parse_mode='html' )

@dp.callback_query_handler(text='helper')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])



    helper_menu = InlineKeyboardMarkup(row_width=1)
    cash_helper = InlineKeyboardButton(text='🛒 Купить', callback_data='cash_helper')
    
    helper_menu.add(cash_helper)
    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные за привилегию ХЕЛПЕР 💚

🛒 | При покупке:
        1️⃣ | Бонус-кит ХЕЛПЕР
        2️⃣ | Префикс ХЕЛПЕР
        3️⃣ | 750.000$
        4️⃣ | 20 Рейтинга
        5️⃣ | Money-case 3 шт.
        6️⃣ | Способность менять себе префикс

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ХЕЛПЕР
        2️⃣ | Префикс ХЕЛПЕР
        3⃣ | Способность менять себе префикс

🛒 Чтобы купить привилегию , виберите кнопку купить ниже
    """, reply_markup=helper_menu,  parse_mode='html')


@dp.callback_query_handler(text='cash_platina')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    pref = cursor.execute("SELECT pref from users where user_id = ?",(callback.from_user.id,)).fetchone()
    pref = pref[0]
    
    
    case_money = cursor.execute("SELECT case_money from user_case where user_id = ?",(callback.from_user.id,)).fetchone()
    case_money = int(case_money[0])
    
    balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
    balance = int(balance[0])
    
    rating = cursor.execute("SELECT rating from users where user_id = ?",(callback.from_user.id,)).fetchone()
    rating = int(rating[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])
    
    if donate_coins >= 50:
       await callback.message.answer( f"✅ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили привилегию ПЛАТИНА", parse_mode='html' )
       cursor.execute(f'UPDATE users SET user_status = "Platina" where user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_money = {case_money + 1} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET rating = {rating + 800} where user_id = {user_id}')
       cursor.execute(f'UPDATE users SET balance = {balance + 400000000000} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "ПЛАТИНА 💛" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET donate_coins = {donate_coins - 50} WHERE user_id = {user_id}') 
       connect.commit()
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас нехватает Donate-coins", parse_mode='html' )

@dp.callback_query_handler(text='platina')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])



    platina_menu = InlineKeyboardMarkup(row_width=1)
    cash_platina = InlineKeyboardButton(text='🛒 Купить', callback_data='cash_platina')
    
    platina_menu.add(cash_platina)
    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные за привилегию ПЛАТИНА 💛

🛒 | При покупке:
        1️⃣ | Бонус-кит ПЛАТИНА
        2️⃣ | Префикс ПЛАТИНА
        3️⃣ | 550.000$
        4️⃣ | 10 Рейтинга
        5️⃣ | Money-case 1 шт.

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ПЛАТИНА
        2️⃣ | Префикс ПЛАТИНА

🛒 Чтобы купить привилегию , виберите кнопку купить ниже
    """, reply_markup=platina_menu,  parse_mode='html')


@dp.callback_query_handler(text='cash_premium')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    pref = cursor.execute("SELECT pref from users where user_id = ?",(callback.from_user.id,)).fetchone()
    pref = pref[0]
    
    balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
    balance = int(balance[0])
    
    rating = cursor.execute("SELECT rating from users where user_id = ?",(callback.from_user.id,)).fetchone()
    rating = int(rating[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])
    
    if donate_coins >= 30:
       await callback.message.answer( f"✅ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили привилегию ПРЕМИУМ", parse_mode='html' )
       cursor.execute(f'UPDATE users SET user_status = "Premium" where user_id = {user_id}')
       cursor.execute(f'UPDATE users SET rating = {rating + 300} where user_id = {user_id}')
       cursor.execute(f'UPDATE users SET balance = {balance + 100000000000} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "ПРЕМИУМ 🧡" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET donate_coins = {donate_coins - 30} WHERE user_id = {user_id}') 
       connect.commit()
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас нехватает Donate-coins", parse_mode='html' )

@dp.callback_query_handler(text='premium')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])



    premium_menu = InlineKeyboardMarkup(row_width=1)
    cash_premium = InlineKeyboardButton(text='🛒 Купить', callback_data='cash_premium')
    
    premium_menu.add(cash_premium)
    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные за привилегию ПРЕМИУМ 🧡

🛒 | При покупке:
        1️⃣ | Бонус-кит ПРЕМИУМ
        2️⃣ | Префикс ПРЕМИУМ
        3️⃣ | 300.000$

🎁 | При использовании Donate-Case:
        1️⃣ | Бонус-кит ПРЕМИУМ
        2️⃣ | Префикс ПРЕМИУМ

🛒 Чтобы купить привилегию , виберите кнопку купить ниже
    """, reply_markup=premium_menu,  parse_mode='html')


@dp.callback_query_handler(text='cash_vip')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    pref = cursor.execute("SELECT pref from users where user_id = ?",(callback.from_user.id,)).fetchone()
    pref = pref[0]
    
    balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
    balance = int(balance[0])
    
    rating = cursor.execute("SELECT rating from users where user_id = ?",(callback.from_user.id,)).fetchone()
    rating = int(rating[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])
    
    if donate_coins >= 10:
       await callback.message.answer( f"✅ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили привилегию ВИП", parse_mode='html' )
       cursor.execute(f'UPDATE users SET user_status = "Vip" where user_id = {user_id}')
       cursor.execute(f'UPDATE users SET rating = {rating + 100} where user_id = {user_id}')
       cursor.execute(f'UPDATE users SET balance = {balance + 10000000000} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "ВИП ❤️" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET donate_coins = {donate_coins - 10} WHERE user_id = {user_id}') 
       connect.commit()
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас нехватает Donate-coins", parse_mode='html' )

@dp.callback_query_handler(text='vip')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])



    vip_menu = InlineKeyboardMarkup(row_width=1)
    cash_vip = InlineKeyboardButton(text='🛒 Купить', callback_data='cash_vip')
    
    vip_menu.add(cash_vip)
    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные за привилегию ВИП ❤️

🛒 | При покупке:
        1️⃣ | Бонус-кит ВИП
        2️⃣ | Префикс ВИП
        3️⃣ | 250.000$

🎁 | При использовании Donate-Case:
       1️⃣ | Бонус-кит ВИП
       2️⃣ | Префикс ВИП

🛒 Чтобы купить привилегию , виберите кнопку купить ниже
    """, reply_markup=vip_menu,  parse_mode='html')

@dp.callback_query_handler(text='privilegii')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    
    privilegii_inline = InlineKeyboardMarkup(row_width=3)
    vip = InlineKeyboardButton(text='❤️ ВИП ', callback_data='vip')
    premium = InlineKeyboardButton(text='🧡 ПРЕМИУМ', callback_data='premium')
    platina = InlineKeyboardButton(text='💛 ПЛАТИНА', callback_data='platina')
    helper = InlineKeyboardButton(text='💚 ХЕЛПЕР', callback_data='helper')
    sponsor = InlineKeyboardButton(text='💙 СПОНСОР', callback_data='sponsor')
    osnovatel = InlineKeyboardButton(text='💜 ОСНОВАТЕЛЬ', callback_data='osnovatel')
    vladelec = InlineKeyboardButton(text='🖤 ВЛАДЕЛЕЦ', callback_data='vladelec')
    bog = InlineKeyboardButton(text='🤍 БОГ', callback_data='bog')
    vlastelin = InlineKeyboardButton(text='🤎 ВЛАСТЕЛИН', callback_data='vlastelin')
    privilegii_inline.add(vip, premium, platina, helper, sponsor, osnovatel, vladelec, bog, vlastelin)
    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот все доступные привилегии📝

❤️ | ВИП - 10 Donate-coins 🪙
🧡 | ПРЕМИУМ - 30 Donate-coins 🪙
💛 | ПЛАТИНА - 50 Donate-coins 🪙
💚 | ХЕЛПЕР - 100 Donate-coins 🪙
💙 | СПОНСОР - 155 Donate-coins 🪙
💜 | ОСНОВАТЕЛЬ - 170 Donate-coins 🪙
🖤 | ВЛАДЕЛЕЦ - 250  Donate-coins 🪙
🤍 | БОГ - 300 Donate-coins 🪙
🤎 | ВЛАСТЕЛИН - 350 Donate-coins 🪙

🛒 Чтобы купить привилегию , виберите её ниже
ℹ️ Чтобы посмотреть возможности привилегий , виберите привилегию ниже   
    """, reply_markup=privilegii_inline,  parse_mode='html')

@dp.callback_query_handler(text='money_case_cash1')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])

    money_case = cursor.execute(f'SELECT case_money from user_case where user_id = {user_id}').fetchone()
    money_case = int(money_case[0])

    if donate_coins >= 50:
       await callback.message.answer(f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купил 1 Money-Case", parse_mode='html')
       cursor.execute(f'UPDATE user_case SET case_money = {money_case + 1} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET donate_coins = {donate_coins - 50} WHERE user_id = {user_id}')
       connect.commit()
       return
    else:
       await callback.message.answer(f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас не достаточно Donate-Coins 🪙", parse_mode='html')




@dp.callback_query_handler(text='money_case')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])

    money_case_cash = InlineKeyboardMarkup(row_width=2)
    money_case_cash1 = InlineKeyboardButton(text='🛒 Купить кейс', callback_data='money_case_cash1')
    money_case_cash.add(money_case_cash1)

    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные за Money-Case 💸

ℹ️ | В 1 Money-Case выпадает от 0$ и до 999гугл.

🛒 Чтобы купить нажмите кнопку ниже 🔽
    """, reply_markup=money_case_cash,  parse_mode='html')


@dp.callback_query_handler(text='up_money_case')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    money_case = cursor.execute(f'SELECT case_money from user_case where user_id = {user_id}').fetchone()
    money_case = int(money_case[0])

    balance = cursor.execute(f'SELECT balance from users where user_id = {user_id}').fetchone()
    balance = int(balance[0])

    if money_case < 1:
       await callback.message.answer( f"🆘 | Игрок, у вас нету Money кейсов", parse_mode='html')
       return
       
    rx = random.randint(0, 100000000000000000000000000000)
    rx2 = '{:,}'.format(rx)

    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вы открыли Money-Case 💸

🔎 | Результат: {rx2}$    
    """, parse_mode='html')
    cursor.execute(f'UPDATE users SET balance = {balance + rx} WHERE user_id = {user_id}')
    cursor.execute(f'UPDATE user_case SET case_money = {money_case - 1} WHERE user_id = {user_id}')
    connect.commit()

@dp.callback_query_handler(text='up_donate_case')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_case = cursor.execute(f'SELECT case_donate from user_case where user_id = {user_id}').fetchone()
    donate_case = int(donate_case[0])

    if donate_case < 1:
       await callback.message.answer( f"🆘 | Игрок, у вас нету Донат кейсов", parse_mode='html')
       return
   
    rx = random.randint(0, 935)

    if int(rx) in range(0,500):
       await callback.message.answer( f"""
⏳ | <i>Открытия кейса .....</i>      
       """, parse_mode='html')
       time.sleep(2)
       await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно выбили с донат кейса - <b>💚 ХЕЛПЕР</b>    
       """, parse_mode='html')
       cursor.execute(f'UPDATE users SET user_status = "Helper" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "ХЕЛПЕР 💚" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_donate = {donate_case - 1} WHERE user_id = {user_id}')
       connect.commit()
    if int(rx) in range(501,750):
       await callback.message.answer( f"""
⏳ | <i>Открытия кейса .....</i>      
       """, parse_mode='html')
       time.sleep(2)
       await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно выбили с донат кейса - <b>💙 СПОНСОР</b>    
       """, parse_mode='html')
       cursor.execute(f'UPDATE users SET user_status = "Sponsor" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "СПОНСОР 💙" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_donate = {donate_case - 1} WHERE user_id = {user_id}')
       connect.commit()
    if int(rx) in range(751,850):
       await callback.message.answer( f"""
⏳ | <i>Открытия кейса .....</i>      
       """, parse_mode='html')
       time.sleep(2)
       await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно выбили с донат кейса - <b>💜 ОСНОВАТЕЛЬ</b>    
       """, parse_mode='html')
       cursor.execute(f'UPDATE users SET user_status = "Osnovatel" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "ОСНОВАТЕЛЬ 💜" WHERE user_id = {user_id}')
       connect.commit()
    if int(rx) in range(851,900):
       await callback.message.answer( f"""
⏳ | <i>Открытия кейса .....</i>      
       """, parse_mode='html')
       time.sleep(2)
       await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно выбили с донат кейса - <b>🖤 ВЛАДЕЛЕЦ</b>    
       """, parse_mode='html')
       cursor.execute(f'UPDATE users SET user_status = "Vladelec" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "ВЛАДЕЛЕЦ 🖤" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_donate = {donate_case - 1} WHERE user_id = {user_id}')
       connect.commit()
    if int(rx) in range(901,925):
       await callback.message.answer( f"""
⏳ | <i>Открытия кейса .....</i>      
       """, parse_mode='html')
       time.sleep(2)
       await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно выбили с донат кейса - <b>🤍 БОГ</b>    
       """, parse_mode='html')
       cursor.execute(f'UPDATE users SET user_status = "Bog" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "БОГ 🤍" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_donate = {donate_case - 1} WHERE user_id = {user_id}')
       connect.commit()
    if int(rx) in range(925,935):
       await callback.message.answer( f"""
⏳ | <i>Открытия кейса .....</i>      
       """, parse_mode='html')
       time.sleep(2)
       await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно выбили с донат кейса - <b>🤎 ВЛАСТЕЛИН</b>    
       """, parse_mode='html')
       cursor.execute(f'UPDATE users SET user_status = "Vlaselin" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET pref = "ВЛАСТЕЛИН 🤎" WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE user_case SET case_donate = {donate_case - 1} WHERE user_id = {user_id}')
       connect.commit()
@dp.callback_query_handler(text='donate_case_cash1')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])

    donate_case = cursor.execute(f'SELECT case_donate from user_case where user_id = {user_id}').fetchone()
    donate_case = int(donate_case[0])

    if donate_coins >= 100:
       await callback.message.answer(f"🧧 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купил 1 Donate-Case", parse_mode='html')
       cursor.execute(f'UPDATE user_case SET case_donate = {donate_case + 1} WHERE user_id = {user_id}')
       cursor.execute(f'UPDATE users SET donate_coins = {donate_coins - 100} WHERE user_id = {user_id}')
       connect.commit()
       return
    else:
       await callback.message.answer(f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас не достаточно Donate-Coins 🪙", parse_mode='html')


@dp.callback_query_handler(text='donate_case')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(callback.from_user.id,)).fetchone()
    donate_coins = int(donate_coins[0])

    donate_case_cash = InlineKeyboardMarkup(row_width=2)
    donate_case_cash1 = InlineKeyboardButton(text='🛒 Купить кейс', callback_data='donate_case_cash1')
    donate_case_cash.add(donate_case_cash1)

    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные за Donate-Case 🧧

ℹ️ | В 1 Donate-Case падает рандомно случайная привилегия!

🛒 Чтобы купить нажмите кнопку ниже 🔽
    """, reply_markup=donate_case_cash,  parse_mode='html')

@dp.callback_query_handler(text='case')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    case_shop = InlineKeyboardMarkup(row_width=2)
    money_case1 = InlineKeyboardButton(text='💸 Money-Case', callback_data='money_case')
    donate_case2 = InlineKeyboardButton(text='🧧 Donate-Case', callback_data='donate_case')
    case_shop.add(money_case1, donate_case2)

    money_case = cursor.execute(f'SELECT case_money from user_case where user_id = {user_id}').fetchone()
    money_case = int(money_case[0])

    donate_case = cursor.execute(f'SELECT case_donate from user_case where user_id = {user_id}').fetchone()
    donate_case = int(donate_case[0])
    
    ob_members = 0

    if donate_case > 0:
       ob_members += 1
       donate_case2 = f'      🧧 | Donate-Case - {donate_case} шт.\n'
    else:
       donate_case2 = ''

    if money_case > 0:
       ob_members += 1
       money_case2 = f'      💸 | Money-Case - {money_case} шт.\n'
    else:
       money_case2 = ''
   
    if ob_members > 0:
       casee = '🎁 | Ваши кейсы:\n'
    else:
       casee = '😟 | У вас нету кейсов...'

    await callback.message.answer( f"""
<a href='tg://user?id={user_id}'>{user_name}</a> , вот данные за кейсы 🎁

💸 | Money-Case - 50 Donate-Coins 🪙
🧧 | Donate-Case - 100 Donate-Coins 🪙

{casee}{money_case2}{donate_case2}

🛒 Чтобы купить\посмотреть информацию, виберите кнопку ниже ⬇️  
    """, reply_markup=case_shop,  parse_mode='html')
 

@dp.callback_query_handler(text='resurs4')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    basement = cursor.execute("SELECT basement from house where user_id = ?",(callback.from_user.id,)).fetchone()
    basement = int(basement[0])

    iron = cursor.execute("SELECT iron from mine where user_id = ?",(callback.from_user.id,)).fetchone()
    iron = int(iron[0])

    metall = cursor.execute("SELECT metall from mine where user_id = ?",(callback.from_user.id,)).fetchone()
    metall = int(metall[0])

    linen = cursor.execute("SELECT linen from farm where user_id = ?",(callback.from_user.id,)).fetchone()
    linen = int(linen[0])

    cotton = cursor.execute("SELECT cotton from farm where user_id = ?",(callback.from_user.id,)).fetchone()
    cotton = int(cotton[0])


    #rake, pick
    rake = cursor.execute("SELECT rake from farm where user_id = ?", (callback.from_user.id,)).fetchone()
    rake = rake[0]

    pick = cursor.execute("SELECT pick from mine where user_id = ?", (callback.from_user.id,)).fetchone()
    pick = pick[0]
    
    if basement == 1:
       basement_period = 30
   
    if basement == 2:
       basement_period = 15

    if basement == 3:
       basement_period = 4
    
    rx = random.randint(0,1000)

    getе = cursor.execute("SELECT time_craft FROM bot_time WHERE user_id = ?", (callback.from_user.id,)).fetchone()
    last_stavka = int(getе[0])
    stavkatime = time.time() - float(last_stavka)
    if basement > 0:
       if stavkatime > basement_period:
          if int(rx) in range(0,900):
             await callback.message.answer( f"👨 |Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Крафт предмета\n📦 | Предмет: Грабли Cherick 🌾\n💈 |Результат: Провал ❌", parse_mode='html')
             cursor.execute(f'UPDATE bot_time SET time_craft = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             await bot.answer_callback_query(callback.id)
          if int(rx) in range(901,1000):
             await callback.message.answer(  f"👨 |Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Крафт предмета\n📦 | Предмет: Грабли Cherick 🌾\n💈 |Результат: Успешно ✅", parse_mode='html')
             await callback.message.answer(  f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы получили предмет: Грабли Cherick 🌾\n🔱 | Уникальность: Х2 Добыча ресурсов, Ограничение на время снимаеться на 50%", parse_mode='html')
             cursor.execute(f'UPDATE bot_time SET time_craft = {time.time()} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE farm SET rake = "Cherick" WHERE user_id = {user_id}')
             connect.commit()
             await bot.answer_callback_query(callback.id)
       else:
          await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! С вашим подвалом можно крафтить раз в {basement_period} секунд", parse_mode='html')
          await bot.answer_callback_query(callback.id)
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Крафтить можно только с подвалом", parse_mode='html')
       await bot.answer_callback_query(callback.id)


@dp.callback_query_handler(text='resurs3')
async def craft_resurs3(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    basement = cursor.execute("SELECT basement from house where user_id = ?",(callback.from_user.id,)).fetchone()
    basement = int(basement[0])

    iron = cursor.execute("SELECT iron from mine where user_id = ?",(callback.from_user.id,)).fetchone()
    iron = int(iron[0])

    metall = cursor.execute("SELECT metall from mine where user_id = ?",(callback.from_user.id,)).fetchone()
    metall = int(metall[0])

    linen = cursor.execute("SELECT linen from farm where user_id = ?",(callback.from_user.id,)).fetchone()
    linen = int(linen[0])

    cotton = cursor.execute("SELECT cotton from farm where user_id = ?",(callback.from_user.id,)).fetchone()
    cotton = int(cotton[0])


    #rake, pick
    rake = cursor.execute("SELECT rake from farm where user_id = ?", (callback.from_user.id,)).fetchone()
    rake = rake[0]

    pick = cursor.execute("SELECT pick from mine where user_id = ?", (callback.from_user.id,)).fetchone()
    pick = pick[0]
    
    if basement == 1:
       basement_period = 30
   
    if basement == 2:
       basement_period = 15

    if basement == 3:
       basement_period = 4
    
    rx = random.randint(0,1000)

    getе = cursor.execute("SELECT time_craft FROM bot_time WHERE user_id = ?", (callback.from_user.id,)).fetchone()
    last_stavka = int(getе[0])
    stavkatime = time.time() - float(last_stavka)
    if basement > 0:
       if stavkatime > basement_period:
          if int(rx) in range(0,900):
             await callback.message.answer( f"👨 |Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Крафт предмета\n📦 | Предмет: Кирка Cherick ⛏\n💈 |Результат: Провал ❌", parse_mode='html')
             cursor.execute(f'UPDATE bot_time SET time_craft = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             await bot.answer_callback_query(callback.id)
          if int(rx) in range(901,1000):
             await callback.message.answer(  f"👨 |Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Крафт предмета\n📦 | Предмет: Кирка Cherick ⛏\n💈 |Результат: Успешно ✅", parse_mode='html')
             await callback.message.answer(  f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы получили предмет: Кирка Cherick ⛏\n🔱 | Уникальность: Х2 Добыча ресурсов, Ограничение на время снимаеться на 50%", parse_mode='html')
             cursor.execute(f'UPDATE bot_time SET time_craft = {time.time()} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET pick = "Cherick" WHERE user_id = {user_id}')
             connect.commit()
             await bot.answer_callback_query(callback.id)
       else:
          await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! С вашим подвалом можно крафтить раз в {basement_period} секунд", parse_mode='html')
          await bot.answer_callback_query(callback.id)
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Крафтить можно только с подвалом", parse_mode='html')
       await bot.answer_callback_query(callback.id)


@dp.callback_query_handler(text='resurs2')
async def craft_resurs2(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    basement = cursor.execute("SELECT basement from house where user_id = ?",(callback.from_user.id,)).fetchone()
    basement = int(basement[0])

    iron = cursor.execute("SELECT iron from mine where user_id = ?",(callback.from_user.id,)).fetchone()
    iron = int(iron[0])

    metall = cursor.execute("SELECT metall from mine where user_id = ?",(callback.from_user.id,)).fetchone()
    metall = int(metall[0])

    linen = cursor.execute("SELECT linen from farm where user_id = ?",(callback.from_user.id,)).fetchone()
    linen = int(linen[0])

    cotton = cursor.execute("SELECT cotton from farm where user_id = ?",(callback.from_user.id,)).fetchone()
    cotton = int(cotton[0])


    #rake, pick
    rake = cursor.execute("SELECT rake from farm where user_id = ?", (callback.from_user.id,)).fetchone()
    rake = rake[0]

    pick = cursor.execute("SELECT pick from mine where user_id = ?", (callback.from_user.id,)).fetchone()
    pick = pick[0]
    
    if basement == 1:
       basement_period = 30
   
    if basement == 2:
       basement_period = 15

    if basement == 3:
       basement_period = 4
    
    rx = random.randint(0,1000)

    getе = cursor.execute("SELECT time_craft FROM bot_time WHERE user_id = ?", (callback.from_user.id,)).fetchone()
    last_stavka = int(getе[0])
    stavkatime = time.time() - float(last_stavka)
    if basement > 0:
       if stavkatime > basement_period:
          if int(rx) in range(0,750):
             await callback.message.answer( f"👨 |Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Крафт предмета\n📦 | Предмет: Грабли Zerro 🌾\n💈 |Результат: Провал ❌", parse_mode='html')
             cursor.execute(f'UPDATE bot_time SET time_craft = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             await bot.answer_callback_query(callback.id)
          if int(rx) in range(751,1000):
             await callback.message.answer(  f"👨 |Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Крафт предмета\n📦 | Предмет: Грабли Zerro 🌾\n💈 |Результат: Успешно ✅", parse_mode='html')
             await callback.message.answer(  f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы получили предмет: Грабли Zerro 🌾\n🔱 | Уникальность: Х2 Добыча ресурсов", parse_mode='html')
             cursor.execute(f'UPDATE bot_time SET time_craft = {time.time()} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE farm SET rake = "Zerro" WHERE user_id = {user_id}')
             connect.commit()
             await bot.answer_callback_query(callback.id)
       else:
          await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! С вашим подвалом можно крафтить раз в {basement_period} секунд", parse_mode='html')
          await bot.answer_callback_query(callback.id)
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Крафтить можно только с подвалом", parse_mode='html')
       await bot.answer_callback_query(callback.id)


@dp.callback_query_handler(text='resurs1')
async def craft_resurs1(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    basement = cursor.execute("SELECT basement from house where user_id = ?",(callback.from_user.id,)).fetchone()
    basement = int(basement[0])

    iron = cursor.execute("SELECT iron from mine where user_id = ?",(callback.from_user.id,)).fetchone()
    iron = int(iron[0])

    metall = cursor.execute("SELECT metall from mine where user_id = ?",(callback.from_user.id,)).fetchone()
    metall = int(metall[0])

    linen = cursor.execute("SELECT linen from farm where user_id = ?",(callback.from_user.id,)).fetchone()
    linen = int(linen[0])

    cotton = cursor.execute("SELECT cotton from farm where user_id = ?",(callback.from_user.id,)).fetchone()
    cotton = int(cotton[0])


    #rake, pick
    rake = cursor.execute("SELECT rake from farm where user_id = ?", (callback.from_user.id,)).fetchone()
    rake = rake[0]

    pick = cursor.execute("SELECT pick from mine where user_id = ?", (callback.from_user.id,)).fetchone()
    pick = pick[0]
    
    if basement == 1:
       basement_period = 30
   
    if basement == 2:
       basement_period = 15

    if basement == 3:
       basement_period = 4
    
    rx = random.randint(0,1000)

    getе = cursor.execute("SELECT time_craft FROM bot_time WHERE user_id = ?", (callback.from_user.id,)).fetchone()
    last_stavka = int(getе[0])
    stavkatime = time.time() - float(last_stavka)
    if basement > 0:
       if stavkatime > basement_period:
          if int(rx) in range(0,750):
             await callback.message.answer( f"👨 |Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Крафт предмета\n📦 | Предмет: Кирка Zerro ⛏\n💈 |Результат: Провал ❌", parse_mode='html')
             cursor.execute(f'UPDATE bot_time SET time_craft = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             await bot.answer_callback_query(callback.id)
          if int(rx) in range(751,1000):
             await callback.message.answer(  f"👨 |Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ |Действие: Крафт предмета\n📦 | Предмет: Кирка Zerro ⛏\n💈 |Результат: Успешно ✅", parse_mode='html')
             await callback.message.answer(  f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы получили предмет: Кирка Zerro⛏\n🔱 | Уникальность: Х2 Добыча ресурсов", parse_mode='html')
             cursor.execute(f'UPDATE bot_time SET time_craft = {time.time()} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET pick = "Zerro" WHERE user_id = {user_id}')
             connect.commit()
             await bot.answer_callback_query(callback.id)
       else:
          await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! С вашим подвалом можно крафтить раз в {basement_period} секунд", parse_mode='html')
          await bot.answer_callback_query(callback.id)
    else:
       await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Крафтить можно только с подвалом", parse_mode='html')
       await bot.answer_callback_query(callback.id)


@dp.callback_query_handler(text='Priv2')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a> , вот все доступные привилегии📝

❤️ | ВИП
🧡 | ПРЕМИУМ 
💛 | ПЛАТИНА
💚 | ХЕЛПЕР 
💙 | СПОНСОР 
💜 | ОСНОВАТЕЛЬ 
🖤 | ВЛАДЕЛЕЦ 
🤍 | БОГ
🤎 | ВЛАСТЕЛИН

ℹ️ Что бы использовать команду , напишите команду сообщением
    ''', parse_mode='html')

@dp.callback_query_handler(text='Im2')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, вот все команды на имущество📝

🏠 | Дома
         🏡 Мой дом 
         🏡 Купить подвал [номер]
         🏡 Продать подвал 
         🏡 Крафтить 
         🏡 Система крафта 

🚘 | Машины
        🚗 Моя машина
        🚗 Заправить 
        🚗 Поченить

ℹ️ Что бы использовать команду , напишите команду сообщением
    ''', parse_mode='html')

@dp.callback_query_handler(text='rabot2')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, вот список работних команд📝

⛏ | Шахта
      Купить кирку ⛏
      Копать руду ⛏
      Продать [название руды] [количество] ⛏

🌾 | Ферма 
      Купить грабли 🌾
      Собрать [название урожая] 🌾
      Продать [название урожая] [количество] 🌾

ℹ️ Что бы использовать команду , напишите команду сообщением
    ''', parse_mode='html')

@dp.callback_query_handler(text='game2')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, вот список игровых команд 📝

🧊 | /gamevb - ВБ
⚽️ | Футбол\Фб [ставка]
🎱 | Dice [ч\к] [ставка] - Wheel
🤵‍♀️ | Казино [сумма]
◾️ | Плинко [сумма]
🎰 | Спин [сумма]
🎲 | Кубик [число] [сумма]
🎲 | Чётное\нечётное [сумма]
🏎 | Гонка [сумма]

ℹ️ Что бы использовать команду , напишите команду сообщением
    ''', parse_mode='html')

@dp.callback_query_handler(text='admins_comands')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = str(user_status[0]) 
    if user_status == 'Owner':
       commands = '''
1️⃣ | Выдать [сумма]
2️⃣ | Забрать [сумма]
3️⃣ | Умножить [количество]
4️⃣ | Обнулить
5️⃣ | /ban
6️⃣ | /unban
7️⃣ |Выдать админа
8️⃣ | Выдать хелпера
9️⃣ | Передать права
🔟 | Забрать права
1️⃣1️⃣ | /reset
1️⃣2️⃣ | /warn
1️⃣3️⃣ | reset_id [ID]
1️⃣4️⃣ | /info
1️⃣5️⃣ | /info_id [ID]
1️⃣6️⃣ | Поделить [количество]
1️⃣7️⃣ | /ban_id [ID]
1️⃣8️⃣ | /unban_id [ID]
1️⃣9️⃣ | /warn_id [ID]
2️⃣0️⃣ | /unwarn_id [ID]

       '''
    if user_status == 'Helper_Admin':
       commands = '''
1️⃣ | Выдать [сумма]
2️⃣ | Забрать [сумма]
3️⃣ | Умножить [количество]
4️⃣ | Обнулить
5️⃣ | /ban
6️⃣ | /unban
7️⃣ | /warn
8️⃣ | reset_id [ID]
9️⃣ | /info
🔟 | /info_id [ID]
1️⃣1️⃣ | Поделить [количество]
1️⃣2️⃣ | /ban_id [ID]
1️⃣3️⃣ | /unban_id [ID]
1️⃣4️⃣ | /warn_id [ID]
1️⃣5️⃣ | /unwarn_id [ID]


       '''
    if user_status == 'Admin':
       commands = '''
1️⃣ | Выдать [сумма]
2️⃣ | Забрать [сумма]
3️⃣ | Умножить [количество]
4️⃣ | Обнулить
5️⃣ | /info
6️⃣ | Поделить [количество]
       '''
    if user_status == 'Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот список администраторских команд 📝\n{commands}", parse_mode='html')
       return
    if user_status == 'Helper_Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот список администраторских команд 📝\n{commands}", parse_mode='html')
       return
    if user_status == 'Owner':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот список администраторских команд 📝\n{commands}", parse_mode='html')
       return
    else:
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>,Вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику <a href='t.me/haeshka_qwe_per/'>Хаешка</a>  ⚠️", parse_mode='html')

@dp.callback_query_handler(text='stats222')
async def ob_Statisyik(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = user_status[0]

    sqlite_select_query21 = """SELECT * from users where user_status = \"Vip\""""
    cursor.execute(sqlite_select_query21)
    vip = cursor.fetchall()

    sqlite_select_query22 = """SELECT * from users where user_status = \"Premium\""""
    cursor.execute(sqlite_select_query22)
    premium = cursor.fetchall()

    sqlite_select_query23 = """SELECT * from users where user_status = \"Platina\""""
    cursor.execute(sqlite_select_query23)
    platina = cursor.fetchall()

    sqlite_select_query24 = """SELECT * from users where user_status = \"Helper\""""
    cursor.execute(sqlite_select_query24)
    helper = cursor.fetchall()

    sqlite_select_query25 = """SELECT * from users where user_status = \"Sponsor\""""
    cursor.execute(sqlite_select_query25)
    sponsor = cursor.fetchall()

    sqlite_select_query26 = """SELECT * from users where user_status = \"Osnovatel\""""
    cursor.execute(sqlite_select_query26)
    osnovatel = cursor.fetchall()

    sqlite_select_query27 = """SELECT * from users where user_status = \"Vladelec\""""
    cursor.execute(sqlite_select_query27)
    vladelec = cursor.fetchall()

    sqlite_select_query28 = """SELECT * from users where user_status = \"Bog\""""
    cursor.execute(sqlite_select_query28)
    bog = cursor.fetchall()

    sqlite_select_query29 = """SELECT * from users where user_status = \"Vlaselin\""""
    cursor.execute(sqlite_select_query29)
    vlaselin = cursor.fetchall()

    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Admin\""""
    cursor.execute(sqlite_select_query2)
    records2 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Helper_Admin\""""
    cursor.execute(sqlite_select_query2)
    records3 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Owner\""""
    cursor.execute(sqlite_select_query2)
    records4 = cursor.fetchall()

    if user_status == 'Owner':
       await callback.message.answer(f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот общая статистика бота 🔎

🔓 | Основная
         👤 | Игроков: {len(records)}

🔰 | Привилегии
         ❤️ | ВИП: {len(vip)}
         🧡 | ПРЕМИУМ: {len(premium)}
         💛 | ПЛАТИНА: {len(platina)}
         💚 | ХЕЛПЕР: {len(helper)}
         💙 | СПОНСОР: {len(sponsor)}
         💜 | ОСНОВАТЕЛЬ: {len(osnovatel)}
         🖤 | ВЛАДЕЛЕЦ: {len(vladelec)}
         🤍 | БОГ: {len(bog)}
         🤎 | ВЛАСТЕЛИН: {len(vlaselin)}

🛑 | Администрация
         ⛔️ | ADMIN: {len(records2)}
         ⚠️ | HELPER-ADMIN: {len(records3)}
         ✅ | OWNER: {len(records4)}        
       """, parse_mode='html')
    else:
       await callback.message.answer(f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, статистика бота доступна только от прав администратора \"HELPER-ADMINS\" ", parse_mode='html')


@dp.callback_query_handler(text='statistic')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    
    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Admin\""""
    cursor.execute(sqlite_select_query2)
    records2 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Helper_Admin\""""
    cursor.execute(sqlite_select_query2)
    records3 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Owner\""""
    cursor.execute(sqlite_select_query2)
    records4 = cursor.fetchall()

    stats222 = InlineKeyboardMarkup(row_width=1)
    ob_statistik2 = InlineKeyboardButton(text='Общая статистика 🔎', callback_data='ob_statistik2')
    
    stats222.add(ob_statistik2)

    if user_status == "Admin":
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот статистика бота  📊\n🤵 | Игроков: {len(records)}\n👨‍⚖️ | OWNER: {len(records4)}\n👮‍♀️ | HELPER-ADMINS: {len(records3)}\n🤠 | ADMIN: {len(records2)}",reply_markup=stats222, parse_mode='html')
       return
    if user_status == "Helper_Admin":
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот статистика бота  📊\n🤵 | Игроков: {len(records)}\n👨‍⚖️ | OWNER: {len(records4)}\n👮‍♀️ | HELPER-ADMINS: {len(records3)}\n🤠 | ADMIN: {len(records2)}",reply_markup=stats222 , parse_mode='html')
       return

    if user_status == "Owner":
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот статистика бота  📊\n🤵 | Игроков: {len(records)}\n👨‍⚖️ | OWNER: {len(records4)}\n👮‍♀️ | HELPER-ADMINS: {len(records3)}\n🤠 | ADMIN: {len(records2)}",reply_markup=stats222 , parse_mode='html')
       return
    else:
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>,Вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику <a href='t.me/haeshka_qwe_per/'>Хаешка</a>  ⚠️ ", parse_mode='html')
@dp.callback_query_handler(text='Admins_menu_up')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = str(user_status[0])

    admins_menu = InlineKeyboardMarkup(row_width=2)
    statistic = InlineKeyboardButton(text='Статистика 👥', callback_data='statistic')
    admins_comands = InlineKeyboardButton(text='Админ команды 📝', callback_data='admins_comands')
    admins_menu.add(statistic, admins_comands)
    if user_status == 'Owner':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно вошли в админ меню ✅\n\n⛔️ | Права администратора: OWNER\n\n🔐 | Категории:\n     👥 | Статистика бота\n     📝 | Админ команды\n\n↘️ Выбери одну из категорий", reply_markup=admins_menu , parse_mode='html')
       return

    if user_status == 'Helper_Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно вошли в админ меню ✅\n\n⛔️ | Права администратора: HELPER ADMINS\n\n🔐 | Категории:\n     👥 | Статистика бота\n     📝 | Админ команды\n\n↘️ Выбери одну из категорий", reply_markup=admins_menu , parse_mode='html')
       return
    if user_status == 'Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно вошли в админ меню ✅\n\n⛔️ | Права администратора: ADMINS\n\n🔐 | Категории:\n     👥 | Статистика бота\n     📝 | Админ команды\n\n↘️ Выбери одну из категорий", reply_markup=admins_menu , parse_mode='html')
       return
    else:
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>,Вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику <a href='t.me/haeshka_qwe_per/'>Хаешка</a>  ⚠️ ", parse_mode='html')
@dp.callback_query_handler(text='Osn2')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, вот список основных команд📝

🖼 | Аватарка
      Удалить аватарку 🔒
🕴 | Профиль
🔎 | Ник 
      Сменить ник [сообщения] ⚙️
      Сменить префикс [сообщения] ⚙️
      Сменить игроку префикс [сообщения] ⚙️
👝 | Б\Баланс
🏦 | Банк
      Банк снять [сумма] 🏛
      Банк положить [сумма] 🏛
      Депозит положить [сумма] 🏛
      Депозит снять [сумма] 🏛
      Процент снять [сумма] 🏛
🟣 | Эфириум 
      Эфириум курс 🟪
      Эфириум купить [количество] 🟪
      Эфириум продать [количество] 🟪
💎 | Рейтинг
      Рейтинг купить [количество] 💎
       Рейтинг продать [количество] 💎
🤝 | Дать [сумма]
🤝 | Передать [сумма] [ID]
💰 | Ограбить банк 
🎁 | Ежедневный бонус
👑 | Топ
🏛 | Топ богачей\ Топ Б
🎁 | Кит-бонусы
      Получить кит-бонус 🎁
👮‍♂️ | Репорт
💭 | Рп-команды

ℹ️ Что бы использовать команду , напишите команду сообщением
    ''', parse_mode='html')

@dp.callback_query_handler(text='register_help')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])


    help2 = InlineKeyboardMarkup(row_width=2)
    Osn2 = InlineKeyboardButton(text='Основные 📝', callback_data='Osn2')
    game2 = InlineKeyboardButton(text='Игры 🎮', callback_data='game2')
    rabot2 = InlineKeyboardButton(text='Работы 🔨', callback_data='rabot2')
    Im2 = InlineKeyboardButton(text='Имущество 🏘 ', callback_data='Im2')
    Priv2 = InlineKeyboardButton(text='Привилегии 📖', callback_data='Priv2')
    Adm2 = InlineKeyboardButton(text='Admins menu ⛔️', callback_data='Admins_menu_up')
    help2.add(Osn2, game2, rabot2, Im2, Priv2, Adm2)
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, виберите категории🔍

📝 | Основные
🎮 | Игры 
🔨 | Работы
🏘 | Имущество
📖 | Привилегии
⛔️ | Admins menu 

Разработчик: <a href='t.me/haeshka_qwe_per/'>Хаешка</a>  💻
Наша беседа: @qwechat 💬
    ''', reply_markup=help2, parse_mode='html')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

