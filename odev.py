import sqlite3
import tkinter as tk
from tkinter import messagebox
import requests
import time
import datetime

api_key = "69005d1fe73f2f98149fb531ef76816e"
url_live = f"http://api.currencylayer.com/live?access_key={api_key}&source=TRY"

live = {"success":True,"timestamp":1718618525,"source":"TRY","quotes":{"TRYAED":2,"TRYAFN":2.154986,"TRYALL":2.860931,"TRYAMD":11.809826,"TRYANG":0.054857,"TRYAOA":26.053234,"TRYARS":27.506844,"TRYAUD":0.046099,"TRYAWG":0.054817,"TRYAZN":0.051745,"TRYBAM":0.055646,"TRYBBD":0.061456,"TRYBDT":3.576938,"TRYBGN":0.055659,"TRYBHD":0.011479,"TRYBIF":87.487518,"TRYBMD":0.030454,"TRYBND":0.041203,"TRYBOB":0.210307,"TRYBRL":0.163729,"TRYBSD":0.030438,"TRYBTC":4.63247e-7,"TRYBTN":2.542692,"TRYBWP":0.414415,"TRYBYN":0.099595,"TRYBYR":596.896473,"TRYBZD":0.061354,"TRYCAD":0.041844,"TRYCDF":86.641359,"TRYCHF":0.027164,"TRYCLF":0.001021,"TRYCLP":28.181442,"TRYCNY":0.220977,"TRYCNH":0.221381,"TRYCOP":126.035604,"TRYCRC":16.047313,"TRYCUC":0.030454,"TRYCUP":0.807028,"TRYCVE":3.137101,"TRYCZK":0.701466,"TRYDJF":5.419566,"TRYDKK":0.212081,"TRYDOP":1.807297,"TRYDZD":4.105988,"TRYEGP":1.452945,"TRYERN":0.456809,"TRYETB":1.740905,"TRYEUR":0.028429,"TRYFJD":0.0683,"TRYFKP":0.023894,"TRYGBP":0.024038,"TRYGEL":0.087396,"TRYGGP":0.023894,"TRYGHS":0.458111,"TRYGIP":0.023894,"TRYGMD":2.063253,"TRYGNF":262.046756,"TRYGTQ":0.236424,"TRYGYD":6.368372,"TRYHKD":0.237853,"TRYHNL":0.752321,"TRYHRK":0.213739,"TRYHTG":4.037682,"TRYHUF":11.258122,"TRYIDR":501.185951,"TRYILS":0.113775,"TRYIMP":0.023894,"TRYINR":2.544574,"TRYIQD":39.872099,"TRYIRR":1282.10926,"TRYISK":4.250463,"TRYJEP":0.023894,"TRYJMD":4.737109,"TRYJOD":0.021589,"TRYJPY":4.80156,"TRYKES":3.941949,"TRYKGS":2.675677,"TRYKHR":125.361347,"TRYKMF":13.932983,"TRYKPW":27.408516,"TRYKRW":42.02457,"TRYKWD":0.009341,"TRYKYD":0.025367,"TRYKZT":13.760947,"TRYLAK":664.787605,"TRYLBP":2726.029282,"TRYLKR":9.257235,"TRYLRD":5.904628,"TRYLSL":0.5589,"TRYLTL":0.089922,"TRYLVL":0.018421,"TRYLYD":0.147581,"TRYMAD":0.305869,"TRYMDL":0.541959,"TRYMGA":135.492306,"TRYMKD":1.75035,"TRYMMK":79.601748,"TRYMNT":105.065964,"TRYMOP":0.244892,"TRYMRU":1.198968,"TRYMUR":1.434985,"TRYMVR":0.4693,"TRYMWK":52.777127,"TRYMXN":0.563782,"TRYMYR":0.143727,"TRYMZN":1.93976,"TRYNAD":0.5589,"TRYNGN":45.543809,"TRYNIO":1.120446,"TRYNOK":0.326296,"TRYNPR":4.068582,"TRYNZD":0.049733,"TRYOMR":0.011723,"TRYPAB":0.030436,"TRYPEN":0.115038,"TRYPGK":0.118618,"TRYPHP":1.786304,"TRYPKR":8.478634,"TRYPLN":0.12406,"TRYPYG":228.926004,"TRYQAR":0.111001,"TRYRON":0.141486,"TRYRSD":3.328337,"TRYRUB":2.707377,"TRYRWF":39.939217,"TRYSAR":0.114254,"TRYSBD":0.257689,"TRYSCR":0.430455,"TRYSDG":17.845977,"TRYSEK":0.321126,"TRYSGD":0.0412,"TRYSHP":0.038477,"TRYSLE":0.69579,"TRYSLL":638.60315,"TRYSOS":17.297817,"TRYSRD":0.961491,"TRYSTD":630.334279,"TRYSVC":0.266336,"TRYSYP":76.516355,"TRYSZL":0.558586,"TRYTHB":1.120963,"TRYTJS":0.325514,"TRYTMT":0.106589,"TRYTND":0.095264,"TRYTOP":0.071899,"TRYTTD":0.206848,"TRYTWD":0.985573,"TRYTZS":79.88101,"TRYUAH":1.238574,"TRYUGX":113.062509,"TRYUSD":0.030454,"TRYUYU":1.192932,"TRYUZS":383.954599,"TRYVEF":110320.858789,"TRYVES":1.107661,"TRYVND":775.204068,"TRYVUV":3.615547,"TRYWST":0.08529,"TRYXAF":18.663823,"TRYXAG":0.001043,"TRYXAU":1.3125663e-5,"TRYXCD":0.082303,"TRYXDR":0.02307,"TRYXOF":18.663387,"TRYXPF":3.39314,"TRYYER":7.622557,"TRYZAR":0.554578,"TRYZMK":274.12097,"TRYZMW":0.79671,"TRYZWL":9.806144}} #requests.get(url_live).json()


