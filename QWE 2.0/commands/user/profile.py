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
          priv = '????????????????????????'
       if user_status == 'Vip':
          priv = '????????????'
       if user_status == 'Premium':
          priv = ' ??????????????????'
       if user_status == 'Platina':
          priv = ' ??????????????????'
       if user_status == 'Helper':
          priv = ' ????????????????'
       if user_status == 'Sponsor':
          priv = ' ??????????????????'
       if user_status == 'Osnovatel':
          priv = ' ????????????????????????'
       if user_status == 'Vladelec':
          priv = ' ????????????????????'
       if user_status == 'Bog':
          priv = ' ??????????'
       if user_status == 'Vlaselin':
          priv = ' ??????????????????????'
       if user_status == 'Owner':
          priv = '?????????????????????????'
       if user_status == 'Admin':
          priv = '????????????????????????????????'
       if user_status == 'Helper_Admin':
          priv = 'HELPER ????????????????????????????????'

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
          balance3 = f'{balance2} ??????'
       if int(balance) in range(1000000, 999999999):
          balance1 = balance / 1000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ??????'
       if int(balance) in range(1000000000, 999999999999):
          balance1 = balance / 1000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????'
       if int(balance) in range(1000000000000, 999999999999999):
          balance1 = balance / 1000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????'
       if int(balance) in range(1000000000000000, 999999999999999999):
          balance1 = balance / 1000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????'
       if int(balance) in range(1000000000000000000, 999999999999999999999):
          balance1 = balance / 1000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????'
       if int(balance) in range(1000000000000000000000, 999999999999999999999999):
          balance1 = balance / 1000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????'
       if int(balance) in range(1000000000000000000000000, 999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ??????????'
       if int(balance) in range(1000000000000000000000000000,999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????????'
       if int(balance) in range(1000000000000000000000000000000, 999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????'
       if int(balance) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????'
       if int(balance) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????'
       if int(balance) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ??????????'
       if int(balance) in range(1000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????'
       if int(balance) in range(1000000000000000000000000000000000000000000000,999999999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ??????????'
       if int(balance) in range(1000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ????????'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ??????????'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ??????????'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ??????????'
       if int(balance) >= 1000000000000000000000000000000000000000000000000000000000000000:
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} ??????????'
       
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
          ethereum3 = f'{ethereum2} ??????'
       if int(ethereum) in range(1000000, 999999999):
          ethereum1 = ethereum / 1000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ??????'
       if int(ethereum) in range(1000000000, 999999999999):
          ethereum1 = ethereum / 1000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????'
       if int(ethereum) in range(1000000000000, 999999999999999):
          ethereum1 = ethereum / 1000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????'
       if int(ethereum) in range(1000000000000000, 999999999999999999):
          ethereum1 = ethereum / 1000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????'
       if int(ethereum) in range(1000000000000000000, 999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????'
       if int(ethereum) in range(1000000000000000000000, 999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????'  
       if int(ethereum) in range(1000000000000000000000000, 999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ??????????'
       if int(ethereum) >= 1000000000000000000000000000:
          ethereum1 = ethereum / 1000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????????'
       if int(ethereum) in range(1000000000000000000000000000000, 999999999999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????'
       if int(ethereum) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????'
       if int(ethereum) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????'
       if int(ethereum) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ??????????'
       if int(ethereum) in range(1000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999):
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????'
       if int(ethereum) >= 1000000000000000000000000000000000000000000000:
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ??????????'
       if int(ethereum) in range(1000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999) :
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????'
       if int(ethereum) in range(1000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999) :
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ????????'
       if int(ethereum) in range(1000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999) :
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ??????????'
       if int(ethereum) in range(1000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999) :
          ethereum1 = ethereum / 1000000000000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ??????????'
       if int(ethereum) in range(1000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999):
          ethereum1 = balance / 1000000000000000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ??????????'
       if int(ethereum) >= 1000000000000000000000000000000000000000000000000000000000000000:
          ethereum1 = balance / 1000000000000000000000000000000000000000000000000000000000000000
          ethereum2 = round(ethereum1)
          ethereum3 = f'{ethereum2} ??????????'
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
          bank3 = f'{bank2} ??????'
       if int(bank) in range(1000000, 999999999):
          bank1 = bank / 1000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ??????'
       if int(bank) in range(1000000000, 999999999999):
          bank1 = bank / 1000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????'
       if int(bank) in range(1000000000000, 999999999999999):
          bank1 = bank / 1000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????'
       if int(bank) in range(1000000000000000, 999999999999999999):
          bank1 = bank / 1000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????'
       if int(bank) in range(1000000000000000000, 999999999999999999999):
          bank1 = bank / 1000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????'
       if int(bank) in range(1000000000000000000000, 999999999999999999999999):
          bank1 = bank / 1000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????'
       if int(bank) in range(1000000000000000000000000, 999999999999999999999999):
          bank1 = bank / 1000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ??????????'
       if int(bank) >= 1000000000000000000000000000:
          bank1 = bank / 1000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????????'
       if int(bank) in range(1000000000000000000000000000000, 999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????'
       if int(bank) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????'
       if int(bank) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????'
       if int(bank) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ??????????'
       if int(bank) in range(1000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????'
       if int(bank) >= 1000000000000000000000000000000000000000000000:
          bank1 = bank / 1000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ??????????'
       if int(bank) in range(1000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999) :
          bank1 = bank / 1000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????'
       if int(bank) in range(1000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999) :
          bank1 = bank / 1000000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ????????'
       if int(bank) in range(1000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999) :
          bank1 = bank / 1000000000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ??????????'
       if int(bank) in range(1000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999) :
          bank1 = bank / 1000000000000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ??????????'
       if int(bank) in range(1000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ??????????'
       if int(bank) >= 1000000000000000000000000000000000000000000000000000000000000000:
          bank1 = bank / 1000000000000000000000000000000000000000000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} ??????????'
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
          rating3 = f'{rating2} ??????'
       if int(rating) in range(1000000, 999999999):
          rating1 = rating / 1000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ??????'
       if int(rating) in range(1000000000, 999999999999):
          rating1 = rating / 1000000000
          rating2 = round(rating1) 
          rating3 = f'{rating2} ????????'
       if int(rating) in range(1000000000000, 999999999999999):
          rating1 = rating / 1000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ????????'
       if int(rating) in range(1000000000000000, 999999999999999999):
          rating1 = rating / 1000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ????????'
       if int(rating) in range(1000000000000000000, 999999999999999999999):
          rating1 = rating / 1000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ????????'
       if int(rating) in range(1000000000000000000000, 999999999999999999999999):
          rating1 = rating / 1000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ????????'
       if int(rating) in range(1000000000000000000000000, 999999999999999999999999):
          rating1 = rating / 1000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ??????????'
       if int(rating) >= 1000000000000000000000000000:
          rating1 = rating / 1000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ????????????'
       if int(rating) in range(1000000000000000000000000000000, 999999999999999999999999999999999):
          rating1 = rating / 1000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ????????'
       if int(rating) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
          rating1 = rating / 1000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ????????'
       if int(rating) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
          rating1 = rating / 1000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ????????'
       if int(rating) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
          rating1 = rating / 1000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ??????????'
       if int(rating) in range(1000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999):
          rating1 = rating / 1000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ????????'
       if int(rating) >= 1000000000000000000000000000000000000000000000:
          rating1 = rating / 1000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ??????????'
       if int(rating) in range(1000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999) :
          rating1 = rating / 1000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ????????'
       if int(rating) in range(1000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999) :
          rating1 = rating / 1000000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ????????'
       if int(rating) in range(1000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999) :
          rating1 = rating / 1000000000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ??????????'
       if int(rating) in range(1000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999) :
          rating1 = rating / 1000000000000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ??????????'
       if int(rating) in range(1000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999):
          rating1 = balance / 1000000000000000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ??????????'
       if int(rating) >= 1000000000000000000000000000000000000000000000000000000000000000:
          rating1 = balance / 1000000000000000000000000000000000000000000000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} ??????????'

       times = cursor.execute("SELECT time_register FROM users WHERE user_id=?", (message.from_user.id,)).fetchall()
       times2 = times[0]


       await message.bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a> , ?????? ?????????????? : \n???? | ID: {user_id}\n?????? | ??????????????: {pref} \n???? | ????????????????????: {priv}\n???? | ????????????: {balance3}$\n???? | ?? ??????????: {bank3}$\n???? | ??????????????: {ethereum3}????\n???? | ??????????????: {rating3}\n???? | ??????????????????: {reput}\n???? | Donate-coins: {donate_coins}\n???? | ?????????? ?????????????? ??????: {game2}\n?????? ??????????????????: ?? ????????????????????\n\n???????????? ??????????????????????: {times2}",  parse_mode='html')
