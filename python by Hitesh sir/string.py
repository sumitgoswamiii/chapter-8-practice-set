chai_type = "Ginger tea"
customer_name = "sumit"
print(f"Order for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and bold "
print(f"first word: {chai_description[0:8:2]}")
print(f"last word: {chai_description[13:17]}")
print(f"last word: {chai_description[::-1]}")

label_text = "chai special"
encoded_label = label_text.encode("utf-8")
print(f"Non encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"decoded_label: {decoded_label}")

