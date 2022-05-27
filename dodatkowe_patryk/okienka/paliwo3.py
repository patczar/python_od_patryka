import tkinter
from tkinter import messagebox

def akcja(evt=None):
    global entry_dystans, entry_spalanie, entry_cena, label_wynik, label_wynik2, osoby

    try:
        dystans = float(entry_dystans.get())
        spalanie = float(entry_spalanie.get())
        cena = float(entry_cena.get())
        koszt = dystans * spalanie * cena / 100
        label_wynik.configure(text=f'Koszt: {koszt:.2f} zł')
        ilosc_osob = int(osoby.get())
        koszt2 = koszt / ilosc_osob
        label_wynik2.configure(text=f'Koszt na osobę: {koszt2:.2f} zł')
    except Exception as e:
        label_wynik.configure(text=f'')
        label_wynik2.configure(text=f'')
        messagebox.showerror('Błędne dane!', 'Musisz wprowadzić wartości liczbowe!')


def main():
    global entry_dystans, entry_spalanie, entry_cena, label_wynik, label_wynik2, osoby

    font = ('Arial', 32)
    tlo = '#F8FFDD'

    root = tkinter.Tk()
    root.geometry("600x600")

    label_dystans = tkinter.Label(master=root, text='Dystans:', font=font)
    label_dystans.pack()

    entry_dystans = tkinter.Entry(master=root, font=font, bg=tlo)
    entry_dystans.insert(tkinter.END, '100')
    entry_dystans.pack()

    label_spalanie = tkinter.Label(master=root, text='Spalanie:', font=font)
    label_spalanie.pack()

    entry_spalanie = tkinter.Entry(master=root, font=font, bg=tlo)
    entry_spalanie.insert(tkinter.END, '6.5')
    entry_spalanie.pack()

    label_cena = tkinter.Label(master=root, text='Cena:', font=font)
    label_cena.pack()

    entry_cena = tkinter.Entry(master=root, font=font, bg=tlo)
    entry_cena.insert(tkinter.END, '5.00')
    entry_cena.pack()

    label_osoby = tkinter.Label(master=root, text='Ilość osób:', font=font)
    label_osoby.pack()

    osoby = tkinter.Spinbox(root, from_=1, to=9, font=font, bg=tlo)
    osoby.pack()

    button = tkinter.Button(master=root, text='Policz', font=font, command=akcja)
    button.pack()

    label_wynik = tkinter.Label(master=root, text='Koszt: ', font=font)
    label_wynik.pack()

    label_wynik2 = tkinter.Label(master=root, text='Koszt na osobę: ', font=font)
    label_wynik2.pack()

    root.title('Kalkulator kosztów podróży')
    root.mainloop()

if __name__ == '__main__':
    main()
