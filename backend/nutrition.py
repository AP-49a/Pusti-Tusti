food_db = {
    "rice": {
        "calories": 200,
        "protein": 4
    },
    "egg": {
        "calories": 70,
        "protein": 6
    },
    "banana": {
        "calories": 90,
        "protein": 1
    },
    "dal": {
        "calories": 120,
        "protein": 7
    }
}


def calculate_nutrition(food_list):
    total_calories = 0
    total_protein = 0

    for food in food_list:
        if food in food_db:
            total_calories += food_db[food]["calories"]
            total_protein += food_db[food]["protein"]

    return {
        "calories": total_calories,
        "protein": total_protein
    }