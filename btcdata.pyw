from tkinter import *
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook
import requests
import json

amount = 0.0001273

#btc price
def btcvalue():
    response = requests.get('https://api.coinbase.com/v2/prices/BTC-COP/spot')
    value = response.json()["data"]["amount"]
    return value

price = btcvalue()
d9 = amount * float(price) / 1
# print(f"currency: Bitcoin; Price: {price}; your bitcoin is worth: {d9} ")

d9_int = int(d9)
price_float = float(price)
price_int = int(price_float)

def show_data():
    lb2 = Label(window, text = "Bitcoin is currently: ", fg = '#4d4d4d', font=("Helvetica", 16))
    lb2.grid(row=3, column=2)
    lb = Label(window, text = f"COP {price_int}", fg = '#329239', font=("Helvetica", 16))
    lb.grid(row=4, column=2)
    lb3 = Label(window, text = "You currently have: ", fg = '#4d4d4d', font=("Helvetica", 16))
    lb3.grid(row=5, column=2)
    lb7 = Label(window, text = f"COP {d9_int}", fg = '#329239', font=("Helvetica", 16))
    lb7.grid(row=6, column=2)

window=Tk()

window.title('btcdata')
window.geometry("250x400")
window.resizable(False,False)

btn_img = PhotoImage(file='../9dbtc/img/btc.png')
btn = Button(window, text = "Bitcoin rn.", image = btn_img, command = show_data, borderwidth=0)
btn.grid(row=2, column=2)
lbl = Label(window, text = "BITCOIN", fg = '#f7931a', font=("Helvetica", 16))
lbl.place(x=160, y=10)
lbl.grid(row=1, column=2)
window.mainloop()
