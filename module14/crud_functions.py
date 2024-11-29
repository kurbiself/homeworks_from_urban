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


# for num in range(1, 5):
#     cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
#                    (num, f'Продукт {num}', f'Описание {num}', num * 100))


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products


connection.commit()

