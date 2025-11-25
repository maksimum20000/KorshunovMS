#Задача 1.
#Дан словарь person = {"name": "Alice", "age": 25, "city": "London"}.
# Выведите на экран возраст (age) персоны.

person = {"name": "Alice", "age": 25, "city": "London"}
print(person["age"])

#Задача 2.
#Дан словарь car = {"brand": "Ford", "model": "Mustang"}. Добавьте в него новый ключ year со значением 1964.
# Затем обновите значение model на "Focus".

car = {"brand": "Ford", "model": "Mustang"}
car["year"] = 1964
car["model"] = "Focus"
print(car)

#Задача 3.
#Дан словарь colors = {"r": "red", "g": "green", "b": "blue"}.
#Выведите на экран список всех его ключей и отдельно список всех его значений.

colors = {"r": "red", "g": "green", "b": "blue"}
keys_result = list(colors.keys())
val_result = list(colors.values())
print(keys_result)
print(val_result)

#Задача 4.
#Создайте словарь book, который будет содержать информацию о книге: название "Мастер и Маргарита", автор "Булгаков", год 1966.
book = {
    "name": "Мастер и маргарита",
    "author": "Булгаков",
    "year_of_publication": "1966"
}
print(book)

#Задача 5
#Дан словарь inventory = {"apples": 10, "oranges": 5, "bananas": 7}.
# Удалите из него ключ oranges и его значение.
inventory = {"apples": 10, "oranges": 5, "bananas": 7}
del inventory["oranges"]
print(inventory)

#Задача 6
#Дан словарь student = {"name": "Tom", "grade": "A"}.
# Проверьте, есть ли в словаре ключ "grade". Затем проверьте, есть ли в словаре значение "Tom".
student = {"name": "Tom", "grade": "A"}
if "grade" in student:
    print("Есть в словаре")
    if "Tom" in student.values():
        print("Есть в словаре")
