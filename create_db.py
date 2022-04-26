import sqlite3

class DB:
    # Создание конструктор класса для DB
    def __init__(self):
        self.conn = sqlite3.connect('accounting.db') #Соединение с базой данных
        self.c = self.conn.cursor() #Взаимодействие с базой
        print('Я создал базу')

    # Добавляем в поля вводимые значения
    def insert_data(self, add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out):
        self.c.execute('''INSERT INTO accounting(add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out)VALUES (?, ?, ?, ?, ?, ?)''',
                       (add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out))
        self.conn.commit()
        print('Я создал базу1')

    def search_records(self, add_name, add_inv_nomer, add_pib):
        add_name = ('%' + add_name + '%',) #Подстановочные символы ищет любое значение
        add_inv_nomer = ('%' + add_inv_nomer + '%',)  # Подстановочные символы ищет любое значение
        add_pib = ('%' + add_pib + '%',)  # Подстановочные символы ищет любое значение
        self.c.execute('''SELECT * FROM finance WHERE add_name LIKE ?''', add_name) # Обращение к полю add_name LIKE это наш запрос
        self.conn.commit()
        print('Я создал базу2')

    def add_db(self):
        self.conn = sqlite3.connect('accounting.db') #Соединение с базой данных
        self.c = self.conn.cursor() #Взаимодействие с базой
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS accounting (add_id integer primary key, add_name text,
                                                      add_inv_nomer integer, add_pib text, add_division text,
                                                      add_data_in text, add_data_out text)'''
        )
        self.conn.commit()
        print('Я создал базу3')

    def records(self, add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out):
        self.insert_data(add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out)
        print('Я создал базу4')

    #def view_records(self):  # Передача данных
    #    self.c.execute('''SELECT * FROM accounting''')
    #    [self.tree.delete(i) for i in self.tree.get_children()]  # Очистна данных
    #    # Генератор
    #    [self.tree.insert('', 'end', values=row) for row in
    #     self.c.fetchall()]  # Добавление новых значений после предедущих

    #def view_delete(self):
    #    self.c.execute('''SELECT * FROM accounting''')
    #    print('Я создал базу5')

    #def view_insert(self):
    #    self.c.fetchall()  # Добавление новых значений после предедущих
    #    print('Я создал базу6')