table = {'AED': 'United Arab Emirates Dirham', 'AFN': 'Afghan Afghani', 'ALL': 'Albanian Lek', 'AMD': 'Armenian Dram', 'ANG': 'Netherlands Antillean Guilder', 'AOA': 'Angolan Kwanza', 'ARS': 'Argentine Peso', 'AUD': 'Australian Dollar', 'AWG': 'Aruban Florin', 'AZN': 'Azerbaijani Manat', 'BAM': 'Bosnia-Herzegovina Convertible Mark', 'BBD': 'Barbadian Dollar', 'BDT': 'Bangladeshi Taka', 'BGN': 'Bulgarian Lev', 'BHD': 'Bahraini Dinar', 'BIF': 'Burundian Franc', 'BMD': 'Bermudan Dollar', 'BND': 'Brunei Dollar', 'BOB': 'Bolivian Boliviano', 'BRL': 'Brazilian Real', 'BSD': 'Bahamian Dollar', 'BTC': 'Bitcoin', 'BTN': 'Bhutanese Ngultrum', 'BWP': 'Botswanan Pula', 'BYN': 'New Belarusian Ruble', 'BYR': 'Belarusian Ruble', 'BZD': 'Belize Dollar', 'CAD': 'Canadian Dollar', 'CDF': 'Congolese Franc', 'CHF': 'Swiss Franc', 'CLF': 'Chilean Unit of Account (UF)', 'CLP': 'Chilean Peso', 'CNY': 'Chinese Yuan', 'CNH': 'Chinese Yuan Offshore', 'COP': 'Colombian Peso', 'CRC': 'Costa Rican Colón', 'CUC': 'Cuban Convertible Peso', 'CUP': 'Cuban Peso', 'CVE': 'Cape Verdean Escudo', 'CZK': 'Czech Republic Koruna', 'DJF': 'Djiboutian Franc', 'DKK': 'Danish Krone', 'DOP': 'Dominican Peso', 'DZD': 'Algerian Dinar', 'EGP': 'Egyptian Pound', 'ERN': 'Eritrean Nakfa', 'ETB': 'Ethiopian Birr', 'EUR': 'Euro', 'FJD': 'Fijian Dollar', 'FKP': 'Falkland Islands Pound', 'GBP': 'British Pound Sterling', 'GEL': 'Georgian Lari', 'GGP': 'Guernsey Pound', 'GHS': 'Ghanaian Cedi', 'GIP': 'Gibraltar Pound', 'GMD': 'Gambian Dalasi', 'GNF': 'Guinean Franc', 'GTQ': 'Guatemalan Quetzal', 'GYD': 'Guyanaese Dollar', 'HKD': 'Hong Kong Dollar', 'HNL': 'Honduran Lempira', 'HRK': 'Croatian Kuna', 'HTG': 'Haitian Gourde', 'HUF': 'Hungarian Forint', 'IDR': 'Indonesian Rupiah', 'ILS': 'Israeli New Sheqel', 'IMP': 'Manx pound', 'INR': 'Indian Rupee', 'IQD': 'Iraqi Dinar', 'IRR': 'Iranian Rial', 'ISK': 'Icelandic Króna', 'JEP': 'Jersey Pound', 'JMD': 'Jamaican Dollar', 'JOD': 'Jordanian Dinar', 'JPY': 'Japanese Yen', 'KES': 'Kenyan Shilling', 'KGS': 'Kyrgystani Som', 'KHR': 'Cambodian Riel', 'KMF': 'Comorian Franc', 'KPW': 'North Korean Won', 'KRW': 'South Korean Won', 'KWD': 'Kuwaiti Dinar', 'KYD': 'Cayman Islands Dollar', 'KZT': 'Kazakhstani Tenge', 'LAK': 'Laotian Kip', 'LBP': 'Lebanese Pound', 'LKR': 'Sri Lankan Rupee', 'LRD': 'Liberian Dollar', 'LSL': 'Lesotho Loti', 'LTL': 'Lithuanian Litas', 'LVL': 'Latvian Lats', 'LYD': 'Libyan Dinar', 'MAD': 'Moroccan Dirham', 'MDL': 'Moldovan Leu', 'MGA': 'Malagasy Ariary', 'MKD': 'Macedonian Denar', 'MMK': 'Myanma Kyat', 'MNT': 'Mongolian Tugrik', 'MOP': 'Macanese Pataca', 'MRU': 'Mauritanian Ouguiya', 'MUR': 'Mauritian Rupee', 'MVR': 'Maldivian Rufiyaa', 'MWK': 'Malawian Kwacha', 'MXN': 'Mexican Peso', 'MYR': 'Malaysian Ringgit', 'MZN': 'Mozambican Metical', 'NAD': 'Namibian Dollar', 'NGN': 'Nigerian Naira', 'NIO': 'Nicaraguan Córdoba', 'NOK': 'Norwegian Krone', 'NPR': 'Nepalese Rupee', 'NZD': 'New Zealand Dollar', 'OMR': 'Omani Rial', 'PAB': 'Panamanian Balboa', 'PEN': 'Peruvian Nuevo Sol', 'PGK': 'Papua New Guinean Kina', 'PHP': 'Philippine Peso', 'PKR': 'Pakistani Rupee', 'PLN': 'Polish Zloty', 'PYG': 'Paraguayan Guarani', 'QAR': 'Qatari Rial', 'RON': 'Romanian Leu', 'RSD': 'Serbian Dinar', 'RUB': 'Russian Ruble', 'RWF': 'Rwandan Franc', 'SAR': 'Saudi Riyal', 'SBD': 'Solomon Islands Dollar', 'SCR': 'Seychellois Rupee', 'SDG': 'South Sudanese Pound', 'SEK': 'Swedish Krona', 'SGD': 'Singapore Dollar', 'SHP': 'Saint Helena Pound', 'SLE': 'Sierra Leonean Leone', 'SLL': 'Sierra Leonean Leone', 'SOS': 'Somali Shilling', 'SRD': 'Surinamese Dollar', 'STD': 'São Tomé and Príncipe Dobra', 'SVC': 'Salvadoran Colón', 'SYP': 'Syrian Pound', 'SZL': 'Swazi Lilangeni', 'THB': 'Thai Baht', 'TJS': 'Tajikistani Somoni', 'TMT': 'Turkmenistani Manat', 'TND': 'Tunisian Dinar', 'TOP': 'Tongan Paʻanga', 'TRY': 'Turkish Lira', 'TTD': 'Trinidad and Tobago Dollar', 'TWD': 'New Taiwan Dollar', 'TZS': 'Tanzanian Shilling', 'UAH': 'Ukrainian Hryvnia', 'UGX': 'Ugandan Shilling', 'USD': 'United States Dollar', 'UYU': 'Uruguayan Peso', 'UZS': 'Uzbekistan Som', 'VEF': 'Venezuelan Bolívar Fuerte', 'VES': 'Sovereign Bolivar', 'VND': 'Vietnamese Dong', 'VUV': 'Vanuatu Vatu', 'WST': 'Samoan Tala', 'XAF': 'CFA Franc BEAC', 'XAG': 'Silver (troy ounce)', 'XAU': 'Gold (troy ounce)', 'XCD': 'East Caribbean Dollar', 'XDR': 'Special Drawing Rights', 'XOF': 'CFA Franc BCEAO', 'XPF': 'CFP Franc', 'YER': 'Yemeni Rial', 'ZAR': 'South African Rand', 'ZMK': 'Zambian Kwacha (pre-2013)', 'ZMW': 'Zambian Kwacha', 'ZWL': 'Zimbabwean Dollar'}

