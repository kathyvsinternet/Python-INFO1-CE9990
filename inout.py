"""
inout.py

Calculate the number of years one must be without avocado toast in order to afford the down payment for a $750,000 home.
"""
import sys

while True:
    
    print("In order to afford a 20% down payment for a home in Brooklyn at the median sale price of $750,000, how many avocado toasts will you, A Millenial, need to give up? For how many years?")

    print()

    try:
        t = input("How many avocado toasts do you eat per week? ")
    except EOFError:
        sys.exit(0)

    try:
        avocado = float(t)
    except ValueError:
        print("Sorry, ", t, " is not a number.")
        avocado = 1.0
        print("I'll assume you eat", avocado, "avocado toasts per week.")

    try:
        c = input("How much does an avocado toast cost on average in your area? $")
    except EOFError:
        sys.exit(0)

    try:
        cost = float(c)
    except ValueError:
        print("Sorry,", c, "is not an amount.")
        cost = 19.00
        print("I'll assume an avocado toast costs $", cost, ".")

    downpay = 750000 * 0.2 # calculates down payment of $150,000
    annual = avocado * 52 * cost # calculates cost of t weekly avocado toasts per year
    years = downpay // annual # calculates truncated number of years to get to down payment
    months = ((downpay % annual) / annual) * 12 # calculates number of months from truncated remainder
    toasts = downpay / cost

    print("At this rate, you will be able to save enough for a down payment if you cut out", int(toasts), "avocado toasts. This will take you", int(years), "years and", int(months), "months.")
    print("Good luck!")
      
    print ()

exit(0)
