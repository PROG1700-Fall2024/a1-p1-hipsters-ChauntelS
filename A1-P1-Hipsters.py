#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Title
    print("Hipster's Local Vinyl Records ""\nPurchase Invoice Record")
    #instruction message
    print("Please fill in the required fields below.")

    #known variables
    KilometerPrice = 15
    TaxPrice = 0.14

    #User input variables
    RecoredPrice = float(input("Enter Record Sale Price:"))
    KilometerAmount = float(input("Enter Distance in Kilometers:"))
    CustomerName = input("Enter Customer's Name:")

    #math
    DeliveryPrice = float(KilometerPrice)*(KilometerAmount)
    TaxAmount = float(RecoredPrice)*(TaxPrice)
    RecoredTotal = float(RecoredPrice)+(TaxAmount)
    TotalAmount = (float(RecoredTotal)+(DeliveryPrice))

    #Outcome Summary with customer's name
    print("Order Details for Customer:",end="")
    print(CustomerName)
    #print(DeliveryPrice)
    print('Delivery Total:${0:.2f}'.format (DeliveryPrice)) 
    #print(RecoredTotal)
    print('Order Total:${0:.2f}'.format(RecoredTotal)) 
    #Complete order total
    print('Order Total including Delivery:${0:.2f}'.format(TotalAmount))   #<-- took me a while to remember how to get only 2 place holders after the decimal
    # YOUR CODE ENDS HERE

main()