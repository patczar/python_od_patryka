import tkinter
from tkinter import messagebox


def policz_koszt_przejazdu():
    try:
        dystans = int(dystans_entry.get())
        spalania = float(spalanie_entry.get())
        cena = float(cena_entry.get())
        koszt = (dystans / 100) * spalania * cena
        wynik_label.configure(text=f'Wynik: {koszt}')
    except ValueError:
        messagebox.showerror('Błędne dane!', 'Musisz wprowadzić wartości liczbowe!')


root = tkinter.Tk()
root.columnconfigure(1, weight=1)
dystans_label = tkinter.Label(master=root, text='Dystans')
dystans_label.grid(row=0, column=0)
dystans_entry = tkinter.Entry(master=root)
dystans_entry.grid(row=0, column=1, sticky=tkinter.EW)
spalanie_label = tkinter.Label(master=root, text='Spalanie')
spalanie_label.grid(row=1, column=0)
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.grid(row=1, column=1, sticky=tkinter.EW)
cena_label = tkinter.Label(master=root, text='Cena')
cena_label.grid(row=2, column=0)
cena_entry = tkinter.Entry(master=root)
cena_entry.grid(row=2, column=1, sticky=tkinter.EW)
policz_button = tkinter.Button(master=root, text='Policz', command=policz_koszt_przejazdu)
policz_button.grid(row=3, column=0)
wynik_label = tkinter.Label(master=root, text='Wynik: - ')
wynik_label.grid(row=3, column=1, sticky=tkinter.EW)
root.title('Kalkulator Spalania')
root.mainloop()
