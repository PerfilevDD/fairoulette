from tkinter import *
from tkinter import ttk



import requests
url = "http://localhost:8000"
def make_bet_digit(number):
    user_id = "2"
    type = "number"
    value = str(number)
    try:
        amount = float(feet.get())
        print(float(feet.get()))
    except:
        amount = 0.0
        print('f')
    print(number)
    try:
        r = requests.post(f"{url}/make_bet/", json = {'user_id': user_id, "type": type, 'value': value, 'amount': amount})
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        pass
    

root = Tk()
root.title("Fairoulette")

mainframe = ttk.Frame(root, padding="5 5 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
print(feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

#meters = StringVar()
#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

f_row = [3,6,9,12,15,18,21,24,28,31,34,37]
s_row = [2,5,8,11,14,17,20,23,27,30,33,36]
th_row = [1,4,7,10,13,16,19,22,26,29,32,35]
rows = [f_row, s_row, th_row]
row_numbers = 0
for row in rows:
    row_numbers = row_numbers + 1
    for i in row:
            ttk.Button(mainframe, text=f"{i}", command=lambda i=i: make_bet_digit(i)).grid(column=i+row_numbers+10, row=row_numbers+10, sticky=W)
    


#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()

root.mainloop()