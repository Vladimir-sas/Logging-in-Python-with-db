from tkinter import *


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


    login_label = Label(reg_window,text = "Логин:").place(x=10,y=50)
    password_label = Label(reg_window, text="Пароль:").place(x=10,y=80)

    login_ent = Entry(reg_window,textvariable = login_var)
    login_ent.place(x=70,y=50)

    password_ent = Entry(reg_window,textvariable = password_var)
    password_ent.place(x=70,y = 80)

    def add_to_db():#добавление данных в базу
        print(f'Логин:{login_ent.get()}',f' Пароль:{password_ent.get()}' ,sep = " | ")



    reg_btn = Button(reg_window, text="Зарегистрироваться", background="green", foreground="black",activebackground="red", command=add_to_db).place(x = 50,y = 120)

def enter_win():#окно входа
    enter_window = Toplevel(root)
    enter_window.geometry("200x200")
    enter_window.title("Вкид")

reg_btn = Button(root, text="Регистрация", width=20, background="green", foreground="black",activebackground="red",command = reg_win).place(x=130, y=200)

enter_btn = Button(root, text="Вкид", width=20, background="green", foreground="black", activebackground="red",command = enter_win).place(x=130, y=230)



root.mainloop()
