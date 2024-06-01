from tkinter import *
from tkinter import ttk

clicks = 0


def Label():
    global Label
    Label = (f'\nСалмаков Максим Ильич'
             f'\nпрограмист'
             f'\nпрограмирование'
             f'\nмужской'
             f'\nГалушина 10'
             f'\n10.02.2015')
    btn["text"] = f"{Label}"


root = Tk()
root.title("Departament")
root.geometry("350x300")

btn = ttk.Button(text="Clicks", command=Label)
btn.pack()

root.mainloop()
