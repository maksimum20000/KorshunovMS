#Задача 5
#Дан список: items = ['book', 'pen', 'pencil', 'eraser', 'ruler']
#Удалите элемент 'pencil' из списка, зная его значение.
items = ['book', 'pen', 'pencil', 'eraser', 'ruler']
items.remove("pencil")
print(items)

#Задача 6
#Даны два списка: list1 = [1, 2, 3] и list2 = [4, 5, 6]
#Объедините их в один новый список с именем merged_list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)

#Задача 7
#Дан список: numbers = [1, 2, 3, 4, 5]
#Получите и выведите на экран последний элемент этого списка, используя отрицательные индексы.
numbers = [1, 2, 3, 4, 5]
print(numbers[-1])

#Задача 8
#Дан список: my_list = [10, 20, 30, 40, 50]
#Полностью очистите этот список, чтобы он стал пустым.
my_list = [10, 20, 30, 40, 50]
my_list.clear()
print(my_list)
