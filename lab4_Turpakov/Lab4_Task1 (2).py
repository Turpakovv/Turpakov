# TODO решите задачу
import json
def goal() -> float:
    sum_of_items = 0
    with open("input.json", "r") as f:
        data = json.load(f)
        for item in data:
            sum_of_items += item["score"] * item["weight"]
    return round(sum_of_items, 3)


print(goal())
