def main():

    menu_items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
        "Biriyani": 24.55,
        "Kabob": 33.68,
    }
    orderValue = takeOrder(menu_items)
    # print("Total: $",orderValue, sep='')
    # print("Total: ${:,.2f}".format(orderValue))


def takeOrder(menu_items):

    orderTotal = 0.00

    while True:
        try:
            item = input("Item: ").strip().title()
            # print("Item is : ", item)

            # Getting the value of a key
            price = menu_items.get(item)
            if price is None:
                continue
            orderTotal = orderTotal + price
            # print("price : ", price)
            print("Total: ${:,.2f}".format(orderTotal))
            continue

        except EOFError:
            break
        except KeyError:
            continue
        except ValueError:
            # print("Either X or Y not an integer")
            continue
        except ZeroDivisionError:
            # print("Y must be > than ZERO.")
            continue
        else:
            break
    
    # print("well:  ", orderTotal)
    return orderTotal


main()
