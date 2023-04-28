import random

def task_30():
    my_list = arithc_progres(prompt("Введите первый элемент: "), 
                   prompt("Введите разность: "), 
                   prompt("Введите количество элементов:"))
    
    print(my_list)

def arithc_progres(start_num, step, count_el):
    my_list = [i for i in range(start_num, count_el * step, step)]
    return my_list

def task_32():
    my_list = create_and_fill_list(prompt("Введите количество элементов: "))
    
    find_index_on_ranges(my_list, 
                         prompt("Введите минимальный предел: "), 
                         prompt("Введите максимальный предел: "))


def find_index_on_ranges(my_list, min_range, max_range):
    index_list = list()
    for i in range(0, len(my_list)):
        if my_list[i] >= min_range and my_list[i] <= max_range:
            index_list.append(i)
    print(index_list)

def create_and_fill_list(dim, min_num = 0, max_num = 20):
    my_list = [random.randint(min_num, max_num) for _ in range(0, dim)]
    print(my_list)
    return my_list

def prompt(msg):
    num = int(input(msg))
    return num
    
task_32()