connection = sqlite3.connect("database.db", isolation_level=None)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS myAssets (code, name, amount, rate, date)")
cursor.execute("CREATE TABLE IF NOT EXISTS log (code, name, rate, date)")

#{"success":true,"terms":"https:\/\/currencylayer.com\/terms","privacy":"https:\/\/currencylayer.com\/privacy","timestamp":1718618525,"source":"TRY","quotes":{"TRYAED":0.111858,"TRYAFN":2.154986,"TRYALL":2.860931,"TRYAMD":11.809826,"TRYANG":0.054857,"TRYAOA":26.053234,"TRYARS":27.506844,"TRYAUD":0.046099,"TRYAWG":0.054817,"TRYAZN":0.051745,"TRYBAM":0.055646,"TRYBBD":0.061456,"TRYBDT":3.576938,"TRYBGN":0.055659,"TRYBHD":0.011479,"TRYBIF":87.487518,"TRYBMD":0.030454,"TRYBND":0.041203,"TRYBOB":0.210307,"TRYBRL":0.163729,"TRYBSD":0.030438,"TRYBTC":4.63247e-7,"TRYBTN":2.542692,"TRYBWP":0.414415,"TRYBYN":0.099595,"TRYBYR":596.896473,"TRYBZD":0.061354,"TRYCAD":0.041844,"TRYCDF":86.641359,"TRYCHF":0.027164,"TRYCLF":0.001021,"TRYCLP":28.181442,"TRYCNY":0.220977,"TRYCNH":0.221381,"TRYCOP":126.035604,"TRYCRC":16.047313,"TRYCUC":0.030454,"TRYCUP":0.807028,"TRYCVE":3.137101,"TRYCZK":0.701466,"TRYDJF":5.419566,"TRYDKK":0.212081,"TRYDOP":1.807297,"TRYDZD":4.105988,"TRYEGP":1.452945,"TRYERN":0.456809,"TRYETB":1.740905,"TRYEUR":0.028429,"TRYFJD":0.0683,"TRYFKP":0.023894,"TRYGBP":0.024038,"TRYGEL":0.087396,"TRYGGP":0.023894,"TRYGHS":0.458111,"TRYGIP":0.023894,"TRYGMD":2.063253,"TRYGNF":262.046756,"TRYGTQ":0.236424,"TRYGYD":6.368372,"TRYHKD":0.237853,"TRYHNL":0.752321,"TRYHRK":0.213739,"TRYHTG":4.037682,"TRYHUF":11.258122,"TRYIDR":501.185951,"TRYILS":0.113775,"TRYIMP":0.023894,"TRYINR":2.544574,"TRYIQD":39.872099,"TRYIRR":1282.10926,"TRYISK":4.250463,"TRYJEP":0.023894,"TRYJMD":4.737109,"TRYJOD":0.021589,"TRYJPY":4.80156,"TRYKES":3.941949,"TRYKGS":2.675677,"TRYKHR":125.361347,"TRYKMF":13.932983,"TRYKPW":27.408516,"TRYKRW":42.02457,"TRYKWD":0.009341,"TRYKYD":0.025367,"TRYKZT":13.760947,"TRYLAK":664.787605,"TRYLBP":2726.029282,"TRYLKR":9.257235,"TRYLRD":5.904628,"TRYLSL":0.5589,"TRYLTL":0.089922,"TRYLVL":0.018421,"TRYLYD":0.147581,"TRYMAD":0.305869,"TRYMDL":0.541959,"TRYMGA":135.492306,"TRYMKD":1.75035,"TRYMMK":79.601748,"TRYMNT":105.065964,"TRYMOP":0.244892,"TRYMRU":1.198968,"TRYMUR":1.434985,"TRYMVR":0.4693,"TRYMWK":52.777127,"TRYMXN":0.563782,"TRYMYR":0.143727,"TRYMZN":1.93976,"TRYNAD":0.5589,"TRYNGN":45.543809,"TRYNIO":1.120446,"TRYNOK":0.326296,"TRYNPR":4.068582,"TRYNZD":0.049733,"TRYOMR":0.011723,"TRYPAB":0.030436,"TRYPEN":0.115038,"TRYPGK":0.118618,"TRYPHP":1.786304,"TRYPKR":8.478634,"TRYPLN":0.12406,"TRYPYG":228.926004,"TRYQAR":0.111001,"TRYRON":0.141486,"TRYRSD":3.328337,"TRYRUB":2.707377,"TRYRWF":39.939217,"TRYSAR":0.114254,"TRYSBD":0.257689,"TRYSCR":0.430455,"TRYSDG":17.845977,"TRYSEK":0.321126,"TRYSGD":0.0412,"TRYSHP":0.038477,"TRYSLE":0.69579,"TRYSLL":638.60315,"TRYSOS":17.297817,"TRYSRD":0.961491,"TRYSTD":630.334279,"TRYSVC":0.266336,"TRYSYP":76.516355,"TRYSZL":0.558586,"TRYTHB":1.120963,"TRYTJS":0.325514,"TRYTMT":0.106589,"TRYTND":0.095264,"TRYTOP":0.071899,"TRYTTD":0.206848,"TRYTWD":0.985573,"TRYTZS":79.88101,"TRYUAH":1.238574,"TRYUGX":113.062509,"TRYUSD":0.030454,"TRYUYU":1.192932,"TRYUZS":383.954599,"TRYVEF":110320.858789,"TRYVES":1.107661,"TRYVND":775.204068,"TRYVUV":3.615547,"TRYWST":0.08529,"TRYXAF":18.663823,"TRYXAG":0.001043,"TRYXAU":1.3125663e-5,"TRYXCD":0.082303,"TRYXDR":0.02307,"TRYXOF":18.663387,"TRYXPF":3.39314,"TRYYER":7.622557,"TRYZAR":0.554578,"TRYZMK":274.12097,"TRYZMW":0.79671,"TRYZWL":9.806144}}
# 1 / rate yap

