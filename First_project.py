import math as m

# Циклы (for, while)
def cyclesEdu():
    name = "Привет, мир!"
    for i in name:
        print(i)
    for k in range(1,11):
        print(name)
    return

# Кортежи, словари
def TuplesEdu():
    tuple = ("first", 25, 25.1)
    print (tuple)
    return

def DictionariesEdu():
    dict = {"Саня":1, "Ваня":2, "Илья":3}
    print(dict)

    dict["Ваня"] = 5

    for k in dict.keys():
        print(k)

    print (dict)
    return

# ужас и эксперименты
def Experiments():
    list = ["test", 35, "wings"]
    print (list)
    print(type(tuple(list)))
    return

#Работа со строками
def StrExtraEdu():
    print("""ergfbhllieg
fregbjklerg
    gregregrggggggggggggggggggggggg
    grgrgergegr
    wergwergergergweg""")
    return

def StrExtraEdu2():
    print('"Strings "f" test"')
    print("test \"f\"  wfefewf")
    return

def StrExtraEdu3():
    text1 = "Привет мир"
    text2 = "ПРИВЕТ МИР"
    print(text1[0:4])

    print(text1.upper())
    print(text2.lower())

    return

#Работа с модулями
def ModulesEdu():
    print(m.sqrt(36))
    return


#Множества - sets
def SetsEdu():
    numbers = set()
    #Множества нельзя задать пустыми фигурными скобками

    numbers2 = {}
    print(type(numbers2))

    numbers = {1, 1, 2, 4, 2, "strings", 66, 45, "strings"}
    print(numbers)
    print("Добавляем элемент во множество")

    numbers.add(3)

    print(numbers)

    print("число 66 входит в множество " + str(66 in numbers))

    numbers3 = set([4, "buble", 66, 35.7])
    numbers4 = numbers.union(numbers3)
    numbers5 = numbers | numbers3
    numbers6 = numbers.intersection(numbers3)
    numbers7 = numbers & numbers3
    numbers8 = numbers3 - numbers
    print("Объединение множеств - " + str(numbers4))
    print("Объединение множеств - " + str(numbers5))
    print("Пересечение множеств - " + str(numbers6))
    print("Пересечение множеств - " + str(numbers7))
    print(numbers8)

    return

SetsEdu()
