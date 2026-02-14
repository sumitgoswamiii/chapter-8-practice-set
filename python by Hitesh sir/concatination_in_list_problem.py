base_liquid = ["water","milk"]
extra_flavour = ["ginger"]
full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea","water"]*3
print(f"strong brew: {strong_brew}")

raw_spice_data = bytearray(b"cinnamon")
raw_spice_data = raw_spice_data.replace(b"cardamom",b"cinnamon")
print(f"bytes: {raw_spice_data}")
