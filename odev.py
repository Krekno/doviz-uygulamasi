import sqlite3
import tkinter as tk
from tkinter import messagebox
import http.client
import json
######################import sys

######################sys.stdout.reconfigure(encoding='utf-8')

# Establishing connection to API
conn_api = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 2vsoPDtAhSkflBmkScY8VQ:1opljQNWm5ZEHjUoIRB1wW"
}

# Establishing connection to SQLite database
conn_db = sqlite3.connect("varliklar.db", isolation_level=None)
cursor = conn_db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS varliklar (varlik_adi TEXT, varlik_kodu TEXT, miktar REAL, alis REAL, satis REAL, tarih TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS doviz_kurlari (varlik_adi TEXT, varlik_kodu TEXT, alis REAL, satis REAL, tarih TEXT)")

def get_exchange_rate():
    conn_api.request("GET", "/economy/allCurrency", headers=headers)
    res = conn_api.getresponse()
    data = res.read()
    return json.loads(data)

def get_gold_price():
    conn_api.request("GET", "/economy/goldPrice", headers=headers)
    res = conn_api.getresponse()
    data = res.read()
    return json.loads(data)

def add_asset():
    def get_buying_price(code):
        exchange_rates = get_exchange_rate()["result"]
        for varlik in exchange_rates:
            if varlik["code"] == code:
                return varlik["buying"]
        gold_prices = get_gold_price()["result"]
        for altin in gold_prices:
            if altin["name"] == code:
                return altin["buying"]
        return None

    def get_selling_price(code):
        exchange_rates = get_exchange_rate()["result"]
        for varlik in exchange_rates:
            if varlik["code"] == code:
                return varlik["selling"]
        gold_prices = get_gold_price()["result"]
        for altin in gold_prices:
            if altin["name"] == code:
                return altin["selling"]
        return None

    ekleme_ekrani = tk.Toplevel(root)
    ekleme_ekrani.title("Varlık Ekleme")

    lb_varliklar = tk.Listbox(ekleme_ekrani, height=15, width=50)
    lb_varliklar.pack(padx=10, pady=10, side=tk.LEFT)
    
    miktar_label = tk.Label(ekleme_ekrani, text="Miktar: ")
    miktar_label.pack(pady=10, side=tk.LEFT)

    miktar = tk.Entry(ekleme_ekrani)
    miktar.pack(pady=10, side=tk.LEFT)
    
    def add_asset_to_db():
        selected_varlik = lb_varliklar.get(tk.ACTIVE)
        miktar_value = miktar.get()

        if selected_varlik and miktar_value:
            varlik_info = selected_varlik.split(" - ")
            varlik_kodu = varlik_info[0]
            varlik_adi = varlik_info[1]
            cursor.execute(
                "INSERT INTO varliklar (varlik_adi, varlik_kodu, miktar, alis, satis, tarih) VALUES (?, ?, ?, ?, ?, DATE('now'))",
                (varlik_adi, varlik_kodu, miktar_value, get_buying_price(varlik_kodu), get_selling_price(varlik_kodu))
            )
            messagebox.showinfo("Başarılı", "Varlık eklendi.")
        else:
            messagebox.showwarning("Hata", "Lütfen bir varlık seçin ve miktarı girin.")
    
    button = tk.Button(ekleme_ekrani, text="Ekle", command=add_asset_to_db)
    button.pack(side=tk.LEFT, pady=1)

    exchange_rates = get_exchange_rate()["result"]
    for varlik in exchange_rates:
        lb_varliklar.insert(tk.END, f"{varlik['code']} - {varlik['name']} - Satış Fiyatı: {varlik['selling']} TRY")

    gold_prices = get_gold_price()["result"]
    for altin in gold_prices:
        lb_varliklar.insert(tk.END, f"{altin['name']} - Satış Fiyatı: {altin['sell']}")

root = tk.Tk()
root.title("Varlık Kayıtları")

menubar = tk.Menu(root)
root.config(menu=menubar)
menubar.add_command(label="Varlık Ekle", command=add_asset)

root.mainloop()
