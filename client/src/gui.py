from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
url = "http://localhost:8000"

# Global
balance = 0.0
user_id = 0

def check_user(name):
    try:
        r = requests.get(f"{url}/users/{name}")
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException:
        return None


def register_user():
    global balance
    global user_id
    name = entry_name.get()
    if not name:
        messagebox.showwarning("name blyat")
        return
    
    user_data = check_user(name)
    print(user_data)
    if user_data:
        # User exists
        user_id = user_data['id']
        balance = user_data['balance']
        messagebox.showinfo(f"{name} vietnam!!1")
        login_window.destroy()
        open_game_window()
    else:
        try:
            r = requests.post(f"{url}/users/", json={'name': name})
            r.raise_for_status()
            print(r.json())
            messagebox.showinfo("f {name} yesss")
            
            # Daten for local
            balance = 100.0
            user_id = r.json()['id']
            
            login_window.destroy() 
            open_game_window()
        except requests.exceptions.RequestException as e:
            messagebox.showerror(f"{e}")
            
            # Delete this late blyat (for debbuging)
            login_window.destroy() 
            open_game_window()


# Make a bet with a number
def make_bet_digit(number, feet):
    global balance, user_id
    print(user_id)
    
    type = "number"
    value = str(number)
    
    # if amount not digit
    try:
        amount = float(feet.get())
            
        print(float(feet.get()))
    except:
        amount = 0.0
        print('f')
    print(number)
    
    
    if amount > balance:
        messagebox.showwarning("u haven't enouht money blyat")
    elif (amount < 0) and (str(user_id) != '777'):
        messagebox.showwarning("are u hacker blyat?")
    elif amount == 0:
        messagebox.showwarning("ZERO?")
    else:
        try:
            r = requests.post(f"{url}/make_bet/", json = {'user_id': str(user_id), "type": type, 'value': value, 'amount': amount})
            r.raise_for_status()
            balance = balance - amount # minus money
            print(balance)
            update_balance_label()
        except requests.exceptions.RequestException as e:
            pass
    
def open_login_window():
    global login_window, entry_name
    login_window = Tk()
    login_window.title("Reg")

    label_name = Label(login_window, text="Name:")
    label_name.grid(row=0, column=0, padx=20, pady=5)

    entry_name = Entry(login_window)
    entry_name.grid(row=0, column=1, padx=20, pady=5)

    button_register = Button(login_window, text="reg", command=register_user)
    button_register.grid(row=1, columnspan=2, pady=20)

    login_window.mainloop()
    
def update_balance_label():
    balance_label.config(text=str(balance))

    
def open_game_window():
    global root, balance_label
    # Main window
    root = Tk()
    root.title("Fairoulette")

    # Window settings
    mainframe = ttk.Frame(root, padding="5 5 15 15")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Entry a bet
    feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(W, E))

    #meters = StringVar()
    #ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

    # Gameboard
    f_row = [3,6,9,12,15,18,21,24,28,31,34,37]
    s_row = [2,5,8,11,14,17,20,23,27,30,33,36]
    th_row = [1,4,7,10,13,16,19,22,26,29,32,35]
    rows = [f_row, s_row, th_row]
    row_numbers = 0
    for row in rows:
        row_numbers = row_numbers + 1
        for i in row:
                ttk.Button(mainframe, text=f"{i}", command=lambda i=i: make_bet_digit(i, feet)).grid(column=i+row_numbers+10, row=row_numbers+10, sticky=W)
        

    balance_label = ttk.Label(mainframe, text=str(balance))
    balance_label.grid(column=2, row=2, sticky=W)
    #ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    #ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

    #for child in mainframe.winfo_children(): 
    #   child.grid_configure(padx=5, pady=5)

    feet_entry.focus()

    root.mainloop()
    
#open_game_window()
open_login_window()