# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Входные данные: 'ываабв лповап абвцукв алоабвабв ываываыв'
# Выходные данные: 'лповап ываываыв'

def transform_txt(txt_list, find_txt):
    new_list = []
    for i in txt_list:
        if find_txt not in i:
            new_list.append(i)
    return new_list


txt = input("Введите текст через пробел: ").split()
find_txt = "абв"
lst = [i for i in txt if find_txt not in i] # сокращенная запись функции transform_txt
print(f"Результат: {' '.join(lst)}")
print(f"Результат: {' '.join(transform_txt(txt, find_txt))}")
