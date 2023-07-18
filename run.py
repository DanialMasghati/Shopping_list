exit_command = ("quit", "q", "ex", "exit")
remove_command = ("remove",)
shopping_list = []

while True:
    product = input("Enter your product? ")
    product = product.lower()
    if product in exit_command:
        break
    # print(f"your product is {product}")
    shopping_list.append(product)
    # print(shopping_list)
    elif product in remove_command:
        item = input("Please enter an item to remove from your shopping list: ")
        if item in shopping_list:
        shopping_list=shopping_list.remove(item)
        else:
        print("Item not found in shopping list.")
# print("Your shopping list:")
# for product in shopping_list:
#     print("--->" + product)
