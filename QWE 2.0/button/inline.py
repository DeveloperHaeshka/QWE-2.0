from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

gamevbmenu = InlineKeyboardMarkup(row_width=1)
gamevb = InlineKeyboardButton(text='ИГРАТЬ 🎮', callback_data='gamevb')
gamevbmenu.add(gamevb)

reg = InlineKeyboardMarkup(row_width=1)
register_help = InlineKeyboardButton(text='🆘 Помощь', callback_data='register_help')
reg.add(register_help)

admin_menu = InlineKeyboardMarkup(row_width=1)
Admins_menu_up = InlineKeyboardButton(text='Войти ✅', callback_data='Admins_menu_up')
admin_menu.add(Admins_menu_up)


help2 = InlineKeyboardMarkup(row_width=2)
Osn2 = InlineKeyboardButton(text='Основные 📝', callback_data='Osn2')
game2 = InlineKeyboardButton(text='Игры 🎮', callback_data='game2')
rabot2 = InlineKeyboardButton(text='Работы 🔨', callback_data='rabot2')
Im2 = InlineKeyboardButton(text='Имущество 🏘 ', callback_data='Im2')
Priv2 = InlineKeyboardButton(text='Привилегии 📖', callback_data='Priv2')
Adm2 = InlineKeyboardButton(text='Admins menu ⛔️', callback_data='Admins_menu_up')
help2.add(Osn2, game2, rabot2, Im2, Priv2, Adm2)


