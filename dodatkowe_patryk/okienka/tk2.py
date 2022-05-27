import tkinter

root = tkinter.Tk()
root.geometry('800x600')

# Różne parametry (np. wygląd) można podać od razu podczas tworzenia komponentu.
label1 = tkinter.Label(master=root, text='Pierwszy napis',
                       fg='blue', font='Arial 40 bold')
label1.pack()

label2 = tkinter.Label(master=root, text='Drugi napis')
label2.pack()

tkinter.Label(master=root, text='Trzeci napis', font='Roboto 40').pack()

# Za pomocą configure w dowolnym momencie można zmienić parametry komponentu: wygląd, tekst itp.
# Z grubsza te same parametry, które ustawia się podczas towrzenia obiektu.
label2.configure(text='Nowy drugi napis', font='Times 33 italic', fg='red')

# specyfikację czcionki można też podać w formie tupli lub listy
button1 = tkinter.Button(master=root, text='Klik Klik', font=('Arial', 24, 'bold'))
button1.pack()

button2 = tkinter.Button(master=root, text='Guzik 2')
button2.pack()

# kolory można też podawać jak w CSS #RRGGBB (red green blue, każdy w zakresie od 00 do FF = 255)
poleTekstowe = tkinter.Entry(root, font=('Consolas', 24), fg='#880000', bg='#FFFFEE')
poleTekstowe.pack()

root.mainloop()
