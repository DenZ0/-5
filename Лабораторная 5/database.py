import sqlite3


conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("DROP TABLE books;")
c.execute("CREATE TABLE books (id int auto_increment primary key, author varchar, title varchar, genre varchar);")
lines = [["Есенин","Письмо к женщине", "Художественное произведение"],
         ["Есенин", "Чёрный человек", "Поэзия"],
         ["Достоевский", "Бедные люди", "Роман"],
         ["Достоевский", "Идиот", "Роман"],
         ["Братья Стругацкие", "Пикник на обочине", "Научная фантастика"],
         ["Братья Стругацкие", "Трудно быть богом", "Научная фантастика"],
         ["Николай Грошев", "Эволюция Хакайна", "Фантастика"],
         ["Александр Беляев", "Человек амфибия", "Фантастика"]]


def create_new_line(author, title, genre):
    c.execute(f"INSERT INTO books (author, title, genre) VALUES('{author}', '{title}', '{genre}');")

def delete_line_by_field(field, value):
    c.execute(f'DELETE FROM books WHERE {field}="{value}"')

def print_data():
    row = c.fetchall()
    for line in row:
        print(*["%-20s" % f'|{x}' for x in line if x])

def get_books(author=None):
    if author:
        c.execute(f'SELECT * FROM books WHERE author="{author}"')
    else:
        c.execute(f'SELECT * FROM books')
    print_data()

def get_4_first_lines():
    c.execute(f'SELECT * FROM books LIMIT 4')
    print_data()

def update_line(field, value, new_value):
    c.execute(f'UPDATE books SET {field}="{new_value}" WHERE {field}="{value}";')
    print_data()

for line in lines:
    create_new_line(*line)

update_line('title', 'Идиот', 'Бедные люди')


conn.commit()