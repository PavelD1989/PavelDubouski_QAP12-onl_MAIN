# Списки:
# 1. Создайте два любых списка и свяжите их с переменными.


def two_lists():
    list_one = [1, 2, "amd"]
    list_two = [2, 3, [23, "f"]]
    return list_one, list_two


# 2. Извлеките из первого списка второй элемент.


def extract_second_element():
    list_one = [1, 2, "amd"]
    extract_element = list_one[1]
    return extract_element


# 3. Измените во втором списке последний элемент. Выведите список на экран.


def change_last_element():
    list_two = [2, 3, [23, "f"]]
    list_two[-1] = "abc"
    return list_two



# 4. Соедините оба списка в один, присвоив результат новой переменной. Выведите
# получившийся список на экран.


def link_two_lists():
    list_one = [1, 2, "amd"]
    list_two = [2, 3, [23, "f"]]
    union_list = list_one + list_two
    return union_list


# 5. "Снимите" срез из соединенного списка так, чтобы туда попали некоторые части
# обоих первых списков. Срез свяжите с очередной новой переменной. Выведите
# значение этой переменной.


def few_elements():
    list_one = [1, 2, "amd"]
    list_two = [2, 3, [23, "f"]]
    union_list_slise = list_one[1:2] + list_two[1:2]
    return union_list_slise


# 6. Добавьте в список два новых элемента и снова выведите его.
def add_new_element():
    list_one = [1, 2, "amd"]
    adding_element = "row", 123
    list_one.extend(adding_element)
    return list_one


# 7. Даны списки. Нужно вернуть список, который состоит из элементов,
# общих для этих двух списков. -- !не использовать циклы
# a = [2, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 4, 6, 7, 8, 9, 1, 11, 12, 13]
# Списки преобразовали в множества (убрав повторяющиеся значения),
# выполнили операцию пересечения множеств (&)



def return_common_elements():
    a = [2, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 4, 6, 7, 8, 9, 1, 11, 12, 13]
    c = list(set(a) & set(b))
    return c

# 8. Есть список. Оставить в нем только уникальные значения.
# !не использовать циклы

def unique_elements():
    f_list = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
    f_list = set(f_list)
    f_list = list(f_list)
    return f_list


