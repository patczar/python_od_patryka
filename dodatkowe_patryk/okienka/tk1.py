import tkinter as tk
# nazwę tego modułu często się skraca przy imporcie

print('Początek programu')

# Utworzenie obiektu "całe okno" - korzeń całej struktury komponentów
root = tk.Tk()

# Utworzenie komponentu typu Label, który "należy do" okna
label1 = tk.Label(master=root, text='Pierwszy napis')
# Dodanie do okna - komponent staje się widoczny
label1.pack()

# Jeśli potrzebuję późniejszego dostępu do tego komponentu, to zapisuję go na zmienną.
label2 = tk.Label(master=root, text='Drugi napis')
label2.pack()

# A jeśli dalszy los komponentu mnie nie interesuje, to mogę tak, bez zapisywanie na zmienną...
tk.Label(master=root, text='Trzeci napis').pack()

button1 = tk.Button(master=root, text="Klik Klik")
button1.pack()

button2 = tk.Button(master=root, text="Guzik 2")
button2.pack()

print('Zaraz wyświetlę okno')

# Wyświetlenie okna. Od tej pory aplikacja działa na zasadzie zasadzie obsługi zdarzeń.
root.mainloop()

print('Koniec programu')
