# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint

def input_data(p_name):
    candy_count = int(input(f"{p_name} введите количество конфет, которые возьмете от 1 до 28: "))
    while candy_count < 1 or candy_count > 28:
        candy_count = int(input(f"{p_name} введите правильное количество конфет: "))
    return candy_count

def p_print(p_name, k, c_count, value):
    print(f"Ходил {p_name}, он взял {k}, теперь у него {c_count}. Осталось на столе {value} конфет.")

def game():
    global value
    flag = randint(0, 1)  # флаг очередности
    if flag:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")

    counter1 = 0
    counter2 = 0

    while value > 28:
        if flag:
            k = input_data(player1)
            counter1 += k
            value -= k
            flag = False
            p_print(player1, k, counter1, value)
        else:
            k = input_data(player2)
            counter2 += k
            value -= k
            flag = True
            p_print(player2, k, counter2, value)

    if flag:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
game()