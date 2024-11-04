import os
import platform
from locale import currency

import requests

def get_currencies():

    BASE_USD_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json"
    currencies = requests.get(BASE_USD_URL)

    if currencies.status_code == 200:
        currencies = currencies.json()
    else:
        exit(3)

    # parse data
    currencyList = [
        str(currencies['usd']['cad'])[:6],
        str(currencies['usd']['krw'])[:6],
        str(currencies['usd']['eur'])[:6],
        str(currencies['usd']['gbp'])[:6],
        str(currencies['usd']['rub'])[:6],
        str(currencies['usd']['chf'])[:6]
    ]

    currency_names = [
        "CAD", "KRW", "EUR", "GBP", "RUB", "CHF"
    ]

    return currencyList, currency_names

def get_assets():

    BASE_GOLD_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xau.json"
    BASE_Silver_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xag.json"
    BASE_PLATINUM_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xpt.json"
    BASE_PALLADIUM_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xpd.json"

    asset1 = requests.get(BASE_GOLD_URL)
    asset2 = requests.get(BASE_Silver_URL)
    asset3 = requests.get(BASE_PLATINUM_URL)
    asset4 = requests.get(BASE_PALLADIUM_URL)

    if asset1.status_code == 200 and asset2.status_code == 200 and asset3.status_code == 200 and asset4.status_code == 200:
        asset1 = asset1.json()
        asset2 = asset2.json()
        asset3 = asset3.json()
        asset4 = asset4.json()
    else:
        exit(3)

    # parse data
    assetList = [
        str(asset1['xau']['usd'])[:6],
        str(asset2['xag']['usd'])[:6],
        str(asset3['xpt']['usd'])[:6],
        str(asset4['xpd']['usd'])[:6],
        "______",
        "______"
    ]

    asset_names = [
        "GOLD     ", "SILVER   ", "PLATINUM ", "PALLADIUM", "_________", "_________"
    ]

    return assetList, asset_names

def get_crypto():

    BASE_BITCOIN_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/btc.json"
    BASE_ETHEREUM_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eth.json"
    BASE_TETHER_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usdt.json"
    BASE_MONERO_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xmr.json"
    BASE_DOGE_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/doge.json"
    BASE_SHIBA_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/shib.json"

    asset1 = requests.get(BASE_BITCOIN_URL)
    asset2 = requests.get(BASE_ETHEREUM_URL)
    asset3 = requests.get(BASE_TETHER_URL)
    asset4 = requests.get(BASE_MONERO_URL)
    asset5 = requests.get(BASE_DOGE_URL)
    asset6 = requests.get(BASE_SHIBA_URL)

    if (
            asset1.status_code == 200 and
            asset2.status_code == 200 and
            asset3.status_code == 200 and
            asset4.status_code == 200 and
            asset5.status_code == 200 and
            asset6.status_code == 200
    ):
        asset1 = asset1.json()
        asset2 = asset2.json()
        asset3 = asset3.json()
        asset4 = asset4.json()
        asset5 = asset5.json()
        asset6 = asset6.json()
    else:
        exit(3)

    # parse data
    assetList = [
        str(asset1['btc']['usd'])[:7],
        str(asset2['eth']['usd'])[:7],
        str(asset3['usdt']['usd'])[:7],
        str(asset4['xmr']['usd'])[:7],
        str(asset5['doge']['usd'])[:7],
        str(asset6['shib']['usd'])[:7],
    ]

    asset_names = [
        "BITCOIN  ", "ETHEREUM ", "TETHER   ", "MONERO   ", "DOGE COIN", "SHIBA INU"
    ]

    return assetList, asset_names

def format_output():
    output = "BASE: USD"
    output+="\nCurrencies\tAssets          \tCrypto"

    list1, names1 = get_currencies()
    list2, names2 = get_assets()
    list3, names3 = get_crypto()

    for i in range(0,6):
        output+=f"\n{names1[i]} {list1[i]}\t{names2[i]} {list2[i]}\t{names3[i]} {list3[i]}"

    return output


command = ""

if platform.system() == 'Linux':
    # Command to open a new terminal and start counting
    #command = "gnome-terminal -- bash -c 'for i in {1..1000}; do echo $i; sleep 1; clear; done'"

    command = f"gnome-terminal -- bash -c 'while true; do echo \"{format_output()}\"; sleep 3; clear; done'"
    os.system(command)

elif platform.system() == 'Windows':
    command = f"cmd /k \"for /L %i in (1,1,1000) do (echo {format_output()} & timeout /t 3 > nul & cls)\""
else:
    # max
    pass


# Execute the command
os.system(command)
