# sugar_amount = 1print(f"Total gram of base tea is: {total_grams}")2
# print(f"initial sugar:{sugar_amount}")
# sugar_amount = 3
# print(f"initial sugar:{sugar_amount}")

# print(f"ID of 3: {id(3)}")
# print(f"ID of 12: {id(12)}")
spice_mix = set()
print(f"Initial spice mix ID: {id(spice_mix)}")
print(f"Initial spice mix : {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("cardemom")
print(f"after spice mix ID: {id(spice_mix)}")
print(f"after spice mix : {spice_mix}")

black_tea_grams = 16
ginger_grams = 5

total_grams = black_tea_grams + ginger_grams
print(f"Total gram of base tea is: {total_grams}")


remaining_grams = black_tea_grams - ginger_grams
print(f"Total gram of remaining tea is: {remaining_grams}")

milk_litre = 7
servings = 4
milk_per_serving = milk_litre/servings
print(f"milk per serving is: {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pots = total_tea_bags//pots
print(f"while tea bags per pot: {bags_per_pots}")

total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover c pods: {leftover_pods}")

base_flavor_strength = 3
scale_factor = 3
powerful_flavour = base_flavor_strength ** scale_factor
print(f"scaled flavoured strength: {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")

is_boiling = True
stri_count = 5
total_action = stri_count + is_boiling
print(f"Total action: {total_action}")

milk_present = 0 #no milk
print(f"Is there milk?:{bool(milk_present)}")

water_hot = True
tea_added = True

can_serve = water_hot and tea_added
print(f"can serve it?: {can_serve}")

import sys
from decimal import Decimal 

Ideal_temp = 95.5
current_temp = 95.49
print(f"Ideal temp: {Ideal_temp}")
print(f"current temp: {current_temp}")
print(f"difference temp: {Ideal_temp - current_temp}")

print(sys.float_info)




