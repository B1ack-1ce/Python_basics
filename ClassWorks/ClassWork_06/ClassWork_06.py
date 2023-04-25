from random import randint

def prompt(msg):
    num = int(input(msg))
    return num

def create_and_fill_list(dim):
    my_list = list(randint(0, 10) for _ in range(0, dim))
    print(my_list)
    return my_list

def task_39():

    first_list = create_and_fill_list(prompt("Input 1: "))
    second_list = create_and_fill_list(prompt("Input 2: "))

    sort_list = [i for i in first_list if i not in second_list]
    print(sort_list)

def task_41():
    my_list = create_and_fill_list(prompt("Input 3: "))
    print(my_list)
    repeats = [my_list.count(i) // 2 for i in set(my_list)] # алгоритм поиска пары
    print(sum(repeats))

def summarize(number, sum = 0):
    for item in range(1, number // 2 + 1):
        if number % item == 0:
            sum += item
    return sum

def task_43():
    limit_num = prompt("Input num of limit? ")
    my_list = [i for i in range(limit_num)]

    for item in my_list:
        sum = summarize(summarize(item))
        temp = summarize(item)
        if item == sum and item != temp:
            print(item, temp)
        sum = temp = 0

task_39()