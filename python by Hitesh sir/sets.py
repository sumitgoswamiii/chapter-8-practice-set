essential_spices = {"cardamom","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices | optional_spices
print(f"all spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

only_essential = essential_spices - optional_spices
print(f"only essential: {only_essential}")
#membership testing
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")