def main():
    fruit_calories = [
        {"name": "Apple", "calories": 130},
        {"name": "Avocado", "calories": 50},
        {"name": "Banana", "calories": 110},
        {"name": "Cantaloupe", "calories": 50},
        {"name": "Grapefruit", "calories": 60},
        {"name": "Grapes", "calories": 90},
        {"name": "Honeydew Melon", "calories": 50},
        {"name": "Kiwifruit", "calories": 90},
        {"name": "Lemon", "calories": 15},
        {"name": "Lime", "calories": 20},        
        {"name": "Nectarione", "calories": 60},
        {"name": "Orange", "calories": 80},
        {"name": "Peach", "calories": 60},
        {"name": "Pear", "calories": 100},
        {"name": "Pineapple", "calories": 50},
        {"name": "Plums", "calories": 70},
        {"name": "Strawberries", "calories": 50},
        {"name": "Sweet Cherries", "calories": 100},
        {"name": "Tangerine", "calories": 50},
        {"name": "Watermelon", "calories": 80}
    ]

    whatFruit = input("Item: ").strip().casefold()
    # whatFruit = "watermelon".strip().casefold()

    for fruit in fruit_calories:
        if (fruit["name"]).casefold() == whatFruit:
            print("Calories:", fruit["calories"])

    # Accessing the calorie count for a specific fruit
    # print("Calories:", next(item for item in fruit_calories if item["name"] == whatFruit)["calories"])

    # Iterating through the list and printing the fruit names and their calorie counts
    # for fruit in fruit_calories:
    #     print(f"{fruit['name']}: {fruit['calories']} calories")

main()    