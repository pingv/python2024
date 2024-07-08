def main():

    grocery_list = {}
    collect_grocerylist(grocery_list)
    print_grocerylist(grocery_list)

def collect_grocerylist(grocery_list):

    while True:
        try:
            item = input("").strip().lower()

            if item:
                grocery_list[item] = grocery_list.get(item, 0) + 1

        except (KeyboardInterrupt, EOFError):
            break

def print_grocerylist(grocery_list):
    print("")
    for item, count in sorted(grocery_list.items()):
        print(f"{count} {item.upper()}")

main()
