print('hello')

x = 10
y = 20

# 20^3
print(y ** 3)

# скільки разів на ціло можна поділити
print(10 // 2)  # 5

# List - це колекція, яка впорядкована і змінна. Дозволяє дублювати членів.
#     Tuple - це колекція, яка впорядкована і незмінна. Дозволяє дублювати членів.
#     Set - це колекція, яка невпорядкована і неіндексована. Немає дубльованих членів.
#     Dictionary - це колекція, яка невпорядкована, змінна і індексована. Немає дубльованих членів. Обєкт

list = ["apple", "banana", "cherry"]
list.insert(1, "orange")
print(list)

list.remove("banana")  # видалити якесь значення
del list[0]  # видалити елемент
print(list)

tuple = ("apple", "banana", "cherry")  # Array like const

dict = {
    "model": "Hello",
    "year": 1964,
    "owners": ['Katty, Kimmy']
}

# owners = dict.get("owners")
owners = dict["owners"]
print(owners)

a = 10
b = 20
if a > b:
    print('A > B')
elif a < b:
    print('A < B')
else:
    print('A = B')

print('A is big') if a > b else print('B is big')
