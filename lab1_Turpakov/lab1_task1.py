numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

a = -99
summa = 0
average = 0
leng = len(numbers)

for i in range(0,leng):
    if numbers[i] != None:
        summa += numbers[i]
    else:
        a = i
average = summa/(leng)
numbers[a] = average

print("Измененный список:", numbers)
