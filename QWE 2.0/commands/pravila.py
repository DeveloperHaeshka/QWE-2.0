from email.message import Message
from aiogram.types import message
from db import cursor, connect

async def pravila_hendler(message: Message):
    await message.bot.send_message(message.chat.id, f"""
🤬 | 1. Оскорбление [Мут - 15 минут ]
🤬 | 1.1 Оскорбление друзей личности [Мут - 10 минут]
🤬 | 1.2 Оскорбление родителем/родственников [Мут - 2 часа] + [ Варн ]
🤬 | 1.3 Оскорбление администрации [Мут - от 2 до 5 часов ] + [ Варн ]
🤬 | 1.4 Провокация на оскорбление [Мут - 5 минут]
🔞 | 2. Порнография в любом виде [Мут - 5 минут]
🔞 | 2.1 Спам контента порнографии [ Мут - 15 минут ]
🚷 | 3. Обман игроков [ Бан - 1 день ] + [ Варн ]
⛔️ | 4. Продажа игровой валюты [ Бан - 7 дней ] + [ Варн ] + [ Обнуление ]
⛔️ | 4.1 Продажа "Схем заработка" [Бан - 3 дня ] + [ Варн ]
⚠️ | 5. Капс (ПРИМЕР) [ Мут - 1 минута ]
⚠️ | 5.1 Флуд , спам [ Мут - 15 минут ]
⚠️ | 5.2 Не соглашёная реклама [ Мут - 1 час ] 
🆘 | 6. Любые действия связанные с вредом проекту [ Бан - 1 день ] + [ Варн ] [Если вред был нанесён тогда чс проекта ]
🆘 | 6.1 Читерство/Дюпинг в боте [ Обнуление ] + [ Варн ]      
       """, parse_mode='html')