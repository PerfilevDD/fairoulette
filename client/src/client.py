from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

from PIL import Image, ImageTk
url = "http://localhost:8000"

# Global
balance = 0.0        # Hält das aktuelle Guthaben des Spielers 
user_id = 0          # Speichert die ID des aktuellen Benutzers 
random = 0           # Speichert eine zufällige Zahl "das letzte Ergebnis des Roulettrads"
table_id = 0         # Tisch-ID

def check_user(name):
    try:
        r = requests.get(f"{url}/users/{name}")
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException:
        return None     # Bei einem Fehler wird "None" zurückgegeben


def register_user():     # wird aufgerufen, wenn sich ein Benutzer angemeldet hat bzw. anmeldet
    global balance
    global user_id
    name = entry_name.get()
    if not name:         # Überprüft, ob der Name eingegeben wurde, und registriert den Benutzer über das Backend, wenn er noch nicht existiert.
        messagebox.showwarning("", "Wir sollen deinen Namen wissen, looser")
        return
    
    user_data = check_user(name)
    print(user_data)
    if user_data:
        # User exists
        user_id = user_data['id']
        balance = user_data['balance']
        messagebox.showinfo("", f"{name} bist du bereit zu verlieren (wieder)?")
        login_window.destroy()
        open_table_window()
    else:
        try:
            r = requests.post(f"{url}/users/", json={'name': name})
            r.raise_for_status()
            print(r.json())
            messagebox.showinfo("", f"Willkommen, {name}, in the best Fairoulette in the world")
            
            # Daten for local
            balance = 100.0
            user_id = r.json()['id']
            
            login_window.destroy()
            open_table_window()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("", f"No Internet")


# Make a bet with a number          # Spiellogik
def make_bet_digit(number, feet):   # Ermöglicht es dem Spieler, auf eine spezifische Zahl zu wetten
    global balance, user_id, table_id
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
    
    
    if amount > balance:    # Überprüft, ob das Wettgeld im erlaubten Rahmen des aktuellen Guthabens liegt.
        messagebox.showwarning("", "Du hast kein Geld mehr\n\n Guthaben aufladen?\n\n Paypal: @perf007\n Text: nickname + Betrag (Optional)")
    elif (amount < 0) and (str(user_id) != '777'):
        messagebox.showwarning("", "are u hacker?")
    elif amount == 0:
        messagebox.showwarning("", "ZERO?")
    else:
        try:
            r = requests.post(f"{url}/bet", json = {'user_id': str(user_id), "table_id": table_id, "type": type, 'value': value, 'amount': amount})
            r.raise_for_status()
            balance -= amount # minus money
            update_balance_label()
            update_random_label()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("", f"No Internet")
            pass
    
def open_login_window():    #Erstellt ein Anmeldefenster, in dem der Benutzer seinen Namen eingeben und sich authentifizieren kann. 
    global login_window, entry_name
    login_window = Tk()
    login_window.title("Reg")

    label_name = Label(login_window, text="Name:")
    label_name.grid(row=0, column=0, padx=20, pady=5)

    entry_name = Entry(login_window)
    entry_name.grid(row=0, column=1, padx=20, pady=5)

    button_register = Button(login_window, text="Auth", command=register_user)
    button_register.grid(row=1, columnspan=2, pady=20)

    login_window.mainloop()
    
def update_balance_label():
    balance_label.config(text=f"Balance: {str(balance)}")
    
    
def update_random_label():
    try:
        r = requests.get(f"{url}/get_result/{table_id}")
        r.raise_for_status()
        random = r.json()['result']
        random_label.config(text=f"Random: {str(random)}")
            
    except requests.exceptions.RequestException as e:
        messagebox.showerror("", f"{e}")
    
