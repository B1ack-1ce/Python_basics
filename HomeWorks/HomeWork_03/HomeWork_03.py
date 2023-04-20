import random

def task_16_and_18():
    list_num = list()
    min_list_num = 1
    max_list_num = 10
    
    for i in range(0, int(input('Введите количество элементов:\n'))):
        list_num.append(random.randint(min_list_num, max_list_num))
    print(list_num)

    desired_element = int(input(f"Какой элемент нужно найти?\n"))
    count = list_num.count(desired_element)
    print(f"Найденных элементов со значением {desired_element}: => {count}.")

    if count == 0:
        temp = None
        min_num = abs(desired_element - list_num[0])
        for i in list_num:
            if abs(desired_element - i) <= min_num:
                temp = i
                min_num = abs(desired_element - i)
        print(f"Ближайшее число к искомому: {temp}. ")

def task_20():
    scrabble_list = {
                    1: 'A' 'E' 'I' 'O' 'U' 'L' 'N' 'S' 'T' 'R' 'А' 'В' 'Е' 'И' 'Н' 'О' 'Р' 'С' 'Т',
                    2: 'D' 'G' 'Д' 'К' 'Л' 'М' 'П' 'У',
                    3: 'B' 'C' 'M' 'P' 'Б' 'Г' 'Ё' 'Ь' 'Я',
                    4: 'F' 'H' 'V' 'W' 'Y' 'Й' 'Ы',
                    5: 'K' 'Ж' 'З' 'Х' 'Ц' 'Ч',
                    8: 'J' 'X' 'Ш' 'Э' 'Ю',
                    10: 'Q' 'Z' 'Ф' 'Щ' 'Ъ'
                    }

    word = input("Введите слово:\n").upper()
    char_sum = 0

    for item in word:
        for point, value in scrabble_list.items():
            if item in value:
                char_sum += point 
            
    print(f'Слово "{word.lower()}" набрало {char_sum} баллов.')
