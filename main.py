import tkinter as tk
from tkinter import ttk
from add_child import CreateChild
#import sqlite3
from create_db import DB

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.view_records()

    def view_records(self):  # Передача данных
        [self.tree.delete(i) for i in self.tree.get_children()]  # Очистна данных
        # Генератор
        [self.tree.insert('', 'end', values=row) for row in DB.view_insert(self, db_fetchall=0)]  # Добавление новых значений после предедущих

    def search_db(self):
        # Верхняя полоска кнопок для дочернего окна
        toolbar_main = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar_main.pack(side=tk.TOP, ipady=80, ipadx=545)

        label_name = tk.Label(toolbar_main, text='Матеріальна цінність:', font=8, bg='#d7d8e0')
        label_name.place(x=20, y=10)
        label_inv_nomer = tk.Label(toolbar_main, text='Інв. номер:', font=8, bg='#d7d8e0')
        label_inv_nomer.place(x=115, y=50)
        label_PIB = tk.Label(toolbar_main, text='ПІБ:', font=8, bg='#d7d8e0')
        label_PIB.place(x=180, y=90)

        self.entry_name = ttk.Entry(toolbar_main, width=50)
        self.entry_name.place(x=250, y=15)
        self.entry_inv_nomer = ttk.Entry(toolbar_main, width=20)
        self.entry_inv_nomer.place(x=250, y=55)
        self.entry_PIB = ttk.Entry(toolbar_main, width=50)
        self.entry_PIB.place(x=250, y=95)
        # End

    def view_tree(self):
        # Таблица и формирование шапки
        self.tree = ttk.Treeview(self, columns=('add_id', 'add_name', 'add_inv_nomer', 'add_pib',
                                                'add_division', 'add_data_in', 'add_data_out'), show='headings')
        self.tree.column('add_id', width=30, anchor=tk.CENTER)
        self.tree.column('add_name', width=240, anchor=tk.CENTER)
        self.tree.column('add_inv_nomer', width=100, anchor=tk.CENTER)
        self.tree.column('add_pib', width=250, anchor=tk.CENTER)
        self.tree.column('add_division', width=250, anchor=tk.CENTER)
        self.tree.column('add_data_in', width=100, anchor=tk.CENTER)
        self.tree.column('add_data_out', width=100, anchor=tk.CENTER)

        self.tree.heading('add_id', text='№')
        self.tree.heading('add_name', text='Матеріальна цінність')
        self.tree.heading('add_inv_nomer', text='Інв. номер')
        self.tree.heading('add_pib', text='ПІБ')
        self.tree.heading('add_division', text='Підрозділ')
        self.tree.heading('add_data_in', text='Дата введення')
        self.tree.heading('add_data_out', text='Дата зняття')

        self.tree.pack(side=tk.LEFT, ipady=180, ipadx=10)
        # End

    def init_main(self):
        self.search_db()
        self.view_tree()

        my_menu = tk.Menu(self)
        root.config(menu=my_menu)

        #Создание меню Файл
        file_menu = tk.Menu(my_menu, tearoff=0) # створення меню
        my_menu.add_cascade(label="Файл", menu=file_menu) #"Файл" до главного окна
        file_menu.add_command(label="Імпорт", command=self.quit) #"Новый" подменю "Файл"
        file_menu.add_command(label="Експорт", command=self.quit)  # "Новый" подменю "Файл"
        file_menu.add_separator() #Горизонтальная полоса
        file_menu.add_command(label="Вихід", command=self.quit)  # "Выход" подменю "Файл"

        # Создание меню Редактирование
        edit_menu = tk.Menu(my_menu, tearoff=0) # створення меню
        my_menu.add_cascade(label="Редагування", menu=edit_menu) #"Файл" до главного окна
        edit_menu.add_command(label="Додати дані", command=self.open_dialog) #"Новый" подменю "Файл"
        edit_menu.add_command(label="Змінити дані", command=self.quit)  # "Выход" подменю "Файл"
        edit_menu.add_command(label="Видалити дані", command=self.quit)  # "Выход" подменю "Файл"

        # Создание меню Обновление
        update_menu = tk.Menu(my_menu, tearoff=0) # створення меню
        my_menu.add_cascade(label="Вид", menu=update_menu)  # "Файл" до главного окна
        update_menu.add_command(label="Оновлення", command=self.view_records)  # "Новый" подменю "Файл"
        update_menu.add_command(label="Пошук", command=self.open_dialog)  # "Новый" подменю "Файл"

    def open_dialog(self):
         CreateChild(self)

if __name__ == "__main__": # Параметры главного окна
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Головне вікно - Облік комп'ютерної техніки")
    root.geometry("1100x750+250+10") #Указываем размеры окна
    root.resizable(False, False) #Делаем невозможным менять размеры окна
    root.mainloop()
