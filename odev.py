import sqlite3
import tkinter as tk
from tkinter import messagebox
import requests
import time
import datetime
from statistics import mean
import matplotlib.pyplot as plt

api_key = "3c3cbe4c167f3f72fb75ff4332285eeb"
url_live = f"http://api.currencylayer.com/live?access_key={api_key}&source=TRY"

live = requests.get(url_live).json()

table = {'AED': 'United Arab Emirates Dirham', 'AFN': 'Afghan Afghani', 'ALL': 'Albanian Lek', 'AMD': 'Armenian Dram', 'ANG': 'Netherlands Antillean Guilder', 'AOA': 'Angolan Kwanza', 'ARS': 'Argentine Peso', 'AUD': 'Australian Dollar', 'AWG': 'Aruban Florin', 'AZN': 'Azerbaijani Manat', 'BAM': 'Bosnia-Herzegovina Convertible Mark', 'BBD': 'Barbadian Dollar', 'BDT': 'Bangladeshi Taka', 'BGN': 'Bulgarian Lev', 'BHD': 'Bahraini Dinar', 'BIF': 'Burundian Franc', 'BMD': 'Bermudan Dollar', 'BND': 'Brunei Dollar', 'BOB': 'Bolivian Boliviano', 'BRL': 'Brazilian Real', 'BSD': 'Bahamian Dollar', 'BTC': 'Bitcoin', 'BTN': 'Bhutanese Ngultrum', 'BWP': 'Botswanan Pula', 'BYN': 'New Belarusian Ruble', 'BYR': 'Belarusian Ruble', 'BZD': 'Belize Dollar', 'CAD': 'Canadian Dollar', 'CDF': 'Congolese Franc', 'CHF': 'Swiss Franc', 'CLF': 'Chilean Unit of Account (UF)', 'CLP': 'Chilean Peso', 'CNY': 'Chinese Yuan', 'CNH': 'Chinese Yuan Offshore', 'COP': 'Colombian Peso', 'CRC': 'Costa Rican Colón', 'CUC': 'Cuban Convertible Peso', 'CUP': 'Cuban Peso', 'CVE': 'Cape Verdean Escudo', 'CZK': 'Czech Republic Koruna', 'DJF': 'Djiboutian Franc', 'DKK': 'Danish Krone', 'DOP': 'Dominican Peso', 'DZD': 'Algerian Dinar', 'EGP': 'Egyptian Pound', 'ERN': 'Eritrean Nakfa', 'ETB': 'Ethiopian Birr', 'EUR': 'Euro', 'FJD': 'Fijian Dollar', 'FKP': 'Falkland Islands Pound', 'GBP': 'British Pound Sterling', 'GEL': 'Georgian Lari', 'GGP': 'Guernsey Pound', 'GHS': 'Ghanaian Cedi', 'GIP': 'Gibraltar Pound', 'GMD': 'Gambian Dalasi', 'GNF': 'Guinean Franc', 'GTQ': 'Guatemalan Quetzal', 'GYD': 'Guyanaese Dollar', 'HKD': 'Hong Kong Dollar', 'HNL': 'Honduran Lempira', 'HRK': 'Croatian Kuna', 'HTG': 'Haitian Gourde', 'HUF': 'Hungarian Forint', 'IDR': 'Indonesian Rupiah', 'ILS': 'Israeli New Sheqel', 'IMP': 'Manx pound', 'INR': 'Indian Rupee', 'IQD': 'Iraqi Dinar', 'IRR': 'Iranian Rial', 'ISK': 'Icelandic Króna', 'JEP': 'Jersey Pound', 'JMD': 'Jamaican Dollar', 'JOD': 'Jordanian Dinar', 'JPY': 'Japanese Yen', 'KES': 'Kenyan Shilling', 'KGS': 'Kyrgystani Som', 'KHR': 'Cambodian Riel', 'KMF': 'Comorian Franc', 'KPW': 'North Korean Won', 'KRW': 'South Korean Won', 'KWD': 'Kuwaiti Dinar', 'KYD': 'Cayman Islands Dollar', 'KZT': 'Kazakhstani Tenge', 'LAK': 'Laotian Kip', 'LBP': 'Lebanese Pound', 'LKR': 'Sri Lankan Rupee', 'LRD': 'Liberian Dollar', 'LSL': 'Lesotho Loti', 'LTL': 'Lithuanian Litas', 'LVL': 'Latvian Lats', 'LYD': 'Libyan Dinar', 'MAD': 'Moroccan Dirham', 'MDL': 'Moldovan Leu', 'MGA': 'Malagasy Ariary', 'MKD': 'Macedonian Denar', 'MMK': 'Myanma Kyat', 'MNT': 'Mongolian Tugrik', 'MOP': 'Macanese Pataca', 'MRU': 'Mauritanian Ouguiya', 'MUR': 'Mauritian Rupee', 'MVR': 'Maldivian Rufiyaa', 'MWK': 'Malawian Kwacha', 'MXN': 'Mexican Peso', 'MYR': 'Malaysian Ringgit', 'MZN': 'Mozambican Metical', 'NAD': 'Namibian Dollar', 'NGN': 'Nigerian Naira', 'NIO': 'Nicaraguan Córdoba', 'NOK': 'Norwegian Krone', 'NPR': 'Nepalese Rupee', 'NZD': 'New Zealand Dollar', 'OMR': 'Omani Rial', 'PAB': 'Panamanian Balboa', 'PEN': 'Peruvian Nuevo Sol', 'PGK': 'Papua New Guinean Kina', 'PHP': 'Philippine Peso', 'PKR': 'Pakistani Rupee', 'PLN': 'Polish Zloty', 'PYG': 'Paraguayan Guarani', 'QAR': 'Qatari Rial', 'RON': 'Romanian Leu', 'RSD': 'Serbian Dinar', 'RUB': 'Russian Ruble', 'RWF': 'Rwandan Franc', 'SAR': 'Saudi Riyal', 'SBD': 'Solomon Islands Dollar', 'SCR': 'Seychellois Rupee', 'SDG': 'South Sudanese Pound', 'SEK': 'Swedish Krona', 'SGD': 'Singapore Dollar', 'SHP': 'Saint Helena Pound', 'SLE': 'Sierra Leonean Leone', 'SLL': 'Sierra Leonean Leone', 'SOS': 'Somali Shilling', 'SRD': 'Surinamese Dollar', 'STD': 'São Tomé and Príncipe Dobra', 'SVC': 'Salvadoran Colón', 'SYP': 'Syrian Pound', 'SZL': 'Swazi Lilangeni', 'THB': 'Thai Baht', 'TJS': 'Tajikistani Somoni', 'TMT': 'Turkmenistani Manat', 'TND': 'Tunisian Dinar', 'TOP': 'Tongan Paʻanga', 'TRY': 'Turkish Lira', 'TTD': 'Trinidad and Tobago Dollar', 'TWD': 'New Taiwan Dollar', 'TZS': 'Tanzanian Shilling', 'UAH': 'Ukrainian Hryvnia', 'UGX': 'Ugandan Shilling', 'USD': 'United States Dollar', 'UYU': 'Uruguayan Peso', 'UZS': 'Uzbekistan Som', 'VEF': 'Venezuelan Bolívar Fuerte', 'VES': 'Sovereign Bolivar', 'VND': 'Vietnamese Dong', 'VUV': 'Vanuatu Vatu', 'WST': 'Samoan Tala', 'XAF': 'CFA Franc BEAC', 'XAG': 'Silver (troy ounce)', 'XAU': 'Gold (troy ounce)', 'XCD': 'East Caribbean Dollar', 'XDR': 'Special Drawing Rights', 'XOF': 'CFA Franc BCEAO', 'XPF': 'CFP Franc', 'YER': 'Yemeni Rial', 'ZAR': 'South African Rand', 'ZMK': 'Zambian Kwacha (pre-2013)', 'ZMW': 'Zambian Kwacha', 'ZWL': 'Zimbabwean Dollar'}

