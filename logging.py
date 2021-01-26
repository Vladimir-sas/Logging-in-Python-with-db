from tkinter import *
import sqlite3
from tkinter import messagebox



conn = sqlite3.connect('configs')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS ent_conf(
                login TEXT,
                password TEXT
                )""")

root = Tk()
root.geometry("400x400")
root.resizable(False, False)
root.title("бабл квас")

lbl = Label(root,text = "бабл квас").place(x=170,y = 100)



def reg_win(): # окно регистрации
    reg_window = Toplevel(root)
    reg_window.geometry("200x200")
    reg_window.title("Регистрация")

    login_var = StringVar()
    password_var = StringVar()
    nick_var = StringVar()


    login_label = Label(reg_window,text = "Логин:").place(x=10,y=50)
    password_label = Label(reg_window, text="Пароль:").place(x=10,y=80)
    password_label = Label(reg_window, text="Имя:").place(x=10, y=20)

    login_ent = Entry(reg_window,textvariable = login_var)
    login_ent.place(x=70,y=50)

    password_ent = Entry(reg_window,textvariable = password_var)
    password_ent.place(x=70,y = 80)

    nick_ent = Entry(reg_window, textvariable = nick_var)
    nick_ent.place(x=70, y=20)

    def add_to_db():#добавление данных в базу
        to_db = (login_ent.get(),password_ent.get())
        print(f'Логин:{login_ent.get()}',f' Пароль:{password_ent.get()}',f' Имя:{nick_ent.get()}' ,sep = " | ")



        cur.execute('SELECT login,password FROM ent_conf')
        rows = cur.fetchall()


        for row in rows:
            print(row)

        if to_db == row:
            messagebox.showinfo("бабл квас", "Логин и пароль уже заняты")
        else:
            cur.execute('INSERT INTO ent_conf(login, password) VALUES (?,?)', to_db)
            messagebox.showinfo("бабл квас", "Регистрация прошла успешно")
        # cur.execute('DELETE from ent_conf')


        conn.commit()




    reg_btn = Button(reg_window, text="Зарегистрироваться", background="green", foreground="black",activebackground="red", command=add_to_db).place(x = 50,y = 120)

def enter_win():#окно входа
    enter_window = Toplevel(root)
    enter_window.geometry("200x200")
    enter_window.title("Вкид")

    login_var1 = StringVar()
    password_var1 = StringVar()
    nick_var1 = StringVar()

    login_label1 = Label(enter_window, text="Логин:").place(x=10, y=50)
    password_label1 = Label(enter_window, text="Пароль:").place(x=10, y=80)
    password_label1 = Label(enter_window, text="Имя:").place(x=10, y=20)

    login_ent1 = Entry(enter_window, textvariable=login_var1)
    login_ent1.place(x=70, y=50)

    password_ent1 = Entry(enter_window, textvariable=password_var1)
    password_ent1.place(x=70, y=80)

    nick_ent1 = Entry(enter_window, textvariable=nick_var1)
    nick_ent1.place(x=70, y=20)

    def check():
        to_db = (login_ent1.get(), password_ent1.get())
        cur.execute('SELECT login,password FROM ent_conf')

        rows1 = cur.fetchall()

        for row1 in rows1:
            pass

        if to_db == row1:
            messagebox.showinfo("бабл квас","Вход оформлен")
        else:
            messagebox.showinfo("бабл квас", "Такого пользователя нет")

        conn.commit()



    ent_btn = Button(enter_window, text="Войти", background="green", foreground="black",
                    activebackground="red", command=check,width=20).place(x=30, y=120)

reg_btn = Button(root, text="Регистрация", width=20, background="green", foreground="black",activebackground="red",command = reg_win).place(x=130, y=200)

enter_btn = Button(root, text="Вход", width=20, background="green", foreground="black", activebackground="red",command = enter_win).place(x=130, y=230)




root.mainloop()