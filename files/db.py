import sqlite3


conn = sqlite3.connect("hack.db")
cursor = conn.cursor()
 
# Создание таблицы
cursor.execute("""CREATE TABLE deadlines
                  (title text, name text, short_name text,
                   code text)
               """)

# Вставляем данные в таблицу
cursor.execute("""INSERT INTO deadlines
                  VALUES ('Факультет', 'Факультет инфокоммуникационных технологий', 'ФИКТ',
                  'код')"""
               )
 
# Сохраняем изменения
conn.commit()
 
# Вставляем множество данных в таблицу используя безопасный метод "?"
deadlines = [('Факультет', 'Факультет инфокоммуникационных технологий', 'ФИКТ','код'),
          ('Факультет', 'Факультет безопасности', '','код'),
          ('Факультет', 'Факультет управления', '','код'),
          ('Факультет', 'Факультет ', '','код')]
 
cursor.executemany("INSERT INTO deadlines VALUES (?,?,?,?,?)", deadlines)
conn.commit()