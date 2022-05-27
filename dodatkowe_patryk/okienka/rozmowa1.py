import tkinter

root = tkinter.Tk()

root.title('Rozmowa')
root.geometry('800x600')

label1 = tkinter.Label(master=root, text='Jak masz na imię?', fg='black', font=('Arial', 24, 'bold'))
label1.pack()

poleTekstowe = tkinter.Entry(root, font=('Consolas', 24), bg='white')
poleTekstowe.pack()

def akcja():
    imie = poleTekstowe.get()
    label2.configure(text=f'Witaj {imie}!')

button1 = tkinter.Button(master=root, text='OK', font=('Arial', 24, 'bold'), command=akcja)
button1.pack()

label2 = tkinter.Label(master=root, text='', fg='blue', font=('Arial', 24, 'bold'))
label2.pack()

root.mainloop()

# odczytanie aktualnej wartości pola:   poleTekstowe.get()
# ustawienie nowej wartości w label-u : label2.configure(text='nowy tekst')

