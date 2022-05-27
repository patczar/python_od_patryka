import tkinter as tk

def akcja():
    dystans = float(entry_dystans.get())
    spalanie = float(entry_spalanie.get())
    cena = float(entry_cena.get())
    kwota = dystans * spalanie * cena / 100
    lbl_wynik.configure(text='%.2f' % kwota)


FONT_LBL = ('Arial', 24, 'normal')
FONT_TXT = ('Consolas', 26, 'bold')
FONT_BTN = ('Arial', 26, 'bold')
FONT_RES = ('Arial', 30, 'bold')

root = tk.Tk()
root.geometry('480x640')

lbl_cena = tk.Label(master=root, text='Cena:', font=FONT_LBL)
lbl_cena.pack()
entry_cena = tk.Entry(master=root, font=FONT_TXT)
entry_cena.pack()

lbl_spalanie = tk.Label(master=root, text='Spalanie:', font=FONT_LBL)
lbl_spalanie.pack()
entry_spalanie = tk.Entry(master=root, font=FONT_TXT)
entry_spalanie.pack()

lbl_dystans = tk.Label(master=root, text='Dystans:', font=FONT_LBL)
lbl_dystans.pack()
entry_dystans = tk.Entry(master=root, font=FONT_TXT)
entry_dystans.pack()

button = tk.Button(master=root, text='Oblicz', font=FONT_BTN, command=akcja)  # ,command=....
button.pack()

lbl_wynik = tk.Label(master=root, text='0.00', font=FONT_RES, fg='blue')
lbl_wynik.pack()

root.title('Kalkulator kosztów podróży')
root.mainloop()
