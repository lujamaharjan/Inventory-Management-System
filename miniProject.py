'''
This is the simple console app for electronic appliances shop.
for managing the stock and the save customer information.
Date: 2075/11/18
Author:Sachin Maharjan
'''
import pyfiglet
import stock as stk
import customer as cus

def main():
    #for welcoming user when opening this app for first time.

    store = pyfiglet.figlet_format("Sachin Electro")
    print(store)

    #main Driver part
    while(True):

        print("\n__________________")
        print("*******MENU*******")
        print("__________________")
        print("1 : watching stock")
        print("2 : selling the product")
        print("3 : Watching customer information")
        print("e : exiting from the app")

        choice = input("Enter your Choice:")
        if(choice == '1'):
            stk.showStock()

        elif(choice == '2'):
            #sell()
            print("choice2")
            #stk.decreaseStock('macbook',1)
            #stk.increaseStockInExisting('macbook',5)
            #stk.newProductAdd('intel',5,500)
        elif(choice == '3'):
            #showCustomerInfo()
            print("choice3")
            cus.generateInvoice('ram','intel',3,83)
        elif(choice == 'e' or 'E'):
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
