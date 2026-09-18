# Available Inventory: Item Name -> Unit Price
catalog = {
    'laptop':800, 
    'mouse':200, 
    'keyboard':50, 
    'monitor':150
}

grand_total = 0
while True:
    data = input('Enter an item to add to order, or type "checkout" to finish, or type "exit" to cancel\n').lower()
   
    if data == "exit":
        break
    elif data in catalog:
        grand_total += catalog[data]
        print(f"--> Added {data} (${catalog[data]}) to order.")
    else:
        print("--> [ERROR] item not found in catalog. Try again.")


#    This code only runs when user enters "checkout"
    if data == "checkout":
        if grand_total > 499:
            discount = grand_total * 0.10
        elif grand_total > 199:
            discount = grand_total * 0.05
        else:
            discount = 0

        final_total = grand_total - discount

        print(f"CHECKOUT RECEIPT\n{'='*20}\nSubtotal: {grand_total}\nDiscount: {discount}\nFinal Total: {final_total}\n{'='*20}")
        break