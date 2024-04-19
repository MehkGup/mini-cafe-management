print("Welcome to our resturant , here's the menu ")
print(" Pizza: Rs 40","\n","Pasta: Rs 50","\n","Burger: Rs 60","\n","Salad: Rs 70","\n","coffee: Rs 80","\n","tea: Rs 15")
menu={"pizza": 40, "Pasta": 50 ,"Burger": 60,"Salad": 70, "coffee": 80,"tea":15}
order_item =0
item_1=input("Enter your first item you want to order =")
if item_1 in menu:
    order_item = order_item + menu[item_1]
    print(f"order of {item_1} has been placed")

else:
    print(f"ordered item {item_1} is not available yet")

another_item = input("Do you want to add another item ? (Yes/No)")
if another_item =='Yes' or 'yes':
    item_2 = input("Enter your second item =")
    if item_2 in menu:
        order_item = order_item +menu[item_2]
        print(f"order of {item_2} has been placed")
    else:
        print(f"ordered item {item_2} is not available yet")

print(f"The  total amount of ordered item {order_item}")