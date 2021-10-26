import sqlite3

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


currentSesion = False
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

