
# pip install inflect
import sys
import inflect

def main():
    p = inflect.engine()
    names = []
    # names = ['apple', 'orange', 'guava', 'strawberry']
    # names = ['Liesl', 'Friedrich', 'Louisa', 'Kurt', 'Brigitta', 'Marta', 'Gretl']

    print("Enter names (press Ctrl+D to end):")
    try:
        while True:
            name = input().strip()
            if name:
                names.append(name)
    except EOFError:
        pass

    if names:
        name_length = len(names)
        # print("name_length : ", name_length)
        for i in range(name_length):
            subset_names = names[:i+1]
            # print(subset_names)
            # for name in subset_names:
            farewell_message = f"Adieu, adieu, to {p.join(subset_names)}"
            print(farewell_message)
    else:
        print("No names were entered.")

if __name__ == "__main__":
    main()
