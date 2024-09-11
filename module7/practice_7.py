import tkinter
from tkinter import filedialog
import tkinter.messagebox as mb
import os


def file_select():
    filename = filedialog.askopenfilename(initialfile='/', title='Select file',
                                          filetypes=(('text file', '.txt'), ('All files', '*')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)


def show_info():
    msg = "Эта программа является проводником"
    mb.showinfo("Информация", msg)


def about_info():
    msg = "Программа выполнена студентом универстите Urban"
    mb.showinfo("Информация", msg)


window = tkinter.Tk()
window.title('Проводник')
window.geometry('400x200')
window.configure(bg='black')
window.resizable(False, False)  # запрет на изменение размера
text = tkinter.Label(window, text='Файл:', width=57, height=3, background='black', fg='white')
button_select = tkinter.Button(window, width=57, height=6, text='Выберите файл', fg='white', background='blue',
                               command=file_select)
menu = tkinter.Menu(window, activebackground='white')
button_select.grid(column=1, row=2, pady=5)
text.grid(column=1, row=1)
window.config(menu=menu)
file_menu = tkinter.Menu(menu, tearoff=0)
file_menu.add_command(label="Информация", command=show_info)
file_menu.add_command(label="About", command=about_info)
menu.add_cascade(label="Файл", menu=file_menu)

window.mainloop()  # постоянное обновление окна