def get_historical(date):
	url_historical = f"http://api.currencylayer.com/historical?access_key={api_key}&date={date.strftime('%Y-%m-%d')}&source=TRY"
	response = {'success': True, 'terms': 'https://currencylayer.com/terms', 'privacy': 'https://currencylayer.com/privacy', 'historical': True, 'date': '2024-06-17', 'timestamp': 1718650985, 'source': 'TRY', 'quotes': {'TRYAED': 0.111872, 'TRYAFN': 2.147253, 'TRYALL': 2.854616, 'TRYAMD': 11.841273, 'TRYANG': 0.05488, 'TRYAOA': 25.964558, 'TRYARS': 27.48805, 'TRYAUD': 0.046045, 'TRYAWG': 0.0549, 'TRYAZN': 0.051596, 'TRYBAM': 0.055608, 'TRYBBD': 0.061485, 'TRYBDT': 3.578221, 'TRYBGN': 0.055522, 'TRYBHD': 0.011478, 'TRYBIF': 87.71769, 'TRYBMD': 0.030458, 'TRYBND': 0.041201, 'TRYBOB': 0.210428, 'TRYBRL': 0.165149, 'TRYBSD': 0.030451, 'TRYBTC': 4.55121e-07, 'TRYBTN': 2.543622, 'TRYBWP': 0.41318, 'TRYBYN': 0.099656, 'TRYBYR': 596.967609, 'TRYBZD': 0.06138, 'TRYCAD': 0.041798, 'TRYCDF': 86.803962, 'TRYCHF': 0.027098, 'TRYCLF': 0.001023, 'TRYCLP': 28.231377, 'TRYCNY': 0.221003, 'TRYCNH': 0.221422, 'TRYCOP': 125.865747, 'TRYCRC': 16.001772, 'TRYCUC': 0.030458, 'TRYCUP': 0.807125, 'TRYCVE': 3.143978, 'TRYCZK': 0.700879, 'TRYDJF': 5.412905, 'TRYDKK': 0.211646, 'TRYDOP': 1.80625, 'TRYDZD': 4.106232, 'TRYEGP': 1.453221, 'TRYERN': 0.456863, 'TRYETB': 1.756268, 'TRYEUR': 0.028372, 'TRYFJD': 0.068309, 'TRYFKP': 0.023897, 'TRYGBP': 0.023972, 'TRYGEL': 0.087261, 'TRYGGP': 0.023897, 'TRYGHS': 0.458386, 'TRYGIP': 0.023897, 'TRYGMD': 2.06426, 'TRYGNF': 261.782476, 'TRYGTQ': 0.236615, 'TRYGYD': 6.370112, 'TRYHKD': 0.237908, 'TRYHNL': 0.752805, 'TRYHRK': 0.213764, 'TRYHTG': 4.039395, 'TRYHUF': 11.226344, 'TRYIDR': 501.379694, 'TRYILS': 0.11341, 'TRYIMP': 0.023897, 'TRYINR': 2.543, 'TRYIQD': 39.890701, 'TRYIRR': 1281.881361, 'TRYISK': 4.241529, 'TRYJEP': 0.023897, 'TRYJMD': 4.74452, 'TRYJOD': 0.021591, 'TRYJPY': 4.803716, 'TRYKES': 3.913916, 'TRYKGS': 2.675996, 'TRYKHR': 125.415454, 'TRYKMF': 13.934458, 'TRYKPW': 27.411782, 'TRYKRW': 42.029108, 'TRYKWD': 0.009341, 'TRYKYD': 0.025376, 'TRYKZT': 13.815603, 'TRYLAK': 668.160151, 'TRYLBP': 2727.056831, 'TRYLKR': 9.250491, 'TRYLRD': 5.907691, 'TRYLSL': 0.554921, 'TRYLTL': 0.089933, 'TRYLVL': 0.018423, 'TRYLYD': 0.14765, 'TRYMAD': 0.304292, 'TRYMDL': 0.543713, 'TRYMGA': 136.47567, 'TRYMKD': 1.747509, 'TRYMMK': 63.768762, 'TRYMNT': 105.078485, 'TRYMOP': 0.24494, 'TRYMRU': 1.199195, 'TRYMUR': 1.434862, 'TRYMVR': 0.469346, 'TRYMWK': 52.784808, 'TRYMXN': 0.564832, 'TRYMYR': 0.143744, 'TRYMZN': 1.939993, 'TRYNAD': 0.554921, 'TRYNGN': 45.169726, 'TRYNIO': 1.120806, 'TRYNOK': 0.324665, 'TRYNPR': 4.06979, 'TRYNZD': 0.049668, 'TRYOMR': 0.011724, 'TRYPAB': 0.030451, 'TRYPEN': 0.114844, 'TRYPGK': 0.117085, 'TRYPHP': 1.786471, 'TRYPKR': 8.482261, 'TRYPLN': 0.123344, 'TRYPYG': 229.33599, 'TRYQAR': 0.111066, 'TRYRON': 0.141189, 'TRYRSD': 3.321322, 'TRYRUB': 2.694781, 'TRYRWF': 39.795074, 'TRYSAR': 0.114284, 'TRYSBD': 0.257719, 'TRYSCR': 0.433143, 'TRYSDG': 17.848126, 'TRYSEK': 0.319254, 'TRYSGD': 0.041176, 'TRYSHP': 0.038482, 'TRYSLE': 0.695872, 'TRYSLL': 638.679256, 'TRYSOS': 17.403491, 'TRYSRD': 0.955377, 'TRYSTD': 630.4094, 'TRYSVC': 0.26644, 'TRYSYP': 76.525474, 'TRYSZL': 0.554717, 'TRYTHB': 1.121146, 'TRYTJS': 0.327773, 'TRYTMT': 0.106601, 'TRYTND': 0.095229, 'TRYTOP': 0.071907, 'TRYTTD': 0.20696, 'TRYTWD': 0.985173, 'TRYTZS': 79.890531, 'TRYUAH': 1.237849, 'TRYUGX': 112.819887, 'TRYUSD': 0.030458, 'TRYUYU': 1.196721, 'TRYUZS': 384.520199, 'TRYVEF': 110334.00642, 'TRYVES': 1.107837, 'TRYVND': 775.296454, 'TRYVUV': 3.615978, 'TRYWST': 0.0853, 'TRYXAF': 18.650452, 'TRYXAG': 0.001035, 'TRYXAU': 1.31364e-05, 'TRYXCD': 0.082313, 'TRYXDR': 0.02311, 'TRYXOF': 18.650452, 'TRYXPF': 3.390852, 'TRYYER': 7.623462, 'TRYZAR': 0.555937, 'TRYZMK': 274.154313, 'TRYZMW': 0.786413, 'TRYZWL': 9.807313}} #requests.get(url_historical).json()  
	time.sleep(1)
	return response

