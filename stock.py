
'''
    This file contain all the activities
    related to stocks.txt fileself.
    This contain major two activities.
    1) Reading a stocks.txt file
    2) Modefying a stocks.txt file
        - Decreasing the stock when purchase
        - adding product and increasing the stock
'''
import os

# This function shows the entire stock
def showStock():
    fh = open("stocks.txt",'r')
    for line in fh:
        print(line,end=' ')
    fh.close()

# This function decrease the stock of sold product
def decreaseStock(stockName,quantity):
    arr = list()
    fh = open("stocks.txt",'r')
    fhl = open('temp.txt','r+')

    # Line by line split the content i.e product_name, stock and price_per_unit
    # search the line where stockName exits and decrese the stock of that line
    # and copy all new updates in temp.txt file
    for lines in fh:
        arr = lines.split(',')
        arr[1] = int(arr[1])
        arr[2] = int(arr[2])
        if arr[0].lower() == stockName.lower():
            if quantity <= arr[1]:
                arr[1] = arr[1] - quantity
            else:
                print("Not Enough Stock!")
        fhl.write(arr[0] + ',' + str(arr[1]) + ',' + str(arr[2]) + os.linesep)
    fh.close()
    fhl.close()

    #copy the content of temp.txt to stocks.txt
    file = open('temp.txt','r')
    fh = open('stocks.txt','w')
    fh.write(file.read())
    file.close()
    fh.close()
    # clearing the temp.txt
    file = open('temp.txt','w')
    file.write('')
    file.close()
    print("Stock deducted sucessfully!")

def newProductAdd(productName,stock,pricePerUnit):
    fh = open('stocks.txt','a')
    fh.write(productName + ',' + str(stock) + ',' + str(pricePerUnit) + os.linesep)
    fh.close()
    print("New product Added sucessfully!")

def increaseStockInExisting(productName,newStock):
    arr = list()
    fh = open("stocks.txt",'r')
    fhl = open('temp.txt','r+')

    # Line by line split the content i.e product_name, stock and price_per_unit
    # search the line where stockName exits and add the stock of that line
    # and copy all new updates in temp.txt file
    for lines in fh:
        arr = lines.split(',')
        arr[1] = int(arr[1])
        arr[2] = int(arr[2])
        if arr[0].lower() == productName.lower():
                arr[1] = arr[1] + newStock
        fhl.write(arr[0] + ',' + str(arr[1]) + ',' + str(arr[2]) + os.linesep)
    fh.close()
    fhl.close()

    #copy the content of temp.txt to stocks.txt
    file = open('temp.txt','r')
    fh = open('stocks.txt','w')
    fh.write(file.read())
    file.close()
    fh.close()
    # clearing the temp.txt
    file = open('temp.txt','w')
    file.write('')
    file.close()
    print("Stock added sucessfully!")

def getPrice(productName):
    arr = list()
    price = 0
    fh = open("stocks.txt",'r')
    for lines in fh:
        arr = lines.split(',')
        arr[2] = int(arr[2])
        if arr[0].lower() == productName.lower():
            price = arr[2]
            break
    return price