connection = sqlite3.connect("database.db", isolation_level=None)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS myAssets (code, name, amount, rate, date)")
cursor.execute("CREATE TABLE IF NOT EXISTS log (code, name, rate, date)")

def get_historical(date):
	url_historical = f"http://api.currencylayer.com/historical?access_key={api_key}&date={date.strftime('%Y-%m-%d')}&source=TRY"
	response = requests.get(url_historical).json()  
	time.sleep(1)
	return response

def get_date(epoch):
	return time.strftime('%Y-%m-%d', time.localtime(epoch))

def percentage(part, whole):
	percentage = 100 * float(part)/float(whole)
	return percentage - 100

cursor.execute("SELECT * FROM log WHERE date = ?", (get_date(live["timestamp"]),))
if cursor.fetchone():
	pass
else:
	for key in live["quotes"].keys():
		cursor.execute("INSERT INTO log VALUES (?, ?, ?, ?)", (key[3:], table[key[3:]], live["quotes"][key], get_date(live["timestamp"])))

root = tk.Tk()
root.title("Döviz Uygulaması")

def varlık_ekle():
	ekleme_penceresi = tk.Toplevel(root)
	ekleme_penceresi.title("Varlık Ekle")

	lb_varlıklar = tk.Listbox(ekleme_penceresi, width=42, selectmode=tk.SINGLE)
	miktar_label = tk.Label(ekleme_penceresi, text="Miktar:")
	miktar_entry = tk.Entry(ekleme_penceresi)

	def db_ekle():
		code = lb_varlıklar.get(lb_varlıklar.curselection()).split(" - ")[0]
		name = lb_varlıklar.get(lb_varlıklar.curselection()).split(" - ")[1]
		amount = float(miktar_entry.get().replace(",", "."))
		rate = live["quotes"]["TRY" + code]
		date = live["timestamp"]

		cursor.execute("SELECT * FROM myAssets WHERE code = ?", (code,))
		foo = cursor.fetchall()
		pre_amount = 0
		kar_zarar = 0
		güncel_kur = float(live["quotes"]["TRY" + code])
		for i in foo:
			pre_amount += float(i[2])
			tarihi_kur = float(i[3])
		if foo:
			sum_amount = float(amount) + pre_amount
			kar_zarar += (float(güncel_kur) - tarihi_kur) * sum_amount
			cursor.execute("INSERT INTO myAssets VALUES (?, ?, ?, ?, ?)", (code, name, amount, rate, date))
			messagebox.showinfo("Başarılı", "Varlık Güncellendi.")
			data = (code, name, sum_amount, rate, sum_amount * float(live['quotes']['TRY' + code]), kar_zarar, percentage(güncel_kur, tarihi_kur))
			data_format = "{:<10} {:<30} {:<15} {:<15} {:<25} {:<20} {:<20}"
			
			for i in lb_toplam.get(0, tk.END):
				if code in i:
					lb_toplam.delete(lb_toplam.get(0, tk.END).index(i))
			
			lb_toplam.insert(tk.END, data_format.format(*data))
		else:
			cursor.execute("INSERT INTO myAssets VALUES (?, ?, ?, ?, ?)", (code, name, amount, rate, date))
			messagebox.showinfo("Başarılı", "Varlık eklendi.")

			data = (code, name, amount, rate, amount * float(live['quotes']['TRY' + code]), 0.0, 0.0)
			data_format = "{:<10} {:<30} {:<15} {:<15} {:<25} {:<20} {:<20}"
			lb_toplam.insert(tk.END, data_format.format(*data))

		ekleme_penceresi.destroy()

	button = tk.Button(ekleme_penceresi, text="Ekle", command=db_ekle)

	lb_varlıklar.pack(side=tk.LEFT, padx=5)
	miktar_label.pack(side=tk.LEFT, padx=5)
	miktar_entry.pack(side=tk.LEFT, padx=5)
	button.pack(side=tk.LEFT, padx=5)

	for key in table.keys():
		lb_varlıklar.insert(tk.END, key + " - " + table[key])

