import sqlite3

def connect():
    conn = sqlite3.connect('libreria.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    try:
        conn = connect()
        conn.execute('''CREATE TABLE IF NOT EXISTS libros(
        id integer primary key autoincrement,
        title char(25) not null,
        author char(25) NOT NULL,
        resume TEXT NOT NULL);''')

        print('Tables created successfully')
    except sqlite3.Error as dbEx:
        print(dbEx)
    finally:
        conn.close()

print('Starting application ...')
create_tables()
print('Done!')