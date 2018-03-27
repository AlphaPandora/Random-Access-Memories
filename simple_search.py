# Program for Simple search with List as an input

def LinSearch(myList, item):
    print("Entered List is: ", myList)
    if item in myList:
        print("Item found!!!& guess what..? it's at location: ",myList.index(item))
    else:
        print("No Luck!!@")


my = input("Enter elements: ")
myList = my.split(',')
item = input("Enter item to find: ")
LinSearch(myList, item)