def get_date(epoch):
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))

cursor.execute("SELECT * FROM log WHERE date = ?", (get_date(live["timestamp"],)))
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
		amount = miktar_entry.get().replace(",", ".")
		rate = live["quotes"]["TRY" + code]
		date = live["timestamp"]

		cursor.execute("SELECT * FROM myAssets WHERE code = ?", (code,))
		foo = cursor.fetchone()
		if foo:
			cursor.execute("INSERT INTO myAssets VALUES (?, ?, ?, ?, ?)", (code, name, amount + foo[2], rate, date))
			messagebox.showinfo("Başarılı", "Varlık Güncellendi.")

			data = f"{code} - {name} - {float(amount) + float(foo[2])} - {rate:.2f} - {get_date(date)} - Yeni Kayıt"
			data_format = "{:<5} {:<25} {:<10} {:<10} {:<20} {:<15}"
			
			for i in lb_toplam.get(0, tk.END):
				if code in i:
					lb_toplam.delete(lb_toplam.get(0, tk.END).index(i))
			
			lb_toplam.insert(tk.END, data_format.format(*data.split(" - ")))
		else:
			cursor.execute("INSERT INTO myAssets VALUES (?, ?, ?, ?, ?)", (code, name, amount, rate, date))
			messagebox.showinfo("Başarılı", "Varlık eklendi.")

			data = f"{code} - {name} - {amount} - {rate:.2f} - {get_date(date)} - Yeni Kayıt"
			data_format = "{:<5} {:<25} {:<10} {:<10} {:<20} {:<15}"
			lb_toplam.insert(tk.END, data_format.format(*data.split(" - ")))

		ekleme_penceresi.destroy()

	button = tk.Button(ekleme_penceresi, text="Ekle", command=db_ekle)

	lb_varlıklar.pack(side=tk.LEFT, padx=5)
	miktar_label.pack(side=tk.LEFT, padx=5)
	miktar_entry.pack(side=tk.LEFT, padx=5)
	button.pack(side=tk.LEFT, padx=5)

	for key in table.keys():
		lb_varlıklar.insert(tk.END, key + " - " + table[key])

