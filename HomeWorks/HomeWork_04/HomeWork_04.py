from random import randint

def fill_list(dimension):
    my_list = [randint(0, 20) for i in range(0, dimension)]
    return my_list

def prompt(msg):
    number = int(input(msg))
    return number

def find_and_sort_uniq_elements(first_list, second_list):
    sort_list = set()

    for item in first_list:
        for jtem in second_list:
            if item == jtem:
                sort_list.add(item)
    sort_list = list(sort_list)
    sort_list.sort()
    return sort_list

def task_22():
    first_list = fill_list(prompt("Введите размерность первого списка: "))
    second_list = fill_list(prompt("Введите размерность второго списка: "))
    print(f'Первый список:\n{first_list}\nВторой список:\n{second_list}')

    sort_list = find_and_sort_uniq_elements(first_list, second_list)
    print(f'Отсортированный список с уникальными значениями:\n{sort_list}')

def task_24():
    berries = [randint(0, 22) for _ in range(0, prompt("Введите количество кустиков?\n"))]
    print(f"Количество ягодок на каждом кустике:\n{berries}")
    
    max_num_of_ber = list()
    for item in range(0, len(berries) - 1):
        max_num_of_ber.append(berries[item -1] + berries[item] + berries[item + 1])
    max_num_of_ber.append(berries[-2] + berries[-1] + berries[0])
    
    print(f"Максимальное число ягодок: {max(max_num_of_ber)}.")
