from currency_symbols import CurrencySymbols
import requests
class currency():
    def __init__(self, name):
        self.name=name
    def intro(self):
        print("Hello, " +self.name+ ". Welcome to the currency convertor, which helps you convert between the top currencies in the world.")
    def currencies():
        starting= input("Which currency would you like to convert from? Please enter the 3 letter abbreviation. ")
        ending=input("Which currency would you like to convert to? Please enter the 3 letter abbreviation. ")
        initialValue=float(input("How much of your currency would you like to convert? Please enter a numerical value."))
        currency.conversion(starting, ending, initialValue)
    def conversion (starting, ending, initialValue):
        response=requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=002065b9199a7dae435f9b362d5af6c9")
        wholeList=response.json()
        ratesList=wholeList['rates']
        numericalStartingCurrency= ratesList[starting]
        numericalEndingCurrency= ratesList[ending]
        currencySymbol=CurrencySymbols.get_symbol(ending)
        finalCurrency=initialValue/numericalStartingCurrency*numericalEndingCurrency
        roundedVersion=round (finalCurrency, 2)
        print("final currency: ", currencySymbol, roundedVersion)
                
user=currency(input("Enter your name. "))
user.intro()
currency.currencies()