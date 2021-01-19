from tkinter import *
import sqlite3

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

        cur.execute('INSERT INTO ent_conf(login, password) VALUES (?,?)',to_db)

        cur.execute('SELECT login,password FROM ent_conf')
        rows = cur.fetchall()


        for row in rows:
            print(row)

        # cur.execute('DELETE from ent_conf')


        conn.commit()




    reg_btn = Button(reg_window, text="Зарегистрироваться", background="green", foreground="black",activebackground="red", command=add_to_db).place(x = 50,y = 120)

def enter_win():#окно входа
    enter_window = Toplevel(root)
    enter_window.geometry("200x200")
    enter_window.title("Вкид")

reg_btn = Button(root, text="Регистрация", width=20, background="green", foreground="black",activebackground="red",command = reg_win).place(x=130, y=200)

enter_btn = Button(root, text="Вход", width=20, background="green", foreground="black", activebackground="red",command = enter_win).place(x=130, y=230)



root.mainloop()


