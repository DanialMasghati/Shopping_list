EXIT_COMMAND = ("quit", "q", "ex", "exit")
shopping_list = []
while True:
    product = input("Enter your product? ")
    product = product.lower()
    if product in EXIT_COMMAND:
        break
    else:
        shopping_list.append(product)
        print(f"your shopping_list is {shopping_list}")
