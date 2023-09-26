# gui.py

import tkinter as tk
from modules import database_handler as dbh
name_entry = None
surname_entry = None
email_entry = None
phone_entry = None
def startGui():
    Login = tk.Tk()
    Login.geometry("300x150")
    Login.title("Login")

    # Login ekranı içeriği
    login_label = tk.Label(Login, text="Kullanıcı Adı:")
    username_entry = tk.Entry(Login)
    password_label = tk.Label(Login, text="Şifre:")
    password_entry = tk.Entry(Login)
    login_button = tk.Button(Login, text="Giriş Yap", command=lambda: handle_login(Login, username_entry.get(), password_entry.get()))
    password_entry.config(show=password_entry.get())
    login_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    login_button.pack()

    Login.mainloop()

def handle_login(login_window, username, password):
    user = dbh.login(username, password)
    if user:
        print(f"Giriş Başarılı! {username}")
        login_window.destroy()  # Login penceresini kapat
        open_student_list()  # Öğrenci listesi penceresini aç
    else:
        print("Giriş Başarısız")

def open_student_list():
    global name_entry, surname_entry, email_entry, phone_entry
    StudentList = tk.Tk()
    StudentList.geometry("360x450")
    StudentList.title("Öğrenci Listesi")
    StudentList.resizable(False,False)

    # Öğrenci Listesi için Listbox ekleyin
    student_listbox = tk.Listbox(StudentList)
    student_listbox.grid(row=5, column=0, rowspan=100,columnspan=4, padx=10, pady=10, sticky="nsew")

    # Öğrenci Ekle butonu
    add_student_button = tk.Button(StudentList,width=17, text="Öğrenci Ekle", command=lambda: save_student())
    add_student_button.grid(row=0, column=1, padx=10, pady=5)

    # Öğrenci Sil butonu
    delete_student_button = tk.Button(StudentList,width=17, text="Öğrenci Sil", command=delete_student)
    delete_student_button.grid(row=1, column=1, padx=10, pady=5)

    # Öğrenci Düzenle butonu
    edit_student_button = tk.Button(StudentList,width=17, text="Öğrenci Düzenle", command=edit_student)
    edit_student_button.grid(row=2, column=1, padx=10, pady=5)
    # Öğrenci Listesi Yenile butonu
    edit_student_button = tk.Button(StudentList,width=17, text="Yenile ", command=lambda:get_students(student_listbox))
    edit_student_button.grid(row=3, column=1, padx=10, pady=5)
    # Öğrenci ekleme formu için Label'lar ve Entry'ler
    name_label = tk.Label(StudentList, text="Adı:")
    name_label.grid(row=0, column=2, padx=10, pady=5)

    name_entry = tk.Entry(StudentList)
    name_entry.grid(row=0, column=3, padx=10, pady=5)

    surname_label = tk.Label(StudentList, text="Soyadı:")
    surname_label.grid(row=1, column=2, padx=10, pady=10)

    surname_entry = tk.Entry(StudentList)
    surname_entry.grid(row=1, column=3, padx=10, pady=10)

    email_label = tk.Label(StudentList, text="E-posta:")
    email_label.grid(row=2, column=2, padx=10, pady=10)

    email_entry = tk.Entry(StudentList)
    email_entry.grid(row=2, column=3, padx=10, pady=10)

    phone_label = tk.Label(StudentList, text="Telefon:")
    phone_label.grid(row=3, column=2, padx=10, pady=10)

    phone_entry = tk.Entry(StudentList)
    phone_entry.grid(row=3, column=3, padx=10, pady=10)


    StudentList.mainloop()


def delete_student():
    # Öğrenci silme işlemini burada gerçekleştirin ve listbox'tan kaldırın.
    pass

def edit_student():
    # Öğrenci düzenleme işlemini burada gerçekleştirin.
    pass
def save_student():
    name = name_entry.get()
    surname = surname_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    # Öğrenciyi veritabanına kaydetmek için database_handler'dan ilgili fonksiyonu çağırın
    dbh.add_student(name, surname, email, phone)

def get_students(student_listbox):
    students = dbh.get_students()
    for student in students:
        student_listbox.insert(tk.END, f"{student[0]} - {student[1]} {student[2]} ({student[3]})")