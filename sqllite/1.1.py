import sqlite3
"""
sql.execute() = работа с данными 
"""



#Создани дб
db = sqlite3.connect('server.db')
#Нужен для работы с бд и дальше только с ним))
sql = db.cursor()

#Создание таблицы с данными 
sql.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    cash BIGINT
)""")

#Выгрузка данных на сервер
db.commit()

#Входные данные
user_login = input('Login: ')
user_password = input('Password: ')

#Проверка нахождениея логина в users 
sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
#Сама проверка

if sql.fetchone() is None:
    #Запись данных в бд
    sql.execute(f"INSERT INTO users VALUES (?,?,?)",(user_login,user_password,0))
    db.commit()
    
    print('Зарегистрированно!')
else:
    print('Такая запись уже есть!')

for value in sql.execute("SELECT * FROM users"):
    print(value)
