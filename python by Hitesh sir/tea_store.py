order_amount = int(input("Enter the order amount: "))
# if(order_amount > 300):
#     print("delivery is free")    
# else:
#     print("delivery charge is 30 rupees")

# another way to do that problem
delivery_fees = 0 if order_amount >300 else 30
print(f"delivery charge is: {delivery_fees}")