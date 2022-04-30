import tkinter as tk
from tkinter import ttk
from add_child import CreateChild
import sqlite3
from create_db import DB

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.view_records()

    def view_insert(self):
        self.conn = sqlite3.connect('accounting.db')  # Соединение с базой данных
        self.c = self.conn.cursor()  # Взаимодействие с базой
        self.c.execute('''SELECT * FROM accounting''')

    def view_records(self):  # Передача данных
        self.view_insert()
        [self.tree.delete(i) for i in self.tree.get_children()]  # Очистна данных
        # Генератор
        [self.tree.insert('', 'end', values=row) for row in self.c.fetchall()]  # Добавление новых значений после предедущих

    def delete_records(self):
        for selection_item in self.tree.selection(): # Цыкл проходит по всем строка
            self.c.execute('''DELETE FROM accounting WHERE add_id=?''', (self.tree.set(selection_item, '#1'),)) # Метот set возвращает значение
        self.conn.commit()
        self.view_records()

    def update_records(self):
        row_id = self.tree.set(self.tree.selection()[0], '#1')
        # Передаю параметр в окно add_child
        CreateChild(self, row_id)
        self.view_records()

    def search_records(self):
        DB.search_records(self, self.entry_name.get(), self.entry_inv_nomer.get(), self.entry_PIB.get())
        self.entry_name.delete(0, 'end')
        self.entry_inv_nomer.delete(0, 'end')
        self.entry_PIB.delete(0, 'end')
        [self.tree.delete(i) for i in self.tree.get_children()]# Очистка нашу таблицу
        [self.tree.insert('', 'end', values=row) for row in self.c.fetchall()] #Отображение нашего запроса

    def search_db(self):
        # Верхняя полоска кнопок для дочернего окна
        toolbar_main = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar_main.pack(side=tk.TOP, ipady=80, ipadx=545)

        label_name = tk.Label(toolbar_main, text='Матеріальна цінність:', font=8, bg='#d7d8e0')
        label_name.place(x=20, y=25)
        label_inv_nomer = tk.Label(toolbar_main, text='Інв. номер:', font=8, bg='#d7d8e0')
        label_inv_nomer.place(x=115, y=65)
        label_PIB = tk.Label(toolbar_main, text='ПІБ:', font=8, bg='#d7d8e0')
        label_PIB.place(x=180, y=105)

        self.entry_name = ttk.Entry(toolbar_main, width=50)
        self.entry_name.place(x=250, y=30)
        self.entry_inv_nomer = ttk.Entry(toolbar_main, width=20)
        self.entry_inv_nomer.place(x=250, y=70)
        self.entry_PIB = ttk.Entry(toolbar_main, width=50)
        self.entry_PIB.place(x=250, y=110)
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
        edit_menu.add_command(label="Змінити дані", command=self.update_records)  # "Выход" подменю "Файл"
        edit_menu.add_command(label="Видалити дані", command=self.delete_records)  # "Выход" подменю "Файл"

        # Создание меню Обновление
        update_menu = tk.Menu(my_menu, tearoff=0) # створення меню
        my_menu.add_cascade(label="Вид", menu=update_menu)  # "Файл" до главного окна
        update_menu.add_command(label="Оновлення", command=self.view_records)  # "Новый" подменю "Файл"
        update_menu.add_command(label="Пошук", command=self.search_records)  # "Найти"

    def open_dialog(self):
         CreateChild(self, row_id=0)
         self.view_records()

if __name__ == "__main__": # Параметры главного окна
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Головне вікно - Облік комп'ютерної техніки")
    root.geometry("1100x750+250+10") #Указываем размеры окна
    root.resizable(False, False) #Делаем невозможным менять размеры окна
    root.mainloop()
