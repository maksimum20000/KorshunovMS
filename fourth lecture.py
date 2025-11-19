#Задача 1
#Дан список: fruits = ["apple", "banana", "cherry"]
#Добавьте элемент "orange" в конец этого списка.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#Задача 2
#Дан список: numbers = [10, 20, 30, 40, 50, 60, 70]
#Используя срезы, получите из него список [30, 40, 50].
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[2:5])

#Задача 3
#Дан список: colors = ["red", "blue", "green"]
#Замените второй элемент (с индексом 1) на строку "yellow".
colors = ["red", "blue", "green"]
colors[1] = "yellow"
print(colors)

#Задача 4
#Дан список: letters = ['a', 'b', 'd', 'e']
#Добавьте элемент 'c' в список так, чтобы он оказался между 'b' и 'd' (т.е. на позицию с индексом 2).
letters = ['a', 'b', 'd', 'e']
letters.insert(2, "c")
print(letters)

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
