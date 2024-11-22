import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
# cursor.execute("DELETE FROM Users WHERE id = ? ", (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
count_users = cursor.fetchone()[0]
print('Количество пользоваталей в БД:', count_users)
cursor.execute('SELECT SUM(balance) FROM Users')
sum_balance = cursor.fetchone()[0]
print('Сумма баланса всех пользоваталей в БД:', sum_balance)
print('Среднний баланс вручную:', sum_balance / count_users)
cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print('Среднний баланс:', avg_balance)

connection.commit()
connection.close()
