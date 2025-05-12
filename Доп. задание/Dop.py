# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список

def my_count(l: list, item):
    count = 0
    for element in l:
        if element == item:
            count += 1
    return count
    
my_list = [1, 2, 3, 4, 5, 2, 2, 4, 6] #пример
print(my_count(my_list, 2)) 