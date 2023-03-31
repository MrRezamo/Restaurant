# Restaurant
Turing Collage Problem Set

## README
This code is a Python script that simulates a basic ordering system for a restaurant menu. The menu is defined as a dictionary containing the item names and their respective prices. The user is prompted to input their order, and the code checks if the order is in the menu. If it is, the code adds the price of the item to a running total and displays the cost of the item and the total cost of the order. If the user inputs an item that is not in the menu, the code displays a message saying that the restaurant is "fresh out of elephant today".

The code continues to ask for orders until the user inputs an empty string, at which point the code breaks out of the loop and displays the total cost of the order.

## Usage
To use this code, save it to a file with a .py extension and run it using a Python interpreter. The code will prompt the user to enter their order. The user should enter the name of the item they want to order. If the item is on the menu, the code will display the cost of the item and the total cost of the order so far. If the item is not on the menu, the code will display an error message. To exit the ordering system, the user should enter an empty string. The code will then display the total cost of the order.

## Modification
This code can be easily modified to add new items to the menu by editing the Menu dictionary. Simply add a new key-value pair to the dictionary with the name of the item as the key and the price of the item as the value.

The code can also be modified to include additional functionality, such as the ability to display a receipt or calculate tax and tip.
