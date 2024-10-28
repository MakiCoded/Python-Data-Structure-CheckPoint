**Shopping List Program**

This program provides an interactive shopping list management system where users can add, remove, view, or exit the shopping list. It uses a command-line menu to navigate through these options, allowing users to create a custom list of items they wish to purchase from a predefined store inventory.

**Features**

Add Item: Users can add items from a store's inventory to their shopping list. The program ensures that no duplicate items are added to the list.
Remove Item: Users can remove items from their shopping list.
View Items: Users can view all items currently in their shopping list.
Exit: Allows users to exit the program.
Code Structure
The program's core structure is organized within a while loop that continually prompts users with a menu of options until they decide to exit.

**Variables and Data Structures**

shoppingList: A list to store the items added by the user.
uniqueItems: A set used to keep track of unique items in the shopping list to prevent duplicates.
our_store_items: A set containing items available for purchase in the store.
Menu Options
The program provides a menu that includes the following options:

**Add Item**

The user is prompted to enter an item to add to the list.
Only items available in our_store_items can be added.
If an item is already in the list, the program notifies the user.
The user can add up to 5 items at a time.

**Remove Item**

The user can view the current list and choose items to remove.
Users can type "stop" to end the removal process.
If an item is not found in the shopping list, the user is notified.

**View Items**

Displays all items currently in the shopping list.
If the list is empty, a message is shown.
**Exit**

The program terminates when the user selects the "Exit" option.
Example Usage
When the program starts, a menu will appear with options to add, remove, view, or exit.
Selecting an option prompts the user for input to perform the desired action.
