masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3,) = masala_spices

print(f"main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio =2,1
print(f"Ratio of G: {ginger_ratio} and c:{cardamom_ratio}")
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio of G: {ginger_ratio} and c:{cardamom_ratio}")
#membership
print(f"is cinnamon in masala spices?{'cinnamon' in masala_spices}")