menubar = tk.Menu(root)
menubar.add_command(label="Yeni Varlık Ekle", command=varlık_ekle)
#Varlıklarım
frame_varlıklar = tk.Frame(root)
lb_toplam = tk.Listbox(frame_varlıklar, font=("Courier New", 10), width=120)
lb_toplam.pack(side=tk.LEFT, padx=5)
frame_varlıklar.pack(side=tk.LEFT, padx=5)
headers = ["Kod", "İsim", "Miktar", "Kur", "Eklenme Tarihi", "TRY Karşılığı", "Kar/Zarar"]
header_format = "{:<5} {:<25} {:<10} {:<10} {:<20} {:<15} {:<15}"
lb_toplam.insert(tk.END, header_format.format(*headers))

cursor.execute("SELECT DISTINCT code FROM myAssets")
unique_codes = cursor.fetchall()
for code in unique_codes:
	cursor.execute("SELECT * FROM myAssets WHERE code = ?", (code[0],))
	asset = cursor.fetchone()
	kod = asset[0]
	isim = asset[1]
	miktar = float(asset[2])
	tarihi_kur = asset[3]
	güncel_kur =float(live["quotes"]["TRY" + kod])
	print(güncel_kur, tarihi_kur)
	tarih = get_date(asset[4])
	kar_zarar = (güncel_kur - tarihi_kur) * miktar
	data = f"{kod} - {isim} - {miktar} - {(1 / güncel_kur):.2f} - {tarih} - {1 / güncel_kur * miktar:.2f} TRY - {kar_zarar:.2f} TRY ({((güncel_kur - tarihi_kur) * 100):.2f}%)"
	data_format = "{:<5} {:<25} {:<10} {:<10} {:<20} {:<15} {:<15}"
	lb_toplam.insert(tk.END, data_format.format(*data.split(" - ")))

root.config(menu=menubar)
root.mainloop()