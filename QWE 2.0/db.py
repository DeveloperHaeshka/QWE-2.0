import sqlite3


connect = sqlite3.connect("users.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT,
    user_name STRING,
    user_tg_name STRING,
    user_status STRING,
    balance INT,
    bank BIGINT,
    ethereum INT,
    rating INT,
    status_block STRING,
    time_register INT,
    pref STRING,
    donate_coins INT,
    game INT,
    bank2 INT,
    depozit INT,
    stats_status STRING
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS mine(
    user_id INT,
    user_name STRING,
    pick STRING,
    iron INT,
    metall INT,
    silver INT,
    bronza INT,
    gold INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS user_case(
    user_id INT,
    case_money INT,
    case_donate INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS farm(
    user_id INT,
    user_name STRING,
    rake STRING,
    linen INT,
    cotton INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS house(
    user_id INT,
    user_name STRING,
    house INT,
    basement INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
    user_id INT,
    user_name STRING,
    cars INT,
    hp INT,
    benz INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS bot_time(
    user_id INT,
    stavka_games INT,
    stavka_bank INT,
    stavka_bonus INT,
    stavka_depozit INT,
    time_pick INT,
    time_rake INT,
    time_craft INT,
    time_kit INT
)
""")


cursor.execute("""CREATE TABLE IF NOT EXISTS time_bank(
    user_id INT,
    stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS ob_time(
    user_id INT,
    stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS time_prefix(
    user_id INT,
    stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS time_sms(
    user_id INT,
    stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS warn(
    user_id INT,
    warn INT 
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS console(
    user_id INT,
    status STRING 
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS channel_pov(
    user_id INT,
    members INT   
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS avatarka(
    user_id INT,
    avatarka STRING   
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS reput(
    user_id INT,
    reput INT   
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS h_module(
    user_id INT,
    h_status INT   
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo1(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo2(
    user_id INT,
    members INT,
    ob_members INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS promo3(
    user_id INT,
    members INT,
    ob_members INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS promo4(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo5(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo6(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo7(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo8(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo9(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo10(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo11(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo12(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo13(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo14(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo15(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo16(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo17(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo18(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo19(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo20(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo21(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo22(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo23(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo24(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo25(
    user_id INT,
    members INT,
    ob_members INT
)
""")
