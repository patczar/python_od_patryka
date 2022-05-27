import tkinter

# Ta wersja funkcji akcja jest uniwersalna: może zostać wywołana bez paramtru (jak robi button)
# oraz z parametrem (jak robi bind)
def akcja(event = None):
    global poleTekstowe, label2

    imie = poleTekstowe.get()
    if imie.strip():
        label2.configure(text=f'Witaj {imie}')
    else:
        label2.configure(text='')

def main():
    global poleTekstowe, label2

    root = tkinter.Tk()

    root.title('Rozmowa')
    root.geometry('800x600')

    label1 = tkinter.Label(master=root, text='Jak masz na imię?', fg='black', font=('Arial', 24, 'bold'))
    label1.pack()

    poleTekstowe = tkinter.Entry(root, font=('Consolas', 24), bg='white')
    poleTekstowe.pack()

    button1 = tkinter.Button(master=root, text="OK", font=('Arial', 24, 'bold'), command=akcja)
    button1.pack()

    poleTekstowe.bind('<Return>', akcja)

    label2 = tkinter.Label(master=root, text='', fg='blue', font=('Arial', 24, 'bold'))
    label2.pack()

    root.mainloop()

if __name__ == '__main__':
    main()

