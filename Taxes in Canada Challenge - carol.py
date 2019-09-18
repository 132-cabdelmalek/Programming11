totalPurchase = input("Entre the amount of your total purchase : $")
country = input("What country are you from? :")
if country == "Canada" :
    province = input("Which province are you currently in? :")
    if province == "Alberta":
        SalesTaxes = (float(totalPurchase))*0.05
        TotalCost = (float(totalPurchase)) *1.05
        
    if province == "Ontario":
        SalesTaxes = (float(totalPurchase))*0.13
        TotalCost = (float(totalPurchase))*1.13
        
    else:
        SalesTaxes = (float(totalPurchase))*0.11
        TotalCost = (float(totalPurchase))*1.11

if country != "Canada":
    SalesTaxes = (float(totalPurchase))*0
    TotalCost = float(totalPurchase)

print("The sames taxes of the items is {0:.2f}".format(SalesTaxes))
print("The total cost of the items is {0:.2f}".format(TotalCost))
    
