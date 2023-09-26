import sqlite3
from modules import gui
try:
    conn = sqlite3.connect("obs_db.db")
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


def login(loginwindow,username,pwd):
    cursor.execute('SELECT * FROM admins WHERE name = ? AND pwd = ?',(username,pwd))
    user = cursor.fetchone()
    if user:
        print(f"Giriş Başarılı! {username},{pwd}")
        global loginSuccess
        loginSuccess = True
        loginwindow.destroy()

    else:
        print("Giriş Başarısız")
        global loginSucces
        loginSuccess = False


def listadmin():
    cursor.execute("SELECT * FROM admins")
    userlist = cursor.fetchall()
    for user in userlist:
        print(user[0],user[1],user[2],user[3],user[4])
