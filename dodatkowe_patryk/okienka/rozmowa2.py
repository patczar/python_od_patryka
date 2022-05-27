import tkinter

# w tej wersji program podzieliłem na funkcje, a wspólne zmienne zadeklarowałem jako global

def main():
    global poleTekstowe, label2

    root = tkinter.Tk()

    root.title('Rozmowa')
    root.geometry('800x600')

    label1 = tkinter.Label(master=root, text='Jak masz na imię?', fg='black', font=('Arial', 24, 'bold'))
    label1.pack()

    poleTekstowe = tkinter.Entry(root, font=('Consolas', 24), bg='white')
    poleTekstowe.pack()

    button1 = tkinter.Button(master=root, text='OK', font=('Arial', 24, 'bold'), command=akcja)
    button1.pack()

    label2 = tkinter.Label(master=root, text='', fg='blue', font=('Arial', 24, 'bold'))
    label2.pack()

    root.mainloop()


def akcja():
    global  poleTekstowe, label2
    imie = poleTekstowe.get()
    label2.configure(text=f'Witaj {imie}!')


if __name__ == '__main__':
    main()