def eskiler():
	eski_pencere = tk.Toplevel(root)
	eski_pencere.title("Eski Bilgiler")

	lb_eskiler = tk.Listbox(eski_pencere, font=("Courier New", 10), width=72)
	cursor.execute("SELECT * FROM log")
	data = cursor.fetchall()
	data_format = "{:<10} {:<30} {:<15} {:<15}"
	for i in data:
		lb_eskiler.insert(tk.END, data_format.format(i[0], i[1], i[2], i[3]))
	lb_eskiler.pack()

	entry_label = tk.Label(eski_pencere, text="Kaç Günlük Veri Görüntülensin:")
	entry = tk.Entry(eski_pencere)
	entry_label.pack()
	entry.pack()

	def display_changes():
		try:
			date = entry.get()
		except ValueError:
			messagebox.showerror("Error", "Gün sayısı geçersiz")
			return

		selection = lb_eskiler.curselection()
		if selection:
			code = lb_eskiler.get(selection[0]).split()[0]
			current_date = datetime.datetime.now().date()
			entered_date = current_date - datetime.timedelta(days=int(date))
			while entered_date <= current_date:
				str_date = str(entered_date)
				if cursor.execute("SELECT * FROM log WHERE date = ?", (str_date,)).fetchone() is None:
					cursor.execute("INSERT INTO log (code, name, rate, date) VALUES (?, ?, ?, ?)", (code, table[code], get_historical(entered_date)['quotes']['TRY' + code], entered_date))
				entered_date += datetime.timedelta(days=1)

			currency = lb_eskiler.get(selection[0]).split()[0]
			cursor.execute("SELECT * FROM log WHERE code = ? ORDER BY date DESC LIMIT ?", (currency, date))
			data = cursor.fetchall()
			dates = []
			rates = []
			for row in data:
				dates.append(row[3])
				rates.append(row[2])
			
			plt.plot(dates[::-1], rates[::-1])
			plt.xlabel('Tarih')
			plt.ylabel('Kur')
			plt.title('Kur Değişimi')
			plt.show()
		else:
			messagebox.showinfo("Error", "Seçim yapmadınız.")

	btn_display = tk.Button(eski_pencere, text="Görüntüle", command=display_changes)
	btn_display.pack()

