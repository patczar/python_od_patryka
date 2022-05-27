import tkinter
from tkinter import messagebox

def co_ma_sie_stac1():
    messagebox.showinfo(title='Informacja',
                        message=f'Ojej naciśnięto pierwszy guzik')


def co_ma_sie_stac2():
    '''Ta funkcja zostanie wywołana, gdy użytkownik naciśnie guzik 2'''
    print('Kliknięto guzik 2')


root = tkinter.Tk()
root.geometry('800x600')

label1 = tkinter.Label(master=root, text='Pierwszy napis',
                       fg='blue', font='Arial 40 bold')
label1.pack()

label2 = tkinter.Label(master=root, text='Drugi napis')
label2.pack()

tkinter.Label(master=root, text='Trzeci napis', font='Roboto 40').pack()

label2.configure(text='Nowy drugi napis', font='Times 33 italic', fg='red')

button1 = tkinter.Button(master=root, text='Klik Klik', font=('Arial', 24, 'bold'), command=co_ma_sie_stac1)
button1.pack()

# Jako paramter command przekazujemy funkcję.
# Przkazujemy funkcję jako wartość - nie wywołujemy tej funkcji TERAZ, tylko ją przekazujemy.
# To tkinter wywoła tę funkcję, gdy użytkownik naciśnie guzik.
button2 = tkinter.Button(master=root, text='Guzik 2', command=co_ma_sie_stac2)
button2.pack()

poleTekstowe = tkinter.Entry(root, font=('Consolas', 24), fg='#880000', bg='#FFFFEE')
poleTekstowe.pack()

root.mainloop()
