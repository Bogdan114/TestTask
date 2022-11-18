from tkinter import *
from tkinter.ttk import Combobox
import encryption
import cifru

l_p = cifru.cifru1()

def click_button_r():
    aes_login.configure(state="normal")
    aes_password.configure(state="normal")
    
    aes_login.delete(0, END)
    aes_password.delete(0, END)

    if l_p.set(login.get(), password.get()):
        log_listbox.insert(END, "Succes creating login and password")
    else:
        log_listbox.insert(END, "Faild len(login) or len(password) = 0")
        return 0

    global login_encrypt
    global password_encrypt
    login_encrypt = l_p.encrypt(l_p.ret_login(), int(combo.get()))
    password_encrypt = l_p.encrypt(l_p.ret_pass(), int(combo.get()))
    
    aes_login.insert(END, login_encrypt)
    aes_password.insert(END, password_encrypt)

    log_listbox.insert(END, "Password and login successfully encrypted")
    
    aes_login.config(state= "disabled")
    aes_password.config(state= "disabled")
def click_button_rc():
    login_decrypt = l_p.decrypt(login_encrypt, login.get(), int(combo.get()))
    password_decrypt = l_p.decrypt(password_encrypt, password.get(), int(combo.get()))

    log_listbox.insert(END, "Password and login successfully dencrypted")

    login_decrypt = 'Login - ' + login_decrypt.decode('utf-8')
    password_decrypt = 'Password - ' + password_decrypt.decode('utf-8')

    log_listbox.insert(END, login_decrypt)
    log_listbox.insert(END, password_decrypt)

    
root = Tk()
root.title("Passwork program")
root.geometry("800x300")
root.resizable(False, False)

btn = Button(text="Зашифровать", command=click_button_r)
btn.place(x=350, y=55, width = 100)

btn = Button(text="Расшифровать", command=click_button_rc)
btn.place(x=350, y=85, width = 100)

combo = Combobox(root)
combo['value'] = (16, 32, 64, 128, 256)
combo.current(3)
combo.place(x=350, y=30, width = 100)

login_label = Label(text = "Login")
login_label.place(x=20, y=10, width = 30, height = 20)
login = Entry(text="Login")
login.place(x=20, y=30, width = 300)

password_label = Label(text = "Password")
password_label.place(x=20, y=50, width = 50, height = 20)
password = Entry(text="Password")
password.place(x=20, y=70, width = 300)

aes_login_label = Label(text = "Encrypted login")
aes_login_label.place(x=480, y=10, width = 85, height = 20)
aes_login = Entry(text="Login1")
aes_login.place(x=480, y=30, width = 300)

aes_password_label = Label(text = "Encrypted password")
aes_password_label.place(x=480, y=50, width = 105, height = 20)
aes_password = Entry(text="Password1")
aes_password.place(x=480, y=70, width = 300)

aes_password_label = Label(text = "Logs")
aes_password_label.place(x=20, y=100, width = 30, height = 20)

log_listbox = Listbox()
log_listbox.place(x=20, y=120, width = 760, height = 170)

scrollbar = Scrollbar(log_listbox)
scrollbar.pack(side = RIGHT, fill = BOTH)
log_listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = log_listbox.yview)


root.mainloop()
































