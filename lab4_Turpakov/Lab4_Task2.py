# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(file="input.csv") -> None:
    ...  # TODO считать содержимое csv файла
    csvfile = open(file)
    read = csv.DictReader(csvfile, delimiter=",", lineterminator="\n")
    data = list(read)
    ...  # TODO Сериализовать в файл с отступами равными 4
    with open("result.json", mode="w") as json_file:
        json.dump(data, json_file, indent=4)
    return None

if __name__ == '__main__':
    # Необходимо для выполнения проверки
    task()

    with open("result.json") as output_f:
        for line in output_f:
            print(line, end="")