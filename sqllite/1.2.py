import sqlite3
from random import randint

global db
global sql

db = sqlite3.connect('server.db')
sql = db.cursor()


sql.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    cash INT
)""")

db.commit()

def reg():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?)",(user_login,user_password,0))
        db.commit()
        
        print('Зарегистрированно!')
    else:
        print('Такая запись уже есть!')

    '''for value in sql.execute("SELECT * FROM users"):
        print(value)'''
def chek_pass(user_login,user_password):
    sql.execute(f"SELECT password FROM users WHERE login = '{user_login}'")
    if user_password in sql.fetchone():
        return True
    else:
        print('ПАРОЛЬ НЕ ВЕРЕН !!!!!!!!!!')
        return False
def casino():
    
    user_login = input('Log in:')
    
    sql.execute(f"SElECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print('Такого логина нет!')
        print('Зарегестрируйтесь!')
        reg()
    else:
        user_password = input('Введите пароль: ')
        key = chek_pass(user_login,user_password)
        if key == True:
            number = randint(1,5)
            if number == 1:
                sql.execute(f"UPDATE users SET cash = '{1000}' WHERE login = '{user_login}'")
                db.commit()
                
                print('Ура победа!')
                
            else:
                print('Вы проиграли !')
        
def enter(user_name):
    for i in sql.execute(f"SELECT login, cash FROM users WHERE login = '{user_name}' "):
        print(i)

def main():
    casino()
    
    for value in sql.execute("SELECT * FROM users"):
        print(value)
    sql.close()
    db.close()

main()

    
