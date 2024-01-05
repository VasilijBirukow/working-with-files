from cook_book import *
def get_shop_list_by_dishes(file_cook, dishes, person_count= int):
    cook_book = cook_file_read(file_cook)
    ingredients_info = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient["ingredient_name"]
                quantity = int(ingredient["quantity"]) * person_count
                measure = ingredient["measure"]
                ingredient_info = {}
                ingredient_info["quantity"] = quantity
                ingredient_info["measure"] = measure
                ingredients_info[ingredient_name] = ingredient_info
        else:
            print(f"Блюда {dish} нет в меню")
    return ingredients_info


