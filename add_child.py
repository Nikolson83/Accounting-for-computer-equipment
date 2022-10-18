import tkinter as tk
import sqlite3
from tkinter import ttk
from create_db import DB


# from  main import Main
class CreateChild(tk.Toplevel):
    def __init__(self, root, row_id):
        super().__init__(root)
        self.init_child(row_id)
        self.grab_focus()
        # self.open_db() #База данных
        # self.db = DB()

    # def open_db(self):
    #    DB() #База данных

    def init_child(self, row_id):
        self.title("Додати дані - Облік комп'ютерної техніки ")
        self.geometry("924x600+340+60")  # Указываем размеры окна
        self.resizable(False, False)  # Делаем невозможным менять размеры окна

        # Верхняя полоска кнопок для дочернего окна
        toolbar_child = tk.Frame(self, bg='#d7d8e0', bd=2)
        toolbar_child.pack(side=tk.TOP, fill=tk.X)

        self.cancel_img = tk.PhotoImage(file='img/cancel.png')
        btn_cancel_dialog = tk.Button(toolbar_child, text='Відмінити', command=self.destroy, bg='#d7d8e0', bd=0,
                                      compound=tk.TOP, image=self.cancel_img)
        btn_cancel_dialog.pack(side=tk.LEFT, padx=10)

        if row_id == 0:
            self.checked_img = tk.PhotoImage(file='img/checked.png')
            btn_checked_dialog = tk.Button(toolbar_child, text='Додати', command=self.destroy, bg='#d7d8e0', bd=0,
                                           compound=tk.TOP, image=self.checked_img)
            btn_checked_dialog.pack(side=tk.LEFT, padx=10)

            btn_checked_dialog.bind('<Button-1>',
                                    lambda event: DB().records(self.entry_name.get(), self.entry_inv_nomer.get(),
                                                               self.entry_PIB.get(), self.entry_division.get(),
                                                               self.entry_data_in.get(), self.entry_data_out.get()))

        ########################################################################

        place_x = 50
        place_y = 150

        label_title = tk.Label(self, text="Додати дані - Взятий на облік комп'ютерна техніка:", font=8)
        label_title.place(x=place_x + 100, y=place_y - 60)
        label_name = tk.Label(self, text='Матеріальна цінність:', font=8)
        label_name.place(x=place_x, y=place_y)
        label_inv_nomer = tk.Label(self, text='Інв. номер:', font=8)
        label_inv_nomer.place(x=place_x + 550, y=place_y)
        label_PIB = tk.Label(self, text='ПІБ:', font=8)
        label_PIB.place(x=place_x + 160, y=place_y + 50)
        label_division = tk.Label(self, text='Підрозділ:', font=8)
        label_division.place(x=place_x + 105, y=place_y + 100)
        label_data_in = tk.Label(self, text='Дата введення:', font=8)
        label_data_in.place(x=place_x + 55, y=place_y + 150)
        label_data_out = tk.Label(self, text='Дата зняття:', font=8)
        label_data_out.place(x=place_x + 535, y=place_y + 150)

        self.entry_name = ttk.Entry(self, width=50)
        self.entry_name.place(x=place_x + 210, y=place_y + 5)
        self.entry_inv_nomer = ttk.Entry(self, width=20)
        self.entry_inv_nomer.place(x=place_x + 665, y=place_y + 5)
        self.entry_PIB = ttk.Entry(self, width=50)
        self.entry_PIB.place(x=place_x + 210, y=place_y + 55)
        self.entry_division = ttk.Entry(self, width=50)
        self.entry_division.place(x=place_x + 210, y=place_y + 105)
        self.entry_data_in = ttk.Entry(self, width=20)
        self.entry_data_in.place(x=place_x + 210, y=place_y + 155)
        self.entry_data_out = ttk.Entry(self, width=20)
        self.entry_data_out.place(x=place_x + 665, y=place_y + 155)

        if row_id != 0:
            # Вывод на экран информации с базы данных
            self.conn = sqlite3.connect('accounting.db')  # Соединение с базой данных
            self.c = self.conn.cursor()  # Взаимодействие с базой
            self.c.execute('''SELECT * FROM accounting WHERE add_id=?''', [row_id])
            row = self.c.fetchone()

            self.entry_name.insert(0, row[1])
            self.entry_inv_nomer.insert(0, row[2])
            self.entry_PIB.insert(0, row[3])
            self.entry_division.insert(0, row[4])
            self.entry_data_in.insert(0, row[5])
            self.entry_data_out.insert(0, row[6])

            self.checked_img = tk.PhotoImage(file='img/checked.png')
            btn_checked_dialog = tk.Button(toolbar_child, text='Оновити', command=self.destroy, bg='#d7d8e0', bd=0,
                                           compound=tk.TOP, image=self.checked_img)
            btn_checked_dialog.pack(side=tk.LEFT, padx=10)

            btn_checked_dialog.bind('<Button-1>',
                                    lambda event: DB().update_records(self.entry_name.get(), self.entry_inv_nomer.get(),
                                                                      self.entry_PIB.get(), self.entry_division.get(),
                                                                      self.entry_data_in.get(),
                                                                      self.entry_data_out.get(),
                                                                      row_id))
            # END

        # Дочернее окно поверх основного

    def grab_focus(self):
        self.grab_set()
        self.focus_set()
        self.wait_window()
