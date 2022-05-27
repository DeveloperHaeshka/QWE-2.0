from aiogram.types import message
from button.inline import reg

async def start_handler(message):

    name = message.from_user.get_mention(as_html=True)
    await message.bot.send_message(message.chat.id, f'''
👋 Привет, {name} 
Я бот для игры в различные игры.
Тебе выдан подарок в размере 10.000$.
Так же ты можешь добавить меня в беседу для игры с друзьями.
🆘 Чтобы узнать все команды введи "Помощь"
    ''', reply_markup=reg, parse_mode='html')