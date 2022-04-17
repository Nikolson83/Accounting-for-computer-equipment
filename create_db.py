import sqlite3

class DB:
    # Создание конструктор класса для DB
    def __init__(self):
        self.conn = sqlite3.connect('accounting.db') #Соединение с базой данных
        self.c = self.conn.cursor() #Взаимодействие с базой
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS accounting (add_id integer primary key, add_name text,
                                                      add_inv_nomer integer, add_pib text, add_division text,
                                                      add_data_in text, add_data_out text)'''
        )
        self.conn.commit()
    # Добавляем в поля вводимые значения
    def insert_data(self, add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out):
        self.c.execute('''INSERT INTO accounting(add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out)
                          VALUES (?, ?, ?, ?, ?, ?)''',(add_name, add_inv_nomer, add_pib, add_division, add_data_in, add_data_out))
        self.conn.commit()

