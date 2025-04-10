# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):
    member1 = set(group1.split(separator))
    member2 = set(group2.split(separator))
    identical = sorted(member1.intersection(member2))
    return identical


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

identical = find_common_participants(participants_first_group, participants_second_group, separator='|')

print("Общие участники:", identical)
