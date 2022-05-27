import tkinter
import tkinter.messagebox
import tkinter.ttk

# główne okno
root = tkinter.Tk()
root.title('Nasza pierwsza apka')
root.geometry('800x600')

# komponenty okna
# pierwszy parametr root oznacza, że komponent należy do tego okna
# poza nim można przekazywać wiele innych parametrów (technicznie: **kwargs),
# za pomocą których ustala się styl i zawartość komponentów
tekst1 = tkinter.Label(root, text='Ala ma kota', font='Arial')
tekst1.pack()

tekst2 = tkinter.Label(root, text='Ola ma psa', font='Times 40 italic', foreground='red')
tekst2.pack()

tekst3 = tkinter.Label(root, text='Trzeci napis')
tekst3.pack()

# własności (wygląd, tekst itp.) można ustawiać także później, już po utworzeniu obiektów, za pomocą configure:
tekst3.configure(font=('Arial', 36, 'bold'), foreground='#008844')

font1 = ('Arial', 30)
pole = tkinter.Entry(root, font=font1, background='white')
pole.pack()

# pole tekstowe (Entry) nie przyjmuje parametru text
# nie zadziała:
# pole = tkinter.Entry(root, text='halo halo', font=font1, background='white')

pole2 = tkinter.Entry(root, font=font1, bg='white', fg='red')
pole2.pack()

# początkowy tekst, który ma być wyświetlony w polu można ustawić takim poleceniem:
pole2.insert(tkinter.END, 'początkowy tekst')

def co_robic():
    tkinter.messagebox.showinfo('Ping', 'Ojej, naciśnięto guzik')

# Aby po wciśnięciu guzika nastapiła reakcja (żeby progra mcoś zrobił),
# to guzikowi przypisujemy komendę : command=
# tą komendą powinna być funkcja, która nie przyjmuje żadnego parametru
guzik = tkinter.Button(root, text='OK', font=font1, command=co_robic)
guzik.pack()

combo = tkinter.ttk.Combobox(root, values=['Ala', 'Ola', 'Ela'], font='Arial 28')
combo.pack()

#myphoto = tkinter.PhotoImage(file='obrazek.png')
#img_label = tkinter.Label(master=root, image=myphoto)

guzikBlue = tkinter.Button(root, text='Niebieskie', fg='blue')
guzikBlue.pack()
guzikRed = tkinter.Button(root, text='Czerwone', fg='red')
guzikRed.pack()

# w akcji obsługi zdarzeń możemy odczytywać i modyfikować wartości w komponentach
# - o ile tylko mamy dostęp do nich jako do zmiennych (tu są to zmienne globalne: pole, tekst3)
def ustaw_niebieskie():
    tekst3.configure(fg='blue', text=pole.get())

def ustaw_czerwone():
    tekst3.configure(fg='red', text=pole2.get())

# akcje obługi zdarzeń można podpiąć do guzików także później, już po ich utworzeniu:
guzikBlue.configure(command=ustaw_niebieskie)
guzikRed.configure(command=ustaw_czerwone)

root.mainloop()
