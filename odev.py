import sqlite3
import tkinter as tk
from tkinter import messagebox
import requests

api_key = "69005d1fe73f2f98149fb531ef76816e"
url = f"http://api.currencylayer.com/live?access_key={api_key}&source=TRY"

response = requests.get(url)

table = {'AED': 'United Arab Emirates Dirham', 'AFN': 'Afghan Afghani', 'ALL': 'Albanian Lek', 'AMD': 'Armenian Dram', 'ANG': 'Netherlands Antillean Guilder', 'AOA': 'Angolan Kwanza', 'ARS': 'Argentine Peso', 'AUD': 'Australian Dollar', 'AWG': 'Aruban Florin', 'AZN': 'Azerbaijani Manat', 'BAM': 'Bosnia-Herzegovina Convertible Mark', 'BBD': 'Barbadian Dollar', 'BDT': 'Bangladeshi Taka', 'BGN': 'Bulgarian Lev', 'BHD': 'Bahraini Dinar', 'BIF': 'Burundian Franc', 'BMD': 'Bermudan Dollar', 'BND': 'Brunei Dollar', 'BOB': 'Bolivian Boliviano', 'BRL': 'Brazilian Real', 'BSD': 'Bahamian Dollar', 'BTC': 'Bitcoin', 'BTN': 'Bhutanese Ngultrum', 'BWP': 'Botswanan Pula', 'BYN': 'Belarusian Ruble', 'BYR': 'Belarusian Ruble', 'BZD': 'Belize Dollar', 'CAD': 'Canadian Dollar', 'CDF': 'Congolese Franc', 'CHF': 'Swiss Franc', 'CLF': 'Chilean Unit of Account (UF)', 'CLP': 'Chilean Peso', 'CNY': 'Chinese Yuan', 'COP': 'Colombian Peso', 'CRC': 'Costa Rican Colón', 'CUC': 'Cuban Convertible Peso', 'CUP': 'Cuban Peso', 'CVE': 'Cape Verdean Escudo', 'CZK': 'Czech Republic Koruna', 'DJF': 'Djiboutian Franc', 'DKK': 'Danish Krone', 'DOP': 'Dominican Peso', 'DZD': 'Algerian Dinar', 'EEK': 'Estonian Kroon', 'EGP': 'Egyptian Pound', 'ERN': 'Eritrean Nakfa', 'ETB': 'Ethiopian Birr', 'EUR': 'Euro', 'FJD': 'Fijian Dollar', 'FKP': 'Falkland Islands Pound', 'GBP': 'British Pound Sterling', 'GEL': 'Georgian Lari', 'GGP': 'Guernsey Pound', 'GHS': 'Ghanaian Cedi', 'GIP': 'Gibraltar Pound', 'GMD': 'Gambian Dalasi', 'GNF': 'Guinean Franc', 'GTQ': 'Guatemalan Quetzal', 'GYD': 'Guyanaese Dollar', 'HKD': 'Hong Kong Dollar', 'HNL': 'Honduran Lempira', 'HRK': 'Croatian Kuna', 'HTG': 'Haitian Gourde', 'HUF': 'Hungarian Forint', 'IDR': 'Indonesian Rupiah', 'ILS': 'Israeli New Sheqel', 'IMP': 'Manx pound', 'INR': 'Indian Rupee', 'IQD': 'Iraqi Dinar', 'IRR': 'Iranian Rial', 'ISK': 'Icelandic Króna', 'JEP': 'Jersey Pound', 'JMD': 'Jamaican Dollar', 'JOD': 'Jordanian Dinar', 'JPY': 'Japanese Yen', 'KES': 'Kenyan Shilling', 'KGS': 'Kyrgystani Som', 'KHR': 'Cambodian Riel', 'KMF': 'Comorian Franc', 'KPW': 'North Korean Won', 'KRW': 'South Korean Won', 'KWD': 'Kuwaiti Dinar', 'KYD': 'Cayman Islands Dollar', 'KZT': 'Kazakhstani Tenge', 'LAK': 'Laotian Kip', 'LBP': 'Lebanese Pound', 'LKR': 'Sri Lankan Rupee', 'LRD': 'Liberian Dollar', 'LSL': 'Lesotho Loti', 'LTL': 'Lithuanian Litas', 'LVL': 'Latvian Lats', 'LYD': 'Libyan Dinar', 'MAD': 'Moroccan Dirham', 'MDL': 'Moldovan Leu', 'MGA': 'Malagasy Ariary', 'MKD': 'Macedonian Denar', 'MMK': 'Myanma Kyat', 'MNT': 'Mongolian Tugrik', 'MOP': 'Macanese Pataca', 'MRO': 'Mauritanian Ouguiya', 'MUR': 'Mauritian Rupee', 'MVR': 'Maldivian Rufiyaa', 'MWK': 'Malawian Kwacha', 'MXN': 'Mexican Peso', 'MYR': 'Malaysian Ringgit', 'MZN': 'Mozambican Metical', 'NAD': 'Namibian Dollar', 'NGN': 'Nigerian Naira', 'NIO': 'Nicaraguan Córdoba', 'NOK': 'Norwegian Krone', 'NPR': 'Nepalese Rupee', 'NZD': 'New Zealand Dollar', 'OMR': 'Omani Rial', 'PAB': 'Panamanian Balboa', 'PEN': 'Peruvian Nuevo Sol', 'PGK': 'Papua New Guinean Kina', 'PHP': 'Philippine Peso', 'PKR': 'Pakistani Rupee', 'PLN': 'Polish Zloty', 'PYG': 'Paraguayan Guarani', 'QAR': 'Qatari Rial', 'RON': 'Romanian Leu', 'RSD': 'Serbian Dinar', 'RUB': 'Russian Ruble', 'RWF': 'Rwandan Franc', 'SAR': 'Saudi Riyal', 'SBD': 'Solomon Islands Dollar', 'SCR': 'Seychellois Rupee', 'SDG': 'Sudanese Pound', 'SEK': 'Swedish Krona', 'SGD': 'Singapore Dollar', 'SHP': 'Saint Helena Pound', 'SLL': 'Sierra Leonean Leone', 'SOS': 'Somali Shilling', 'SRD': 'Surinamese Dollar', 'STD': 'São Tomé and Pr�\xadncipe Dobra', 'SVC': 'Salvadoran Colón', 'SYP': 'Syrian Pound', 'SZL': 'Swazi Lilangeni', 'THB': 'Thai Baht', 'TJS': 'Tajikistani Somoni', 'TMT': 'Turkmenistani Manat', 'TND': 'Tunisian Dinar', 'TOP': 'Tongan Paʻanga', 'TRY': 'Turkish Lira', 'TTD': 'Trinidad and Tobago Dollar', 'TWD': 'New Taiwan Dollar', 'TZS': 'Tanzanian Shilling', 'UAH': 'Ukrainian Hryvnia', 'UGX': 'Ugandan Shilling', 'USD': 'United States Dollar', 'UYU': 'Uruguayan Peso', 'UZS': 'Uzbekistan Som', 'VEF': 'Venezuelan Bolívar Fuerte', 'VND': 'Vietnamese Dong', 'VUV': 'Vanuatu Vatu', 'WST': 'Samoan Tala', 'XAF': 'CFA Franc BEAC', 'XAG': 'Silver (troy ounce)', 'XAU': 'Gold (troy ounce)', 'XCD': 'East Caribbean Dollar', 'XDR': 'Special Drawing Rights', 'XOF': 'CFA Franc BCEAO', 'XPF': 'CFP Franc', 'YER': 'Yemeni Rial', 'ZAR': 'South African Rand', 'ZMK': 'Zambian Kwacha (pre-2013)', 'ZMW': 'Zambian Kwacha', 'ZWL': 'Zimbabwean Dollar'}

