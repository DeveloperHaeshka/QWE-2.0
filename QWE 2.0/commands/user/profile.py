from email.message import Message
from aiogram.types import message

from db import cursor, connect



async def profile_handler(message: Message):
       msg = message
       chat_id = message.chat.id
       
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       reput = cursor.execute("SELECT reput from reput where user_id = ?",(message.from_user.id,)).fetchone()
       reput = int(reput[0])

       avatarka = cursor.execute("SELECT avatarka from avatarka where user_id = ?",(message.from_user.id,)).fetchone()
       avatarka = avatarka[0]

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       ethereum = cursor.execute("SELECT ethereum from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       pref = cursor.execute("SELECT pref from users where user_id = ?",(message.from_user.id,)).fetchone()
       pref = str(pref[0])
       donate_coins = cursor.execute("SELECT donate_coins from users where user_id = ?",(message.from_user.id,)).fetchone()
       donate_coins = int(donate_coins[0])
       donate_coins2 = '{:,}'.format(donate_coins)
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = str(user_status[0])
       game = cursor.execute("SELECT game from users where user_id = ?",(message.from_user.id,)).fetchone()
       game = int(game[0])
       game2 = '{:,}'.format(game)

       balance = int(balance[0])
       bank = int(bank[0])
       rating = int(rating[0])
       ethereum = int(ethereum[0])

       
       c = 999999999999999999999999
       if user_status == 'Player':
          priv = 'Пользователь'
       if user_status == 'Vip':
          priv = 'ВИП❤️'
       if user_status == 'Premium':
          priv = ' ПРЕМИУМ🧡'
       if user_status == 'Platina':
          priv = ' ПЛАТИНА💛'
       if user_status == 'Helper':
          priv = ' ХЕЛПЕР💚'
       if user_status == 'Sponsor':
          priv = ' СПОНСОР💙'
       if user_status == 'Osnovatel':
          priv = ' ОСНОВАТЕЛЬ💜'
       if user_status == 'Vladelec':
          priv = ' ВЛАДЕЛЕЦ🖤'
       if user_status == 'Bog':
          priv = ' БОГ🤍'
       if user_status == 'Vlaselin':
          priv = ' ВЛАСТЕЛИН🤎'
       if user_status == 'Owner':
          priv = 'РАЗРАБОТЧИК✅'
       if user_status == 'Admin':
          priv = 'АДМИНИСТРАТОР⛔️'
       if user_status == 'Helper_Admin':
          priv = 'HELPER АДМИНИСТРАТОР⛔️'

       if balance >= 999999999999999999999999999999999999999999999999999999999999999999:
          balance = 999999999999999999999999999999999999999999999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit() 
       else:
        pass
       if int(balance) in range(0, 1000):
          balance3 = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
          balance3 = int(balance3[0])
       if int(balance) in range(1000, 999999):
          balance1 = balance / 1000
          balance2 = round(balance1)
          balance3 = f'{balance2} тыс'
       if int(balance) in range(1000000, 999999999):
          balance1 = balance / 1000000
          balance2 = round(balance1)
          balance3 = f'{balance2} млн'
       if int(balance) in range(1000000000, 999999999999):
          balance1 = balance / 1000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} млрд'
       if int(balance) in range(1000000000000, 999999999999999):
          balance1 = balance / 1000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} трлн'
       if int(balance) in range(1000000000000000, 999999999999999999):
          balance1 = balance / 1000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} квдр'
       if int(balance) in range(1000000000000000000, 999999999999999999999):
          balance1 = balance / 1000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} квнт'
       if int(balance) in range(1000000000000000000000, 999999999999999999999999):
          balance1 = balance / 1000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} скст'
       if int(balance) in range(1000000000000000000000000, 999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} трикс'
       if int(balance) in range(1000000000000000000000000000,999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} твинкс'
       if int(balance) in range(1000000000000000000000000000000, 999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} септ'
       if int(balance) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} октл'
       if int(balance) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} нонл'
       if int(balance) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} декал'
       if int(balance) in range(1000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} эндк'
       if int(balance) in range(1000000000000000000000000000000000000000000000,999999999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} доктл'
       if int(balance) in range(1000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} гугл'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} кинд'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} трипт'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} срист'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} манит'
       if int(balance) >= 1000000000000000000000000000000000000000000000000000000000000000:
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} гвинт'
       
       if ethereum >= 999999999999999999999999999999999999999999999999999999999999999999:
          ethereum = 999999999999999999999999999999999999999999999999999999999999999999
          cursor.execute(f'UPDATE users SET ethereum = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit() 
       else:
        pass
       if int(ethereum) in range(0, 1000):
          ethereum3 = cursor.execute("SELECT ethereum from users where user_id = ?",(message.from_user.id,)).fetchone()
          ethereum3 = int(ethereum3[0])
       if int(ethereum) in range(1000, 999999):
          ethereum1 = ethereum / 1000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} тыс'
       if int(ethereum) in range(1000000, 999999999):
          ethereum1 = ethereum / 1000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} млн'
       if int(ethereum) in range(1000000000, 999999999999):
          ethereum1 = ethereum / 1000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} млрд'
       if int(ethereum) in range(1000000000000, 999999999999999):
          ethereum1 = ethereum / 1000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} трлн'
       if int(ethereum) in range(1000000000000000, 999999999999999999):
          ethereum1 = ethereum / 1000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} квдр'
       if int(ethereum) in range(1000000000000000000, 999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} квнт'
       if int(ethereum) in range(1000000000000000000000, 999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} скст'  
       if int(ethereum) in range(1000000000000000000000000, 999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} трикс'
       if int(ethereum) >= 1000000000000000000000000000:
          ethereum1 = ethereum / 1000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} твинкс'
       if int(ethereum) in range(1000000000000000000000000000000, 999999999999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} септ'
       if int(ethereum) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} октл'
       if int(ethereum) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} нонл'
       if int(ethereum) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} декал'
       if int(ethereum) in range(1000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} эндк'
       if int(ethereum) >= 1000000000000000000000000000000000000000000000:
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} доктл'
       if int(ethereum) in range(1000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999) :
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} гугл'
       if int(ethereum) in range(1000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999) :
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} кинд'
       if int(ethereum) in range(1000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999) :
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} трипт'
       if int(ethereum) in range(1000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999) :
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} срист'
       if int(ethereum) in range(1000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999):
          ethereum1 = balance / 1000000000000000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} манит'
       if int(ethereum) >= 1000000000000000000000000000000000000000000000000000000000000000:
          ethereum1 = balance / 1000000000000000000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} гвинт'
       if bank >= 999999999999999999999999999999999999999999999999999999999999999999:
          bank = 999999999999999999999999999999999999999999999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()   
       else:
        pass
       if int(bank) in range(0, 1000):
          bank3 = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
          bank3 = int(bank3[0])
       if int(bank) in range(1000, 999999):
          bank1 = bank / 1000
          bank2 = round(bank1)
          bank3 = f'{bank2} тыс'
       if int(bank) in range(1000000, 999999999):
          bank1 = bank / 1000000
          bank2 = round(bank1)
          bank3 = f'{bank2} млн'
       if int(bank) in range(1000000000, 999999999999):
          bank1 = bank / 1000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} млрд'
       if int(bank) in range(1000000000000, 999999999999999):
          bank1 = bank / 1000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} трлн'
       if int(bank) in range(1000000000000000, 999999999999999999):
          bank1 = bank / 1000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} квдр'
       if int(bank) in range(1000000000000000000, 999999999999999999999):
          bank1 = bank / 1000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} квнт'
       if int(bank) in range(1000000000000000000000, 999999999999999999999999):
          bank1 = bank / 1000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} скст'
       if int(bank) in range(1000000000000000000000000, 999999999999999999999999):
          bank1 = bank / 1000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} трикс'
       if int(bank) >= 1000000000000000000000000000:
          bank1 = bank / 1000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} твинкс'
       if int(bank) in range(1000000000000000000000000000000, 999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} септ'
       if int(bank) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} октл'
       if int(bank) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} нонл'
       if int(bank) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} декал'
       if int(bank) in range(1000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} эндк'
       if int(bank) >= 1000000000000000000000000000000000000000000000:
          bank1 = bank / 1000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} доктл'
       if int(bank) in range(1000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999) :
          bank1 = bank / 1000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} гугл'
       if int(bank) in range(1000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999) :
          bank1 = bank / 1000000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} кинд'
       if int(bank) in range(1000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999) :
          bank1 = bank / 1000000000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} трипт'
       if int(bank) in range(1000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999) :
          bank1 = bank / 1000000000000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} срист'
       if int(bank) in range(1000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} манит'
       if int(bank) >= 1000000000000000000000000000000000000000000000000000000000000000:
          bank1 = bank / 1000000000000000000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} гвинт'
       if rating >= 999999999999999999999999999999999999999999999999999999999999999999:
          rating = 999999999999999999999999999999999999999999999999999999999999999999
          cursor.execute(f'UPDATE users SET rating = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
       else:
        pass
       if int(rating) in range(0, 1000):
          rating3 = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
          rating3 = int(rating3[0])
       if int(rating) in range(1000, 999999):
          rating1 = rating / 1000
          rating2 = round(rating1)
          rating3 = f'{rating2} тыс'
       if int(rating) in range(1000000, 999999999):
          rating1 = rating / 1000000
          rating2 = round(rating1)
          rating3 = f'{rating2} млн'
       if int(rating) in range(1000000000, 999999999999):
          rating1 = rating / 1000000000
          rating2 = round(rating1) 
          rating3 = f'{rating2} млрд'
       if int(rating) in range(1000000000000, 999999999999999):
          rating1 = rating / 1000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} трлн'
       if int(rating) in range(1000000000000000, 999999999999999999):
          rating1 = rating / 1000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} квдр'
       if int(rating) in range(1000000000000000000, 999999999999999999999):
          rating1 = rating / 1000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} квнт'
       if int(rating) in range(1000000000000000000000, 999999999999999999999999):
          rating1 = rating / 1000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} скст'
       if int(rating) in range(1000000000000000000000000, 999999999999999999999999):
          rating1 = rating / 1000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} трикс'
       if int(rating) >= 1000000000000000000000000000:
          rating1 = rating / 1000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} твинкс'
       if int(rating) in range(1000000000000000000000000000000, 999999999999999999999999999999999):
          rating1 = rating / 1000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} септ'
       if int(rating) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
          rating1 = rating / 1000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} октл'
       if int(rating) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
          rating1 = rating / 1000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} нонл'
       if int(rating) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
          rating1 = rating / 1000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} декал'
       if int(rating) in range(1000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999):
          rating1 = rating / 1000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} эндк'
       if int(rating) >= 1000000000000000000000000000000000000000000000:
          rating1 = rating / 1000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} доктл'
       if int(rating) in range(1000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999) :
          rating1 = rating / 1000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} гугл'
       if int(rating) in range(1000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999) :
          rating1 = rating / 1000000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} кинд'
       if int(rating) in range(1000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999) :
          rating1 = rating / 1000000000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} трипт'
       if int(rating) in range(1000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999) :
          rating1 = rating / 1000000000000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} срист'
       if int(rating) in range(1000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999):
          rating1 = balance / 1000000000000000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} манит'
       if int(rating) >= 1000000000000000000000000000000000000000000000000000000000000000:
          rating1 = balance / 1000000000000000000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} гвинт'

       times = cursor.execute("SELECT time_register FROM users WHERE user_id=?", (message.from_user.id,)).fetchall()
       times2 = times[0]


       await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , ваш профиль : \n🔎 | ID: {user_id}\n✏️ | Префикс: {pref} \n📝 | Привилегия: {priv}\n💰 | Деньги: {balance3}$\n🏦 | В банке: {bank3}$\n🟣 | Эфириум: {ethereum3}🟪\n💎 | Рейтинг: {rating3}\n📊 | Репутация: {reput}\n🪙 | Donate-coins: {donate_coins}\n🎯 | Всего сыграно игр: {game2}\n⚙️ Имущество: В разработке\n\n📆Дата регистрации: {times2}",  parse_mode='html')
