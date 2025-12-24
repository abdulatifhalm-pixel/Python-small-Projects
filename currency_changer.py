"""
Currency Changer (Currency Converter)
Author: Abdul Latif
Description: A simple console-based currency converter for GitHub projects.
"""

def currency_converter(amount, from_currency, to_currency):
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "AFN": 72.0,
        "PKR": 278.0,
        "INR": 83.0,
        "GBP": 0.79
    }

    if from_currency not in exchange_rates:
        return "Source currency not supported."

    if to_currency not in exchange_rates:
        return "Target currency not supported."

    usd_amount = amount