connection = sqlite3.connect("database.db", isolation_level=None)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS currency (code, name, amount, rate, date)")
cursor.execute("CREATE TABLE IF NOT EXISTS transactions (code, name, rate, date)")

#{"success":true,"terms":"https:\/\/currencylayer.com\/terms","privacy":"https:\/\/currencylayer.com\/privacy","timestamp":1718618525,"source":"TRY","quotes":{"TRYAED":0.111858,"TRYAFN":2.154986,"TRYALL":2.860931,"TRYAMD":11.809826,"TRYANG":0.054857,"TRYAOA":26.053234,"TRYARS":27.506844,"TRYAUD":0.046099,"TRYAWG":0.054817,"TRYAZN":0.051745,"TRYBAM":0.055646,"TRYBBD":0.061456,"TRYBDT":3.576938,"TRYBGN":0.055659,"TRYBHD":0.011479,"TRYBIF":87.487518,"TRYBMD":0.030454,"TRYBND":0.041203,"TRYBOB":0.210307,"TRYBRL":0.163729,"TRYBSD":0.030438,"TRYBTC":4.63247e-7,"TRYBTN":2.542692,"TRYBWP":0.414415,"TRYBYN":0.099595,"TRYBYR":596.896473,"TRYBZD":0.061354,"TRYCAD":0.041844,"TRYCDF":86.641359,"TRYCHF":0.027164,"TRYCLF":0.001021,"TRYCLP":28.181442,"TRYCNY":0.220977,"TRYCNH":0.221381,"TRYCOP":126.035604,"TRYCRC":16.047313,"TRYCUC":0.030454,"TRYCUP":0.807028,"TRYCVE":3.137101,"TRYCZK":0.701466,"TRYDJF":5.419566,"TRYDKK":0.212081,"TRYDOP":1.807297,"TRYDZD":4.105988,"TRYEGP":1.452945,"TRYERN":0.456809,"TRYETB":1.740905,"TRYEUR":0.028429,"TRYFJD":0.0683,"TRYFKP":0.023894,"TRYGBP":0.024038,"TRYGEL":0.087396,"TRYGGP":0.023894,"TRYGHS":0.458111,"TRYGIP":0.023894,"TRYGMD":2.063253,"TRYGNF":262.046756,"TRYGTQ":0.236424,"TRYGYD":6.368372,"TRYHKD":0.237853,"TRYHNL":0.752321,"TRYHRK":0.213739,"TRYHTG":4.037682,"TRYHUF":11.258122,"TRYIDR":501.185951,"TRYILS":0.113775,"TRYIMP":0.023894,"TRYINR":2.544574,"TRYIQD":39.872099,"TRYIRR":1282.10926,"TRYISK":4.250463,"TRYJEP":0.023894,"TRYJMD":4.737109,"TRYJOD":0.021589,"TRYJPY":4.80156,"TRYKES":3.941949,"TRYKGS":2.675677,"TRYKHR":125.361347,"TRYKMF":13.932983,"TRYKPW":27.408516,"TRYKRW":42.02457,"TRYKWD":0.009341,"TRYKYD":0.025367,"TRYKZT":13.760947,"TRYLAK":664.787605,"TRYLBP":2726.029282,"TRYLKR":9.257235,"TRYLRD":5.904628,"TRYLSL":0.5589,"TRYLTL":0.089922,"TRYLVL":0.018421,"TRYLYD":0.147581,"TRYMAD":0.305869,"TRYMDL":0.541959,"TRYMGA":135.492306,"TRYMKD":1.75035,"TRYMMK":79.601748,"TRYMNT":105.065964,"TRYMOP":0.244892,"TRYMRU":1.198968,"TRYMUR":1.434985,"TRYMVR":0.4693,"TRYMWK":52.777127,"TRYMXN":0.563782,"TRYMYR":0.143727,"TRYMZN":1.93976,"TRYNAD":0.5589,"TRYNGN":45.543809,"TRYNIO":1.120446,"TRYNOK":0.326296,"TRYNPR":4.068582,"TRYNZD":0.049733,"TRYOMR":0.011723,"TRYPAB":0.030436,"TRYPEN":0.115038,"TRYPGK":0.118618,"TRYPHP":1.786304,"TRYPKR":8.478634,"TRYPLN":0.12406,"TRYPYG":228.926004,"TRYQAR":0.111001,"TRYRON":0.141486,"TRYRSD":3.328337,"TRYRUB":2.707377,"TRYRWF":39.939217,"TRYSAR":0.114254,"TRYSBD":0.257689,"TRYSCR":0.430455,"TRYSDG":17.845977,"TRYSEK":0.321126,"TRYSGD":0.0412,"TRYSHP":0.038477,"TRYSLE":0.69579,"TRYSLL":638.60315,"TRYSOS":17.297817,"TRYSRD":0.961491,"TRYSTD":630.334279,"TRYSVC":0.266336,"TRYSYP":76.516355,"TRYSZL":0.558586,"TRYTHB":1.120963,"TRYTJS":0.325514,"TRYTMT":0.106589,"TRYTND":0.095264,"TRYTOP":0.071899,"TRYTTD":0.206848,"TRYTWD":0.985573,"TRYTZS":79.88101,"TRYUAH":1.238574,"TRYUGX":113.062509,"TRYUSD":0.030454,"TRYUYU":1.192932,"TRYUZS":383.954599,"TRYVEF":110320.858789,"TRYVES":1.107661,"TRYVND":775.204068,"TRYVUV":3.615547,"TRYWST":0.08529,"TRYXAF":18.663823,"TRYXAG":0.001043,"TRYXAU":1.3125663e-5,"TRYXCD":0.082303,"TRYXDR":0.02307,"TRYXOF":18.663387,"TRYXPF":3.39314,"TRYYER":7.622557,"TRYZAR":0.554578,"TRYZMK":274.12097,"TRYZMW":0.79671,"TRYZWL":9.806144}}
# 1 / rate yap

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
        amount = miktar_entry.get()
        rate = 1 / response.json()["quotes"]["TRY" + code]
        date = response.json()["timestamp"]

        cursor.execute("INSERT INTO currency VALUES (?, ?, ?, ?, ?)", (code, name, amount, rate, date))
        messagebox.showinfo("Başarılı", "Varlık eklendi.")
        ekleme_penceresi.destroy()

    button = tk.Button(ekleme_penceresi, text="Ekle", command=db_ekle)

    lb_varlıklar.pack(side=tk.LEFT)
    miktar_label.pack(side=tk.LEFT)
    miktar_entry.pack(side=tk.LEFT)
    button.pack(side=tk.LEFT)

    for key in table.keys():
        lb_varlıklar.insert(tk.END, key + " - " + table[key])

menubar = tk.Menu(root)
menubar.add_command(label="Yeni Varlık Ekle", command=varlık_ekle)

root.config(menu=menubar)
root.mainloop()