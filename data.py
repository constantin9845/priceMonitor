import requests


class Data:
    def __init__(self):

        # call data here
        self.usd, self.gold, self.btc = self.request_data()

    def request_data(self):

        # request data
        BASE_USD_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json"
        BASE_GOLD_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xau.json"
        BASE_BTC_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/btc.json"

        usd = requests.get(BASE_USD_URL)
        gold = requests.get(BASE_GOLD_URL)
        btc = requests.get(BASE_BTC_URL)

        if usd.status_code == 200 and gold.status_code == 200 and btc.status_code == 200:
            usd = usd.json()
            gold = gold.json()
            btc = btc.json()
        else:
            print("Could not load data")
            exit(1)

        return usd, gold, btc

    # All data for initial setup
    def return_basic(self):
        arr = [
               str(self.usd['usd']['cad'])[:6],  #cad price in usd
               str(self.usd['usd']['krw'])[:6],  # krw price in usd
               str(self.usd['usd']['eur'])[:6],  # eur price in usd
               str(self.btc['btc']['usd'])[:6],  # btc price in usd
               str(self.gold['xau']['usd'])[:5], # gold price in usd
               ]


        return arr

#DATE = usd['date']
#KRW_PRICE = usd['usd']['krw']
