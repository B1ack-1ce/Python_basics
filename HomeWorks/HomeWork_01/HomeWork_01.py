

# Задача 2: 
def task_02():
    userNumber = int(input("Введите трехчначное число: "))

    if userNumber < 0:
        userNumber = abs(userNumber)

    if userNumber > 99 and userNumber < 1000:
        res = (userNumber // 100) + ((userNumber // 10) % 10) + (userNumber % 10)
        print(f"Сумма цифр числа {userNumber} = {res}.")
    else:
        print("Число не является трехзначным.")

# Задача 4:
def task_04():
    numberOfCranes = int(input("Какое общее количество журавликов? "))

    if numberOfCranes  % 6 == 0:
        quantity = numberOfCranes // 6
        print(f'Катя сделала {quantity * 4} журавликов.')
        print(f'Сережа сделал {quantity} журавликов.')
        print(f'Петя сделал {quantity} журавликов.')

# Задача 6:
def task_06():
    ticket = int(input("Введите номер билета: "))

    if ticket >= 100_000 and ticket < 1_000_000:
        firstPart = ticket // 1000
        firstPart = (firstPart // 100) + ((firstPart // 10) % 10) + (firstPart % 10)

        secondPart = ticket % 1000
        secondPart = (secondPart // 100) + ((secondPart // 10) % 10) + (secondPart % 10)
        
        if firstPart == secondPart: print("Билет счастливый!")
        else: print("Билет к сожалению несчастливый.")
    else: 
        print("Номер билета не шестизначный.")

def task_08():
    n = int(input('Введите количество долек по длине: '))
    m = int(input('Введите количество долек по ширине: '))
    k = int(input('Сколько долек нужно отломить за 1 разлом? '))
    if k % n == 0 or k % m == 0:
        print('Yes')
    else: 
        print('No')