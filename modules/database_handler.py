import sqlite3
import sqlite3 as sql
try:
    conn = sql.connect("obs_db.db")
    cursor = conn.cursor()
except sqlite3.Error as e:
    print(e)

create_table = '''CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT
);'''
create_admin = '''CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT UNIQUE,
    pwd TEXT
);'''
cursor.execute(create_table)
cursor.execute(create_admin)
def add_student(conn, student_data):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (student_id, name, surname, email, phone) VALUES (?, ?, ?, ?, ?)",
                       student_data)
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(e)
        return None

def add_admin(conn, admin_data):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO admins (id, name, surname, email, pwd) VALUES (?, ?, ?, ?, ?)",
                       admin_data)
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(e)
        return None
admin_data = [1,"Barış","Çetin","bariscetintr@gmail.com",12345]

add_admin(conn,admin_data)