from tkinter import Tk, Label, Button

def co_ma_sie_stac():
    global licznik, label2
    licznik += 1
    label2.configure(text=f'Licznik: {licznik}')


licznik = 0

root = Tk()
root.title('Nasza przykładowa apka')
root.geometry('800x600')

# atrybuty komponentów graficznych można ustawiać od razu podczas ich tworzenia:
label1 = Label(master=root,
                       text='Ala ma kota',
                       font='Arial 40 bold',
                       fg='#0000FF',
                       bg='#AAFFFF')
label1.pack()

# atrybuty komponentów graficznych można też ustawiać
# wywołując metodę configure na już istniejącym obiekcie
label2 = Label(master=root)
label2.configure(text='Licznik: 0', font=('Arial', 36, 'bold'))
label2.configure(fg='red', bg='white')
label2.pack()

# Funkcja co_ma_sie_stac zostanie odpalona gdy użytkownik naciśnie guzik
button1 = Button(master=root, text='Kliknij mnie',
                         font='Roboto 40 bold',
                         fg='blue', bg='#FFCCFF',
                         command=co_ma_sie_stac)
button1.pack()

root.mainloop()
