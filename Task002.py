# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
def read_file(file_name):
    with open(file_name, 'r') as data:
        return data.read()

def write_file(file_name, str_data):
    with open(file_name, 'w') as data:
        data.write(str_data)

def rle_compression(txt):
    count_sim = 1
    result = ""
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            count_sim += 1
        else:
            result += (str(count_sim) + txt[i])
            count_sim = 1
    if count_sim > 1 or (txt[-2] != txt[-1]):
        result += (str(count_sim) + txt[-1])
    return result

def rle_decompression(txt):
    result = ""
    num = ""
    for i in range(0, len(txt)):
        if txt[i].isdigit():
            num += txt[i]
        else:
            result += (txt[i] * int(num))
            num = ""
    return result

txt_input = read_file("rle_input.txt")
print(txt_input)
print()
txt_comp = rle_compression(txt_input)
print(txt_comp)
print()
write_file("rle_output.txt", txt_comp)
txt_decomp = rle_decompression(txt_comp)
print(txt_decomp)
