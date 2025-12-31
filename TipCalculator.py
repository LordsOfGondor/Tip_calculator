#This is my first project to buld a tip calculator.

Dinner = "thanks for dinning at gondor cafe" #the name of the dinner.

Customers = 2 #the number of customers seated in the cafe

meal_1 = "1 burger with fries" #the meal one of the customers ordered

meal_2 = "pancakes with eggs" #the meal the other customer ordered

burger_cost = 10.00 # the price of the burger meal

pancakes_cost = 12.50 #the pancake meal

mealdone = "thanks for dinning with us, here's your bill." #the patron thanking the customers and handing them the bill

bill = burger_cost + pancakes_cost #the total cost of both meals

Tip_amount = float(input("enter your tip amount (e.g., 5, 10, 15):")) #enter how much you want to tip

Total_bill = bill + Tip_amount #the total amount of the bill with the tip included

print(f"total bill: {Total_bill} ") #print of the bill

print(" thank you come again") #thank the customer
