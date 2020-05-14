import sqlite3
from random import randint

global db
global sql

db = sqlite3.connect('server.db')
sql = db.cursor()


sql.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
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
        sql.execute(f"INSERT INTO users (login,password,cash) VALUES (?,?,?)",(user_login,user_password,0))
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
        print('Пароль не верен!')
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
            number = randint(1,2)
            if number == 1:
                sql.execute(f"UPDATE users SET cash = cash + 1000 WHERE login = '{user_login}'")
                db.commit()

                print('Ура победа!')
                enter(user_login)

            else:
                sql.execute(f"UPDATE users SET cash = cash - 1000 WHERE login = '{user_login}'")
                db.commit()

                print('Вы проиграли !')
                enter(user_login)
            chek_admin(user_login)
        
def enter(user_name):
    for i in sql.execute(f"SELECT login, cash FROM users WHERE login = '{user_name}' "):
        print(i)

def chek_admin(user_name):
    if user_name == 'meresnes':
        k = input('Ввывести данные всех пользователей?(Y/N)')
        if k == 'Y':
            user_password = input('Введите пароль: ')
            key = chek_pass(user_name, user_password)
            if key == True:
                for value in sql.execute("SELECT * FROM users"):
                    print(value)
            else:
                print('Пароль неверен !')
        else:
            pass
    else:
        pass

def main():
    casino()

    sql.close()
    db.close()

main()

    
