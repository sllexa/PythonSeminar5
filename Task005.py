# задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:* 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7] 
# [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]
min_el = 0

def check_list(lst):
    global min_el
    n_list = []
    for i in range(0, len(lst)):
        if min_el + 1 == lst[i]:
            n_list.append(lst[i])
            min_el += 1
    return n_list


def max_sequence(source) -> list:
    global min_el
    new_list = []
    min_el = min(source)
    new_list.append(min_el)
    for _ in range(2):
        new_list += check_list(source)
    return [min(new_list), max(new_list)]


source_list = [1, 5, 2, 3, 4,  1, 7, 8, 15, 1]
print(source_list)
res = max_sequence(source_list)
print(res)
