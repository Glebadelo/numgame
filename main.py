import sqlite3
import random as rnd

def sing_up(): #Функция кнопка Зарегистрироваться
    con = sqlite3.connect('users_db.db')
    cur = con.cursor()

    username = input('Имя пользователя: ') #Значение из поля
    password = input('Пароль: ') #Значение из защищённого поля

    try:
        cur.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    except sqlite3.IntegrityError:
        print("Данное имя пользователя уже используется!")

    for row in cur.execute('SELECT * FROM users ORDER BY username'):
        print(row)

    con.commit()
    con.close()

#sing_up()
currentSession = False
currentSession_name = ""

def login(): #Функция кнопки Войти
    username = input('Имя пользователя: ') #Значение из поля
    password = input('Пароль: ') #Значение из защищённого поля

    con = sqlite3.connect('users_db.db')
    cur = con.cursor()

    try:
        cur.execute("SELECT password FROM users WHERE username = '%s'" % username)
        result = cur.fetchone()[0]
        if password == result:
            currentSesion = True
            currentSession_name = username
            print("Вы успешно зашли")
            # Переход в основное меню игры
        else:
            print("Вы ввели неверный пароль")

    except TypeError:
        print("Вы ввели несущствующее имя пользователя")
        con.close()
login()

def startGame():
    lowBorder = int(input("Нижняя граница:")) #нижняя граница
    topBorder = int(input("Верхняя граница")) #вернхяя граница
    n_attemps = 5
    Num = rnd.randint(lowBorder, topBorder)

    print(Num)

    attemp = 1
    while (attemp <= n_attemps):
        N = int(input("Угадайте число: "))
        if N < Num:
            print("Заданное число меньше")
            attemp += 1
            ##тепло или холодно число окрашивается в соот цвет и заносится в историю
        elif N > Num:
            print("Заданное число больше")
            attemp += 1
            ##тепло или холодно число окрашивается в соот цвет и заносится в историю
        else:
            print("Вы угадали. Игра закончена")
            break
            #функция расчёта очков

    else:
        print("Попытки закончились. Игра закончена")
        #функция расчёта очков и обновление записи игрока

startGame()


