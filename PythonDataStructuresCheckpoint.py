# Create a list named 'shopping_list' to store the items.
shoppingList = []
uniqueItems = set()
our_store_items = {"Bread", "Milk", "Egg", "Water", "Wine", "Apple","Mango","Banana","Oil","Sugar"}


# Use a while loop to create a menu of options for the user to add, remove, or view items from the list.
while True:
        print("""Shopping List Menu \n
               1. Add item
               2. Remove items
               3. View items
               4. Exit""")
#  Use the input() function to prompt the user to make a selection from the menu.
        userInput = int(input("Select from the available options listed Above (1/2/3/4): \n"))

# Use an if-elif-else block to determine the user's selection and perform the corresponding action.
        if userInput == 1:
                print("Add Item Selected")

# If the user selects 'add', use the input() function to prompt the user to enter an item to add to the list. Use the range() function to limit the number of items that can be added to the list.
                for item in range(5):
                        print(our_store_items)
                        item = input("Enter Item you want to buy: ").capitalize()
                        if item == "Stop":
                                break
                        if item not in our_store_items:
                                print("Item  not available in our store")
                        if item in uniqueItems: 
                            print(f"{item} already exist in shopping Cart")
                        else:
                           shoppingList.append(item)
                           uniqueItems.add(item)
                           print(shoppingList)       
                           
# If the user selects 'remove', use the input() function to prompt the user to enter an item to remove from the list.
        
        elif userInput == 2:
              print("Remove Item from Shopping list")
              print("Current shopping list: ", shoppingList)

              for item in shoppingList:   
                    print(shoppingList) 

              while True:
                        item_to_remove = input("Enter the item you want to remove (or type 'stop' to finish): ").capitalize()
                        if item_to_remove == "Stop":
                           break   
                        if item_to_remove in shoppingList:
                           shoppingList.remove(item_to_remove)
                           uniqueItems.remove(item_to_remove)
                           print(f"Your Updated shopping list is: {shoppingList}") 
                        
                        else:
                           print(f"{item_to_remove} is not in shopping list") 
                        

# If the user selects 'view', use a for loop to iterate through the list of items and display them to the user.
        elif userInput == 3:
            print("View Items in Shopping List")
            if shoppingList:
                print("Your shopping list contains:")
                for item in shoppingList:
                      print(f"{item}")
            else:
                print("Shopping list is empty.")

# Exit Block
        elif userInput == 4:
                print("Exit Shopping Cart")
                break
        