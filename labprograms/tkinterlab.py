import tkinter as tk
window = tk.Tk()
window.geometry('200x200')
lbl = tk.Label(window, text = "PARKING FAIR CALCULATOR")
lbl2 = tk.Label(window, text = "SELECT THE VEHICLE")
radio = tk.IntVar()

def bike():
    hrs1 = int(input("How many Hours?"))
    pay = print("take this much",hrs*100)

def car():
    hrs1 = int(input("How many Hours?"))
    pay = print("take this much",hrs*100)
    
    
    
r1 = tk.Radiobutton(window, text="BIKE", variable=radio,
                    value=0, command=bike).pack()
r2 = tk.Radiobutton(window, text="CAR", variable=radio,
                    value=1, command=car).pack()			

lbl.pack()
lbl2.pack()



window.mainloop()
