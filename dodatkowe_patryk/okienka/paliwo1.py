# Napisz program okienkowy, który na podstawie wprowadzonych danych oblicza kosz przejazdu samochodem.

import tkinter

def akcja():
    dystans = float(entry_dystans.get())
    spalanie = float(entry_spalanie.get())
    cena = float(entry_cena.get())
    kwota = dystans * spalanie * cena / 100
    label_wynik.configure(text=kwota)


font = ('Arial', 32)
tlo = '#F8FFDD'

root = tkinter.Tk()
root.geometry("600x600")

label_dystans = tkinter.Label(master=root, text='Dystans:', font=font)
label_dystans.pack()
entry_dystans = tkinter.Entry(master=root, font=font, bg=tlo)
entry_dystans.pack()
label_spalanie = tkinter.Label(master=root, text='Spalanie:', font=font)
label_spalanie.pack()
entry_spalanie = tkinter.Entry(master=root, font=font, bg=tlo)
entry_spalanie.pack()
label_cena = tkinter.Label(master=root, text='Cena:', font=font)
label_cena.pack()
entry_cena = tkinter.Entry(master=root, font=font, bg=tlo)
entry_cena.pack()
button = tkinter.Button(master=root, text='Policz', font=font, command=akcja)
button.pack()

label_wynik = tkinter.Label(master=root, text='Koszt: ', font=font)
label_wynik.pack()

root.title('Kalkulator kosztów podróży')
root.mainloop()
