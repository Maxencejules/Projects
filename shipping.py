weight = 41.5
# Ground Shipping
if weight <= 2:
    cost = weight * 1.50 + 20.00
if weight <= 6:
    cost = weight * 3.00 + 20.00
if weight <= 10:
    cost = weight * 4.00 + 20.00 
else:
    cost = weight * 4.75 + 20.00
print(cost)
# Premium Ground Shipping
cost_ground_premium = 125.00
print("Ground Shipping Premium $", cost_ground_premium)
# Drone Shipping
if weight <= 2:
    cost = weight * 4.50 
elif weight <= 6:
    cost = weight * 9.00
elif weight <= 10:
    cost = weight * 12.00 
else:
    cost = weight * 14.75
print(cost)
