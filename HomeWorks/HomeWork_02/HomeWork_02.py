import random

def task_10():
    coins = int(input("Введите количество монеток: "))
    index, eagle, tails = 0, 0, 0
    
    while index < coins:
        side = random.randint(0, 1)
        
        if side == 0:
            eagle += 1
        else:
            tails += 1
        
        index += 1
    
    print(f"eagle - {eagle}, tails - {tails}")
    
    if eagle > tails:
        print(f"Минимальное количество переворотов: {tails}")
    else:
        print(f"Минимальное количество переворотов: {eagle}")

def task_12():
    sum = int(input("Введите сумму чисел: "))
    multi = int(input("Введите произведение чисел: "))
    
    count = 1
    while count < sum:
        
        if sum - count == multi / count:
            print(f"Первое число {count}, второе число {sum - count}")
            break
        count += 1

def task_14():
    user_number = int(input("Введите число: "))
    couples = 1

    print(f"Целыe степени двойки до числа {user_number}", end= ":| ")
    while couples < user_number:
        
        print(couples, end = " | ")
        couples *= 2