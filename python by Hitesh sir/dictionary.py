chai_order = dict(type = "masala chai", size = "large", sugar = 2)
print(f"chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"recipe base: {chai_recipe['base']}")
print(f"recipe:{chai_recipe}")
del chai_recipe["liquid"]
print(f"chai recipe: {chai_recipe}")

# membership testing
print(f"is sugar in chai order: {'sugar' in chai_order}")

chai_type = {"type":"ginger chai", "size":"medium", "sugar": 1}

print(f"order details (keys): {chai_type.keys()}")
print(f"order details (values): {chai_type.values()}")
print(f"order details (items): {chai_type.items()}")
last_item = chai_type.popitem()
print(last_item)
print(chai_type)

