import tkinter
from tkinter import messagebox

licznik = 0

def co_ma_sie_stac1():
    global licznik
    licznik += 1
    messagebox.showinfo(title='Informacja',
                        message=f'Naciśnięto pierwszy guzik po raz {licznik}')



root = tkinter.Tk()
root.geometry('800x600')

label1 = tkinter.Label(master=root, text='Pierwszy napis',
                       fg='blue', font='Arial 40 bold')
label1.pack()

label2 = tkinter.Label(master=root, text='Drugi napis')
label2.pack()

tkinter.Label(master=root, text='Trzeci napis', font='Roboto 40').pack()


button1 = tkinter.Button(master=root, text='Licznik', font=('Arial', 24, 'bold'), command=co_ma_sie_stac1)
button1.pack()

label2.configure(text='Jak masz na imię?', font='Times 33 italic', fg='red')

poleTekstowe = tkinter.Entry(root, font=('Consolas', 24), fg='#880000', bg='#FFFFEE')
poleTekstowe.pack()

button2 = tkinter.Button(master=root, text='Powitaj', font=('Arial', 24, 'bold'))
button2.pack()

label4 = tkinter.Label(master=root, font='Roboto 40', fg='green')
label4.pack()

def co_ma_sie_stac2():
    imie = poleTekstowe.get()
    label4.configure(text=f'Witaj {imie}')

button2.configure(command=co_ma_sie_stac2)

root.mainloop()
