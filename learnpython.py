import tkinter as tk

def update(*args):
    
    header.config(text=comm.get())

window = tk.Tk()

window.geometry("800x500")
window.title("Test stand controll dashboard")

header = tk.Label(window, text="Rocket Link", font=('Arial',18))
header.pack(pady=(0,20))

toolbar = tk.Frame(window)
toolbar.pack(padx=20,pady=20)

comm = tk.StringVar()
comm.set("port")
commselect = tk.OptionMenu(toolbar, comm, "comm1", "comm2", "comm3",)
commselect.config(font=('Arial',12))
commselect.pack(side="left",)
comm.trace("w",update)

connect = tk.Button(toolbar, text="conect", font=('Arial',12))
connect.pack(side="left")

commandline = tk.Entry(toolbar, font=('Arial',15), width=30)
commandline.pack(side='left',padx=5)

button = tk.Button(toolbar, text="Send", font=('Arial',12))
button.pack(side="left")

textbox = tk.Text(window, width=55, height=35, font=('Arial',12))
textbox.pack()

window.mainloop()

