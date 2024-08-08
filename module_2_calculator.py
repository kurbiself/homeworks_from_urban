import tkinter as tk


def get_value():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(first=0, last='end')
    answer_entry.insert(0, value)


def addition():
    num1, num2 = get_value()
    result = num1 + num2
    insert_values(result)


def subtraction():
    num1, num2 = get_value()
    result = num1 - num2
    insert_values(result)


def div():
    num1, num2 = get_value()
    result = num1 / num2
    insert_values(result)


def multiplication():
    num1, num2 = get_value()
    result = num1 * num2
    insert_values(result)


window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=4, height=2, command=addition)
button_add.place(x=90, y=200)
button_sub = tk.Button(window, text="-", width=4, height=2, command=subtraction)
button_sub.place(x=140, y=200)
button_mul = tk.Button(window, text="*", width=4, height=2, command=multiplication)
button_mul.place(x=190, y=200)
button_div = tk.Button(window, text="/", width=4, height=2, command=div)
button_div.place(x=240, y=200)
number1_entry = tk.Entry(window, width=32)
number1_entry.place(x=90, y=75)
number2_entry = tk.Entry(window, width=32)
number2_entry.place(x=90, y=150)
answer_entry = tk.Entry(window, width=32)
answer_entry.place(x=90, y=300)
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=90, y=50)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=90, y=125)
answer = tk.Label(window, text="Ответ:")
answer.place(x=90, y=275)
window.mainloop()
