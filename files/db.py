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
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
 
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()