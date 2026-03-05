value = 13

if remainder := value % 5:
    print(f"Not divisible,remainder is {remainder}")

available_sizes = ["small","medium","large"]
if(requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"serving {requested_size} chai")
else:
    print(f"size is unavalable - {requested_size}")

flavours = ["masala","ginger","lemon","mint"]
print("Available flavours: ",flavours)

while (flavour := input("Choose your flavour: ")) not in flavours:
    print(f"sorry, {flavour} is not available")

print(f"you choose {flavour} chai")