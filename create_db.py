import sqlite3

class DB:
    # Создание конструктор класса для DB
    def __init__(self):
        self.conn = sqlite3.connect('accounting.db') #Соединение с базой данных
        self.c = self.conn.cursor() #Взаимодействие с базой
        self.c.execute('''SELECT * FROM accounting''')

    # Добавляем в поля вводимые значения
    def insert_data(self, add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out):
        self.c.execute('''INSERT INTO accounting(add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out)VALUES (?, ?, ?, ?, ?, ?)''',
                       (add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out))
        self.conn.commit()

    # Функция поиска
    def search_records(self, add_name, add_inv_nomer, add_pib):
        if not add_name:
            if not add_inv_nomer:
                if not add_pib:
                 print('Нема даних для пошуку')
                else:
                    add_pib = ('%' + add_pib + '%',)  # Подстановочные символы ищет любое значение
                    self.c.execute('''SELECT * FROM accounting WHERE add_pib LIKE ?''',
                                   add_pib)  # Обращение к полю description LIKE это наш запрос
            else:
                add_inv_nomer = ('%' + add_inv_nomer + '%',)  # Подстановочные символы ищет любое значение
                self.c.execute('''SELECT * FROM accounting WHERE add_inv_nomer LIKE ?''',
                               add_inv_nomer)  # Обращение к полю description LIKE это наш запрос
        else:
            add_name = ('%' + add_name + '%',)  # Подстановочные символы ищет любое значение
            self.c.execute('''SELECT * FROM accounting WHERE add_name LIKE ?''',
                           add_name)  # Обращение к полю description LIKE это наш запрос

    def add_db(self):
        self.conn = sqlite3.connect('accounting.db') #Соединение с базой данных
        self.c = self.conn.cursor() #Взаимодействие с базой
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS accounting (add_id integer primary key, add_name text,
                                                      add_inv_nomer integer, add_pib text, add_division text,
                                                      add_data_in text, add_data_out text)'''
        )
        self.conn.commit()

    def records(self, add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out):
        self.insert_data(add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out)



    def update_records(self, add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out, row_id):
        self.c.execute('''UPDATE accounting SET add_name=?, add_inv_nomer=?, add_pib=?, add_division=?, add_data_in=?, add_data_out=? WHERE add_id=?''',
                          (add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out, row_id))  # Обновление данных и вытягивает ID с первого столбца
        #self.db.c.execute('''UPDATE accounting SET description=?, COSTS=?, TOTAL=? WHERE ID=?''',
        #                  (description, costs, total, self.tree.set(self.tree.selection()[0], '#1'),))  # Обновление данных и вытягивает ID с первого столбца
        self.conn.commit()  # Сохраним изменения

    #def view_records(self):  # Передача данных
    #    self.c.execute('''SELECT * FROM accounting''')
    #    [self.tree.delete(i) for i in self.tree.get_children()]  # Очистна данных
    #    # Генератор
    #    [self.tree.insert('', 'end', values=row) for row in
    #     self.c.fetchall()]  # Добавление новых значений после предедущих

    #def view_delete(self):
    #    self.c.execute('''SELECT * FROM accounting''')
    #    print('Я создал базу5')

    #def view_insert(self, db_fetchall):
    #    self.conn = sqlite3.connect('accounting.db')  # Соединение с базой данных
    #    self.c = self.conn.cursor()  # Взаимодействие с базой
    #    self.c.execute('''SELECT * FROM accounting''')
    #    db_fetchall = self.c.fetchall()  # Добавление новых значений после предедущих
    #    return db_fetchall
    #    #print(db_fetchall)