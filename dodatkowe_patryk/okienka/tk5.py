import tkinter

root = tkinter.Tk()
root.title('Nasza przykładowa apka')
root.geometry('800x600')

# atrybuty komponentów graficznych można ustawiać od razu podczas ich tworzenia:
label1 = tkinter.Label(master=root,
                       text='Ala ma kota',
                       font='Arial 40 bold',
                       fg='#0000FF',
                       bg='#AAFFFF')
label1.pack()

# atrybuty komponentów graficznych można też ustawiać
# wywołując metodę configure na już istniejącym obiekcie
label2 = tkinter.Label(master=root)
label2.configure(text='Ola ma psa', font=('Times New Roman', 37, 'italic'))
label2.configure(fg='red', bg='yellow')
label2.pack()

# Funkcję obsługującą zdarzenie można też stworzyć "w miejscu" za pomocą wyrażenia lambda.
button1 = tkinter.Button(master=root, text='Kliknij mnie',
                         font='Roboto 40 bold',
                         fg='blue', bg='#FFCCFF',
                         command=lambda: print('ojej, ktoś nacisnął guzik'))
button1.pack()

root.mainloop()
