from datetime import datetime

import requests


def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    if not (currency_code and url):
        return None

    currency_code = currency_code.upper()

    responses = requests.get(url)

    if responses.ok:

        cur = responses.text.split(currency_code)

        if len(cur) == 1:
            return None

        value = cur[1].split("</Value>")[0].split("<Value>")[1]

        value = float(value.replace(",", "."))

        date = responses.headers["Date"]
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()

        return (value, date)

    else:
        return None


print((currency_rates("Usd")))
print((currency_rates("eUR")))

print((currency_rates("BRL")))
print((currency_rates("BGN")))
