def cook_file_read(cook_file):
    cook_book = {}
    with open(cook_file, encoding="utf-8") as file:
        all_text_file = file.read()
        all_past_list = all_text_file.split("\n\n")
        for past in all_past_list:
            past_lists = past.split("\n")
            dish_name = past_lists[0]
            dish_list = []
            for ind, line in enumerate(past_lists):
                if ind > 1 and ind != -1:
                    line_list = line.split("|")
                    ingredient_name = line_list[0]
                    quantity = line_list[1]
                    measure = line_list[2]
                    ingredient = {"ingredient_name" : ingredient_name, "quantity" : quantity, "measure" : measure}
                    dish_list.append(ingredient)
            cook_book[dish_name] = dish_list
    return cook_book


























