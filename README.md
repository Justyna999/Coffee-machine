# Coffee-machine

This is a program that simulates a coffee machine, allowing users to choose from a menu of drinks and pay for them using coins. The program checks whether there are enough resources to make the requested drink, processes the payment, and dispenses the drink if the transaction is successful.

# Display
    What would you like? (espresso press 1 / latte press 2 / cappuccino press 3):

If there are not enough resources to make the requested drink, the program will display an error message:

    Sorry there is not enough ingredients.
    
After choosing a drink, the program will ask for payment in the form of coins. You can insert coins by typing the number of coins and pressing enter. 
The program will keep track of the amount paid so far and display the remaining debt.

    cost of {drink_name} : {drink_cost} $. Please insert coins.
    How many quarters (0.25$)?:
    Payed so far: {total}$
    Remaining debt: {debt}$

If you have inserted enough coins to pay for the drink, the program will dispense the drink and return any change:

    Here is ${change} in change.
    here is your {drink_name}. Enjoy!
    
If you have not inserted enough coins, the program will display an error message and refund your money:

    Sorry that's not enough money. Money refunded.
    
You can also check the current status of the resources by typing "report" at the menu prompt.    
The program will display the current amount of water, milk, coffee, and money in the machine.

Customization - My modifications 

This project is based on Dr. Angela Yu's project that appears in the "100 Days of Code: The Complete Python Pro Bootcamp" course. 
I have made some modifications to enhance the user experience.

modifications: 
• Modified the "printer_makes_brr" function to calculate the remaining debt and inserted coins.
• Changed the input values to improve usability. Previously, the user had to type "espresso" to order an espresso, but now they can simply type "1".
• Made other minor changes to improve the overall user experience.

Credits
This program was written by Dr. Angela Yu and Justyna Neblik. Feel free to use and modify it for your own purposes.
