I = ["water","milk","black tea"]
I.append("sugar")
print(f"I are: {I}")
I.remove("water")
print(f"I are: {I}")
print(I)

spice_option = ["ginger","cardamom"]
chai_ingredients = ["water","milk"]
chai_ingredients.extend(spice_option)
chai_ingredients.insert(2,"black tea")
chai_ingredients.pop()
print(f"chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")

sugar_level = [1, 2, 3, 4, 5]
print(f"maximum sugar level: {max(sugar_level)}")
print(f"minimum sugar level: {min(sugar_level)}")

