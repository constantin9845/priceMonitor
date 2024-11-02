import requests


class Data:
    def __init__(self):

        self.selected_base = "usd"
        self.selected_currencies = ["cad","krw","eur"]
        self.selected_assets = ["xau", "xag"]
        self.selected_securities = ["btc"]


        # call data here
        self.usd, self.gold, self.silver, self.btc = self.request_data()

    def request_data(self):

        # request data
        BASE_USD_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json"

        BASE_GOLD_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xau.json"
        BASE_SILVER_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xag.json"

        BASE_BTC_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/btc.json"


        usd = requests.get(BASE_USD_URL)
        gold = requests.get(BASE_GOLD_URL)
        silver = requests.get(BASE_SILVER_URL)
        btc = requests.get(BASE_BTC_URL)

        if usd.status_code == 200 and gold.status_code == 200 and btc.status_code == 200:
            usd = usd.json()
            gold = gold.json()
            silver = silver.json()
            btc = btc.json()
        else:
            print("Could not load data")
            exit(1)

        return usd, gold, silver, btc

    # All data for initial setup
    def return_basic(self):

        currencies = [
            "CAD : $"+str(self.usd['usd']['cad'])[:6],  # cad price in usd
            "KRW : $"+str(self.usd['usd']['krw'])[:6],  # krw price in usd
            "EUR : $"+str(self.usd['usd']['eur'])[:6],  # eur price in usd
        ]

        assets = [
            "GOLD   : $" + str(self.gold['xau']['usd'])[:4],  # gold price in usd
            "SILVER : $" + str(self.silver['xag']['usd'])[:4],  # silver price in usd
        ]

        securities = [
            "BTC    : $" + str(self.btc['btc']['usd'])[:5],  # btc price in usd
        ]

        return str(self.usd['date']), currencies, assets, securities

    def get_status(self):
        return [self.selected_base, self.selected_currencies, self.selected_assets, self.selected_securities]

    def set_status(self, new_base, new_currencies, new_assets, new_securities):
        self.selected_base = new_base
        self.selected_currencies = new_currencies
        self.selected_assets = new_assets
        self.selected_securities = new_securities



#DATE = usd['date']
#KRW_PRICE = usd['usd']['krw']
