def print_order(name,chai_type):
    print(f"{name} ordered {chai_type} chai!")

print_order("Aman","masala")
print_order("sumit","lemon")
print_order("rohan","tulsi")

# problem 1
def fetch_sales():
    print("Fetching the sales data")

def filter_valid_scales():
    print("Filtering valid scales data")

def summarize_data():
    print("summarizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_scales()
    summarize_data()
    print("report is ready")

generate_report()

#problem 2
def get_input():
    print("Getting user input")

def validate_input():
    print("validating the user info")

def save_to_db():
    print("saving to database")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("user registration complete")

register_user()

#problem 3
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(4,30)
print(my_bill)
print("orrder for table no 3: ",calculate_bill(2,12))

#problem 4
def add_vat(price, vat_rate):
    return price *(100 + vat_rate)/100

order = [100, 150, 200, 250]
for price in order:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}") 

