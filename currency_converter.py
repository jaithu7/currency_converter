import requests
import tkinter as tk
from tkinter import ttk

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get().upper()
        to_curr = to_currency.get().upper()

        # Fetch exchange rate
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_curr}&to={to_curr}"
        response = requests.get(url)
        data = response.json()

        converted_amount = data['rates'][to_curr]
        result_label.config(text=f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}", fg="green")
    except:
        result_label.config(text="Error: Invalid input or API issue!", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Advanced Currency Converter")
root.geometry("400x300")

# Inputs
tk.Label(root, text="Amount:", font=("Arial", 12)).pack(pady=5)
amount_entry = tk.Entry(root, font=("Arial", 12))
amount_entry.pack()

# Supported Currencies (20+ countries)
currencies = [
    "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", 
    "SEK", "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", "TRY", 
    "INR", "BRL", "ZAR", "RUB", "DKK", "PLN", "THB", "IDR"
]

tk.Label(root, text="From Currency:", font=("Arial", 12)).pack(pady=5)
from_currency = ttk.Combobox(root, values=currencies, font=("Arial", 12))
from_currency.pack()

tk.Label(root, text="To Currency:", font=("Arial", 12)).pack(pady=5)
to_currency = ttk.Combobox(root, values=currencies, font=("Arial", 12))
to_currency.pack()

# Convert Button
convert_button = tk.Button(
    root, 
    text="Convert", 
    command=convert_currency,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white"
)
convert_button.pack(pady=15)

# Result
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

root.mainloop()
