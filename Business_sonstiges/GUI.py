import tkinter as tk
from tkinter import ttk

def funktion_zeitreihe():
    print('Hier Funktion Zeitreihe')

def funktion_Modell_berechnen():
    print('Hier Funktion Modell berechnen')

root = tk.Tk()
root.geometry('400x400')

Label1 = tk.Label(root, text = 'Einlagenmodell Business')
Label1.pack(side = 'top') # top, bottom, right, y fill und expand ebenfalls möglich

button1 = ttk.Button(root, text = 'Zeitreihe hochladen', padding = 10, command=funktion_zeitreihe)
button1.place(x=10, y=330)

button2 = ttk.Button(root, text = 'Modell rechnen', padding = 10, command=funktion_Modell_berechnen)
button2.place(x=165, y=330)

quit_button = ttk.Button(root, text = 'Abbruch', padding = 10, command=root.destroy)
quit_button.place(x=300, y=330)

#for item in button1.keys():
   # print(item, ':', button1[item])
root.mainloop()


