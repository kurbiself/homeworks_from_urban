import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
);
''')


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    );
    ''')
    connection.commit()


# for num in range(1, 5):
#     cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
#                    (num, f'Продукт {num}', f'Описание {num}', num * 100))


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products


def is_included(username: str):
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check_user.fetchall():
        return True
    else:
        return False


def add_user(username: str, email: str, age: int):
    if not is_included(username):
        cursor.execute(f'''
       INSERT INTO Users VALUES(NULL, '{username}', '{email}', '{age}', 1000)
       ''')
        connection.commit()


connection.commit()
