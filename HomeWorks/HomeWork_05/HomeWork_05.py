def prompt(msg):
    return int(input(msg))

def task_26():
    print(recursive_pow(prompt("Введите основание: "), prompt("Введите степень: ")))

def recursive_pow(num1, num2):
    if num2 == 1: return num1
    else: return num1 * recursive_pow(num1, num2 - 1)

def task_28():
    print(recursive_sum(prompt("Введите первое неотрицательное число: "), 
                        prompt("Введите второе неотрицательно число: ")))

def recursive_sum(first_num, second_num ):
    if first_num == 0: return second_num
    else: return recursive_sum(first_num - 1, second_num + 1)