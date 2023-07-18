EXIT_COMMAND = ("quit", "q", "ex", "exit")
shopping_list = list()
while True:
    product = input("Enter your product? ")
    product = product.lower()
    if product in EXIT_COMMAND:
        print("Your final shopping list:")
        for product in shopping_list:
            print("➡  " + product)
        break

    else:
        shopping_list.append(product)
        print("Your shopping list:")
        for product in shopping_list:
            print("➡  " + product)
