import tkinter as tk
from modules import database_handler as dbh

def startGui():
    mainWindow = tk.Tk()
    mainWindow.geometry("600x400")
    mainWindow.title("Ana Ekran")
    mainWindow.resizable(False, False)
    Login = tk.Tk() #Ana pencereyi oluşturuyoruz
    Login.geometry("300x400") #pencere geometrisini belirliyoruz
    Login.resizable(width=False,height=False) #yeniden boyutlandırmayı kısıtlıyoruz
    Login.title("login")
    empty_space = tk.Label(Login,pady=10) #hizlamalar için boş bir label işimizi kolaylaştırabilir.
    loginlabel1 = tk.Label(Login, text="Kullanıcı Adı Giriniz :") #Kullanıcı Adı Label'ı
    loginlabel2 = tk.Label(Login, text="Şifre Giriniz :") #Şifre Label'ı
    username_entry = tk.Entry(Login) #Kullanıcı adı girişi
    pwd_entry = tk.Entry(Login) #şifre Girişi
    login_button = tk.Button(Login,text="Giriş Yap",width="17",pady=10,command= lambda: dbh.login(Login,username_entry.get(),pwd_entry.get()))
    empty_space.pack()
    loginlabel1.pack()
    username_entry.pack()
    loginlabel2.pack()
    pwd_entry.pack()
    login_button.pack(pady=10)
    Login.mainloop()