def open_table_window(): 
    global table_windows
    table_windows = Tk()
    table_windows.title("Choose Table")
    
    #choose_table()
    

    label_table = Label(table_windows, text="Tables")
    label_table.grid(row=0, column=0, padx=20, pady=5)


    button_update = Button(table_windows, text="update", command=update_tables)
    button_update.grid(row=0, columnspan=2, pady=20)

    table_windows.mainloop()

def choose_table(table):
    global table_id, table_windows
    table_id = table  
    
    table_windows.destroy()
    open_game_window() 
    
def update_tables():
    global table_id
    
    try:
        r = requests.get(f"{url}/tables")
        r.raise_for_status()
        tables_arr = r.json()['tables']
        for table in tables_arr:
            label_table_choose = Label(table_windows, text="          ")
            label_table_choose.grid(row=4, column=table, padx=20, pady=5)
            
            Button(table_windows, text=f"Table {table}", command=lambda table=table: choose_table(table)).grid(row=6, columnspan=table, sticky=(S, E))
         
            
        
        
        #login_window.destroy()
        #open_game_window()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("", f"No Internet")
    

    
def open_game_window():       # Erstellt das Hauptfenster des Spiels, in dem der Benutzer Wetten platzieren kann.
                              # Initialisiert Schaltflächen für jede Zahl auf dem Rouletterad und färbt diese entsprechend der Zugehörigkeit zur Kategorie "Schwarz" oder "Rot".
    global root, balance_label, random, random_label, black
    # Main window
    root = Tk()
    root.title("Fairoulette")

    # Window settings
    mainframe = ttk.Frame(root, padding="50 50 50 50")
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    
    # Entrys 
    
    Entrys = ttk.Frame(mainframe)
    Entrys.grid(row = 1, column = 0)
    Entrys.grid_columnconfigure((0,1), weight = 1)
    Entrys.grid_rowconfigure(0, weight = 1)
    
    
    Wert_label = ttk.Label(mainframe, text=f"Wert:")
    Wert_label.grid(column=1, row=0, sticky=('NW'))
    Wert_label.config(font=("Courier", 20))
    
    feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
    feet_entry.grid(column=1, row=0, sticky=(''))
    feet_entry.config(font=("Courier", 20))
    
    
    # Images
               
    wheel_path = Image.open("../assets/data/fairoulette/wheel.png")
    wheel = ImageTk.PhotoImage(wheel_path) 
    
     
    # Labels 
     
    wheel_label = ttk.Label(Entrys, image=wheel)
    wheel_label.grid(column=0, row=5)
    
    random_label = ttk.Label(Entrys, text=f"{str(random)}")
    random_label.config(font=("Courier", 64), width=1)
    random_label.grid(column=0, row=5)
    
    
    empty_label = ttk.Label(Entrys, text=f" ")
    empty_label.grid(column=0, row=6)
    empty_label.config(font=("Courier", 36))


    balance_label = ttk.Label(Entrys, text=f"Balance: {str(balance)}")
    balance_label.grid(column=0, row=7)
    balance_label.config(font=("Courier", 20))
    
    
    empty_label = ttk.Label(Entrys, text=f" ")
    empty_label.grid(column=0, row=8)
    empty_label.config(font=("Courier", 55))
    
    table_label = ttk.Label(Entrys, text=f"Table: {str(table_id)}")
    table_label.grid(column=0, row=9)
    table_label.config(font=("Courier", 12))





    # Gameboard
    frame_all_buttons= ttk.Frame(mainframe)
    frame_all_buttons.grid(row = 1, column = 1, sticky=('N'))
    frame_all_buttons.grid_columnconfigure((0,1), weight = 1)
    frame_all_buttons.grid_rowconfigure(0, weight = 1)
    
    empty_label = ttk.Label(frame_all_buttons, text=f" ")
    empty_label.grid(column=0, row=0)
    empty_label.config(font=("Courier", 40))
    
    # Green
    frame_buttons = ttk.Frame(frame_all_buttons)
    frame_buttons.grid(row = 1, column = 1)
    frame_buttons.grid_columnconfigure((0,1), weight = 1)
    frame_buttons.grid_rowconfigure(0, weight = 1)
    
    Button(frame_buttons, text=f"{0}", command=lambda i=0: make_bet_digit(i, feet), width=4, height=7,bg="green", fg="white").grid(column=0, row=0)
    
    
    # Numbers
    
    frame_buttons = ttk.Frame(frame_all_buttons)
    frame_buttons.grid(row = 1, column = 2)
    frame_buttons.grid_columnconfigure((0,1), weight = 1)
    frame_buttons.grid_rowconfigure(0, weight = 1)
    
    black = [2,4,6,8,10,11,13,15,17,20,22,24,27,29,30,32,34,36]
    f_row = [3,6,9,12,15,18,21,24,28,31,34,37]
    s_row = [2,5,8,11,14,17,20,23,27,30,33,36]
    th_row = [1,4,7,10,13,16,19,22,26,29,32,35]
    
    rows = [f_row, s_row, th_row]
    row_numbers = 0
    column_numbers = 0
    
    for row in rows:
        for i in row:
                color = is_black(i)
                if column_numbers < 12:
                    Button(frame_buttons, text=f"{i}", command=lambda i=i: make_bet_digit(i, feet), width=4, height=2,bg=color, fg="white").grid(column=column_numbers, row=row_numbers)
                    column_numbers += 1
                else:
                    column_numbers = 0
                    Button(frame_buttons, text=f"{i}", command=lambda i=i: make_bet_digit(i, feet), width=4, height=2,bg=color, fg="white").grid(column=column_numbers, row=row_numbers)
                    column_numbers += 1
                    
        row_numbers = row_numbers + 1
    
    # 12 Buttons
    
    frame_buttons = ttk.Frame(frame_all_buttons)
    frame_buttons.grid(row = 4, column = 2)
    frame_buttons.grid_columnconfigure((0,1), weight = 1)
    frame_buttons.grid_rowconfigure(0, weight = 1)
    
    
    Button(frame_buttons, text=f"1 st 12", command=lambda i=0: make_bet_digit(i, feet), width=23, height=2,bg="darkblue", fg="white").grid(column=0, row=0)
    Button(frame_buttons, text=f"2 nd 12", command=lambda i=0: make_bet_digit(i, feet), width=22, height=2,bg="darkblue", fg="white").grid(column=1, row=0)
    Button(frame_buttons, text=f"3 rd 12", command=lambda i=0: make_bet_digit(i, feet), width=23, height=2,bg="darkblue", fg="white").grid(column=2, row=0)
    
    # 3 Buttons
    
    frame_buttons = ttk.Frame(frame_all_buttons)
    frame_buttons.grid(row = 1, column = 14)
    frame_buttons.grid_columnconfigure((0,1), weight = 1)
    frame_buttons.grid_rowconfigure(0, weight = 1)
    
    
    Button(frame_buttons, text=f"2 to 1", command=lambda i=0: make_bet_digit(i, feet), width=15, height=2,bg="darkblue", fg="white").grid(column=0, row=0)
    Button(frame_buttons, text=f"2 to 1", command=lambda i=0: make_bet_digit(i, feet), width=15, height=2,bg="darkblue", fg="white").grid(column=0, row=1)
    Button(frame_buttons, text=f"2 to 1", command=lambda i=0: make_bet_digit(i, feet), width=15, height=2,bg="darkblue", fg="white").grid(column=0, row=2)
    

    feet_entry.focus()

    root.mainloop()
    
    

def is_black(i):       #Hilfsfunktion, die bestimmt, ob eine Zahl schwarz ist, basierend auf einer vorgegebenen Liste von schwarzen Zahlen.
    if i in black:
        return 'black'
    else:
        return "#8B0000"
    
open_game_window()
#open_login_window()

#open_table_window()