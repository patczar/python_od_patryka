import tkinter
from tkinter import messagebox


def przycik_wcisniety():
    dystans = int(entry_dystans.get())
    spalanie = float(entry_spalanie.get())
    cena = float(entry_cena.get())
    wynik = (dystans / 100) * spalanie * cena
    messagebox.showinfo(
        title='Koszt podróży',
        message=f'Koszt podróży to {wynik} PLN',
    )


root = tkinter.Tk()
label_dystans = tkinter.Label(master=root, text='Dystans:')
label_dystans.pack()
entry_dystans = tkinter.Entry(master=root)
entry_dystans.pack()
label_spalanie = tkinter.Label(master=root, text='Spalanie:')
label_spalanie.pack()
entry_spalanie = tkinter.Entry(master=root)
entry_spalanie.pack()
label_cena = tkinter.Label(master=root, text='Cena:')
label_cena.pack()
entry_cena = tkinter.Entry(master=root)
entry_cena.pack()
button = tkinter.Button(master=root, text='Policz', command=przycik_wcisniety)
button.pack()
root.title('Kalkulator kosztów podróży')
root.mainloop()
