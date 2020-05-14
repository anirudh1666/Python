class Items:

    def __init__(self, name=None, barcode=None, price=None):

        self.name = name
        self.barcode = barcode
        self.price price



def display_menu():

    print("1) Search for item.")
    print("2) Add item.")
    print("3) Delete item.")
    print("4) Quit.")


def take_input():

    option = -1
    while option < 0 or option > 4:
        option = input("Enter your choice here: ")

    return option

def search_for_item():
    # TODO

def add_item():
    # TODO

def delete_item():
    # TODO


print("This is an inventory program. Made by Yuwei Zhu")
print()

user_option = -1
while user_option != 4:
    display_menu()
    user_option = take_input()

    if user_option == 1:
        search_for_item()
    elif user_option == 2:
        add_item()
    elif user_option == 3:
        delete_item()
    else:
        continue

    

