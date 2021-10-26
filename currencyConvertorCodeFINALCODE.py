#Kierstin Havens Programming Projects (1)
#Main Code. All comments correspond with the coding statements below them

# These import the required dictionaries in order for the program to format and run properly
from currency_symbols import CurrencySymbols
import requests
import sys
cont=1
#This is the main portion of the program. The class creates the object "currency" as well as greets the user
class currency():
    #creates and stores the user's name as a "currency object"
    def __init__(self, name):
        self.name=name
    #greets the user using their name
    def intro(self):
        print("Hello, " +self.name+ ". Welcome to the currency convertor, which helps you convert between the top currencies in the world.")
    #obtains all the required info (starting and ending currencies and initial value) from the user in order to run and stores this info in their respected variables
    def currencies():
        #The If statements following each variable assignment ensure that the user properly enters the correct values in order for the program to run correctly.
        starting= input("Which currency would you like to convert from? Please enter the 3 letter abbreviation. ")
        if len(starting)>3 or len(starting)<1:
            print("Please try again. Enter the three-character abbreviation for your currency.")
            sys.exit()
        else:
            print("Input saved.")
        ending=input("Which currency would you like to convert to? Please enter the 3 letter abbreviation. ")
        if len(ending)>3 or len(ending)<1:
            print("Please try again. Enter the three-character abbreviation for your currency.")
            sys.exit()
        else:
            print("Input saved.")
        initialValue=float(input("How much of your currency would you like to convert? Please enter a numerical value."))
        if initialValue<=0:
            print("Please try again. Enter a numerical value over 0.")
            sys.exit()
        else:
            print("Input saved.")
        #this prompt calls the conversion function and sends it the parameters necessary in order for the function to run
        currency.conversion(starting, ending, initialValue)
    #this function converts the values given by the user into the appropriate currency using a data API request
    #this function also formats the output with the proper symbol corresponding to the ending currency
    def conversion (starting, ending, initialValue):
        #obtains the live exchange rates from the data API
        response=requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=002065b9199a7dae435f9b362d5af6c9")
        #stores this response in a list
        wholeList=response.json()
        #breaks down the list to just store solely the exchange rates in a list
        ratesList=wholeList['rates']
        #The following 3 lines find the numerical data stored in the list  and set them equal to a variable
        numericalStartingCurrency= ratesList[starting]
        numericalEndingCurrency= ratesList[ending]
        #This request attains the proper symbol associated with the currency the user chose to convert to 
        currencySymbol=CurrencySymbols.get_symbol(ending)
        #performs dimensional analysis in order to convert from beginning currency, to Euros, to ending currency and sets equal to variable
        finalCurrency=initialValue/numericalStartingCurrency*numericalEndingCurrency
        #rounds the final solution to two decimal places
        roundedVersion=round (finalCurrency, 2)
        #prints the final currecny value as well as corresponding symbol
        print("Final Currency: ", currencySymbol, roundedVersion)
#calls the initializing function of the class "currency"               
user=currency(input("Enter your name. "))
#calls the intro function
user.intro()
#runs the main program function and allows the user to repeat the conversion process if they choose
while cont==True:
    #calls the currencies function in order to get the required info from the user and begin the exchange computation
    currency.currencies()
    repeat=input("Would you like to use the currency convertor again? Type 'y' for yes and 'n' for no.")
    if repeat=="n":
        print("Thanks for using my currency convertor! See you soon!")
        cont=0