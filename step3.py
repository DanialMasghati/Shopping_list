EXIT_COMMAND = ("quit", "q", "ex", "exit")

while True:
    product = input("Enter your product? ")
    product = product.lower()
    if product in EXIT_COMMAND:
        break
    print(f"your product is {product}")
