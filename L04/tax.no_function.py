## tax.no_function.py

def get_inputs():
    return float(input("What is the price ")),\
        float(input("What is the tax rate? "))

def calculate_price_with_tax(price, tax):
    return price * (100 + tax) / 100

done = False
while not done:
    sentinel = str.upper(input(f"Enter Q for quit or any other key to compute tax "))
    if sentinel == "Q":
        done = True
        print(sentinel, done)
        continue
    else:
        print("Compute tax")
    price, tax = get_inputs()
    calculated_price = calculate_price_with_tax(price, tax)
    print(f"The calculated price is {calculated_price}")