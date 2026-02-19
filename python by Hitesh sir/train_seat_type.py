seat_type = input("Enter your seat type(sleeper/AC/general/luxury): ")

match seat_type:
    case "sleeper":
        print("sleeper- No AC, beds available")
    case "AC":
        print("AC- Air conditioned,comfy ride")
    case "general":
        print("General-cheapest option,no reservation")
    case "luxury":
        print("Luxury-premium seats with meals")
    case _:
        print("Invalid seat type")