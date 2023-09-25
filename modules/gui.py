import tkinter as tk
import main
from tkinter import PhotoImage
def startGui():
    Login = tk.Tk() #Ana pencereyi oluşturuyoruz
    Login.geometry("300x400") #pencere geometrisini belirliyoruz
    Login.resizable(width=False,height=False) #yeniden boyutlandırmayı kısıtlıyoruz
    Login.title("login")
    empty_space = tk.Label(pady=10) #hizlamalar için boş bir label işimizi kolaylaştırabilir.
    loginlabel1 = tk.Label(text="Kullanıcı Adı Giriniz :") #Kullanıcı Adı Label'ı
    loginlabel2 = tk.Label(text="Şifre Giriniz :") #Şifre Label'ı
    username_entry = tk.Entry() #Kullanıcı adı girişi
    pwd_entry = tk.Entry() #şifre Girişi
    login_button = tk.Button(text="Giriş Yap",width="17",pady=10,command= main.login)

    empty_space.pack()
    loginlabel1.pack()
    username_entry.pack()
    loginlabel2.pack()
    pwd_entry.pack()
    login_button.pack(pady=10)
    Login.mainloop()