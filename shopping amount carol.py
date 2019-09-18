totalPurchase = input("please entre the amount for your total purchase today : $")
if float(totalPurchase) < 50 :
    CostWShip = (float(totalPurchase)) +10
    print("that will be an extra $10 for shipping.\nIncluding shipping fees, your total comes up to {0:.2f}".format(CostWShip))
else:
    totalPurchase = (float(totalPurchase))
    print("No shipping costs today!\nYou have to pay {0:.2f}".format(totalPurchase))
