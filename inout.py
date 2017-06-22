while True:
    
    try:
        t = input("How many avocado toasts do you eat per week? ")
    except EOFError:
        sys.exit(0)

    try:
        avocado = float(t)
    except ValueError:
        print("Sorry, ", t, " is not a number.")
        avocado = 1.0
        print("I'll assume you eat ", avocado, " avocado toasts per week.", sep = "")

    try:
        c = input("How much does an avocado toast cost on average in your area? (Do not type currency.) ")
    except EOFError:
        sys.exit(0)

    try:
        cost = float(c)
    except ValueError:
        print("Sorry, ", c, " is not an amount.")
        cost = 19.00
        print("I'll assume an avocado toast costs $", cost, ".", sep = "")

    downpay = 750000 * 0.2
    annual = avocado * 52 * cost
    years = downpay // annual
    months = ((downpay / annual) - (downpay // annual)) * 12

    print("At this rate, you will be able to save a 20% down payment on a $750,000 (median price) home in Brooklyn if you cut out all avocado toasts for ", int(years), " years and ", int(months), " months.")
      
    print ()
