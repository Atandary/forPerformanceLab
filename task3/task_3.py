import json

path_to_tests = input("Введите путь к tests: ")
path_to_values = input("Введите путь к values: ")
path_to_report = input("Введите путь к report: ")

def load_json(file_path):
    with open(file_path, "r", encoding = "utf-8") as file:
        data = file.read()
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            print(f"Проверьте содержимое JSON файла")

def save_json(filename, data):
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)
                  
tests_json = load_json(path_to_tests)
value_json = load_json(path_to_values)
report_json = load_json(path_to_report)
tests_temp = tests_json["tests"][0]
value_temp = value_json["values"][0]
save_json(path_to_report, tests_json["tests"])
report_json = load_json(path_to_report)

def update():
    dict2 = {item["id"]: item for item in value_json["values"]}
    for item in report_json:
        if item["id"] in dict2:
            item["value"] = dict2[item["id"]]["value"]

update()

save_json(path_to_report, report_json)