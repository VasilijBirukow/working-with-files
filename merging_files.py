def merging_files(*files):
    try:
        result = []
        files_info = []
        lens_files = []
        for file in files:
            file_info = {}
            with open(file, encoding="utf-8") as file_1:
                text_file_1 = file_1.read()
            name_file = file.split("\\")[-1]
            len_file_1 = len(text_file_1.split("\n"))
            lens_files.append(len_file_1)
            file_info["name_file"] = name_file
            file_info["len_file_1"] = len_file_1
            file_info["text_file"] = text_file_1
            files_info.append(file_info)
        lens_files.sort()
        for len_file in lens_files:
            for file_info in files_info:
                if file_info["len_file_1"] == len_file:
                    result_past = file_info["name_file"] + "\n"
                    result_past += str(file_info["len_file_1"]) + "\n"
                    result_past += file_info["text_file"]
                    result.append(result_past)
                    break
        return  "\n".join(result)
    except FileNotFoundError:
        print("Файл не найден")















    


