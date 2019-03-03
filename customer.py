'''
    This python contain all programs related to coustomer information and the
    invoice details.
'''
import os
import time

#saves the all customer and sales info in customerInfo.txt
def generateInvoice(customer,productName,discountedAmount,totalAmount):

    #calculate lines in the customer file each line no is unique and
    #represnts the sales
    line = 0
    fh = open('customerInfo.txt','r')
    for lines in fh:
        line += 1
    newline = line + 1 # This will be newline no i.e. new customer id
    fh.close()
    dateTime = str(time.asctime( time.localtime(time.time()) )) #get the local date and time
    fh = open('customerInfo.txt','a')
    temp = str(newline) +','+customer+','+productName+','+str(discountedAmount)+','+\
            str(totalAmount)+','+ dateTime + os.linesep
    fh.write(temp)
    fh.close()
    print("The invoice for this sales is:")
    print("Sales ID : " + str(newline))
    print("Customer Name : " + customer)
    print("Product Name : " + productName)
    print("discountedAmount : $" + str(discountedAmount))
    print("Total Amount: $" + str(totalAmount))
    print("Date and Time : " + dateTime +'\n')
#displays customerInfo
def getCustomerInfo():
    fh = open('customerInfo.txt','r')
    print(fh.read())
    fh.close()