menubar = tk.Menu(root)
menubar.add_command(label="Varlık Ekle/Güncelle", command=varlık_ekle)
menubar.add_command(label="Eski Bİlgileri Görüntüle", command=eskiler)
#Varlıklarım
frame_varlıklar = tk.Frame(root)
lb_toplam = tk.Listbox(frame_varlıklar, font=("Courier New", 10), width=150)
lb_toplam.pack(side=tk.LEFT, padx=5)
frame_varlıklar.pack(side=tk.TOP, padx=5)
headers = ["Kod", "İsim", "Miktar", "Kur", "TRY Karşılığı", "Kar/Zarar", "Kar/Zarar Yüzdesi"]
header_format = "{:<10} {:<30} {:<15} {:<15} {:<30} {:<20} {:<20}"
lb_toplam.insert(0, header_format.format(*headers))

data_format = "{:<10} {:<30} {:<15} {:<15} {:<25} {:<20} {:<20}"

cursor.execute("SELECT DISTINCT code FROM myAssets")
unique_codes = cursor.fetchall()
toplam = 0
for code in unique_codes:
	cursor.execute("SELECT * FROM myAssets WHERE code = ?", (code[0],))
	data = cursor.fetchall()
	kar_zarar = 0
	toplam_miktar = 0
	yüzde = 0
	güncel_kur = float(live["quotes"]["TRY" + code[0]])
	for i in data:
		kod = i[0]
		isim = table[kod]
		miktar = float(i[2])
		toplam_miktar += miktar
		tarihi_kur = float(i[3])
		kar_zarar += (güncel_kur - tarihi_kur) * miktar
		yüzde += percentage(güncel_kur, tarihi_kur)
	lb_toplam.insert(tk.END, data_format.format(code[0], isim, toplam_miktar, güncel_kur, toplam_miktar * güncel_kur, round(kar_zarar, 2), round(yüzde, 2)))
	toplam += toplam_miktar * güncel_kur
lb_toplam.insert(1, data_format.format("Toplam", "", "", "", toplam, "", ""))

def display_graph():
    cursor.execute("SELECT date, SUM(amount * rate) as total_value FROM myAssets GROUP BY date ORDER BY date")
    data = cursor.fetchall()

    dates = [datetime.datetime.fromtimestamp(row[0]).strftime('%Y-%m-%d %H:%M:%S') for row in data]
    values = []
    sum_values = 0
    for row in data:
        sum_values += row[1]
        values.append(sum_values)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o', linestyle='-', color='b')
    plt.xlabel('Tarih')
    plt.ylabel('Değer')
    plt.title('Servet Değişimi')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

button = tk.Button(root, text="Servet Değişimini Görüntüle", command=display_graph)
button.pack(side=tk.TOP)

root.config(menu=menubar)
root.mainloop()