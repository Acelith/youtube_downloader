import tkinter as tk
#import functions.py 

def scaricaVideo():
    return ""

window = tk.Tk()
window.title("Scarica Video")

tk.Label(window, text="First Name").grid(row=0)
tk.Label(window, text="Last Name").grid(row=1)

e1 = tk.Entry(window)
e2 = tk.Entry(window)

scarica = tk.Button(
    text="Scarica video",
    width=25,
    height=5,
    bg="red",
    command=scaricaVideo(),
)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
scarica.grid(row=2, column=1)

#scarica.pack()

window.mainloop()

