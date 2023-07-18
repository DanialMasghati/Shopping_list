import os 
EXIT_COMMAND = ("quit", "q", "ex", "exit")
shopping_list = list()


def show_help() -> str:
    help_comment = "To exit the program, enter one of these commands: quit, q, ex, exit"
    return help_comment
def clear_screen():
    return os.system('cls' if os.name=='nt' else 'clear')
def product_list(shopping_list: list) -> str:
    item = ""
    for product in shopping_list:
        item += "➡ " + product + "\n"
    return item
def search(shopping_list:list(str),product:str)-> str:
    if product in shopping_list:
        search_exist="exist"
    else:
        search_exist="doesn't exist"

    return search_exist

def delete_item(shopping_list,product):
    if product in shopping_list:
        shopping_list.remove(product)
    else:
        product_exist="this product doesn't exist"
        return product_exist
def add_to_list(shopping_list: list,product:str):
    shopping_list.append(product)
    check=f"Item added: {product},Item count: {len(shopping_list)}"
    return check

while True:
    # clear_screen()
    product = input("Enter your product? ")
    product = product.lower()
    if product in EXIT_COMMAND:
        print(product_list(shopping_list))
        break
    elif product == "help":
        clear_screen()
        print(show_help())
    elif product == "remove":
        product=input("please enter your product for delete them :\n")
        delete_item(shopping_list,product)
    elif product == "show":
        print(product_list(shopping_list))
    elif product=="search":
        product=input("please enter your product for search them :\n")
        print(search(shopping_list,product))
    elif product in shopping_list:
        input("that item is exist now , please change it,  please press enter")
    # elif product=="cls":
    #     clear_screen()
    else:
        print(add_to_list(shopping_list,product))