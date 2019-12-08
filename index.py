# print('hello')
#
# x = 10
# y = 20
#
# # 20^3
# print(y ** 3)
#
# # скільки разів на ціло можна поділити
# print(10 // 2)  # 5
#
# # List - це колекція, яка впорядкована і змінна. Дозволяє дублювати членів.
# #     Tuple - це колекція, яка впорядкована і незмінна. Дозволяє дублювати членів.
# #     Set - це колекція, яка невпорядкована і неіндексована. Немає дубльованих членів.
# #     Dictionary - це колекція, яка невпорядкована, змінна і індексована. Немає дубльованих членів. Обєкт
#
# list = ["apple", "banana", "cherry"]
# list.insert(1, "orange")
# print(list)
#
# list.remove("banana")  # видалити якесь значення
# del list[0]  # видалити елемент
# print(list)
#
# tuple = ("apple", "banana", "cherry")  # Array like const
#
# dict = {
#     "model": "Hello",
#     "year": 1964,
#     "owners": ['Katty, Kimmy']
# }
#
# # owners = dict.get("owners")
# owners = dict["owners"]
# print(owners)
#
# a = 10
# b = 20
# if a > b:
#     print('A > B')
# elif a < b:
#     print('A < B')
# else:
#     print('A = B')
#
# print('A is big') if a > b else print('B is big')
#
# # || &&
# if a > b and a ** 2 > b: print('One line IF')
# if a > b or a ** 2 > b: print('WTF IS **')
#
# # LOOPS
#
#
# # Якщо поміняти i++ та print місцями, то не буде працювати
# i = 0
# while i < 10:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
#
# P = [30, 78, 31, 42, 70, 6, 3]
#
# print(P.__len__())
#
# for num in P:
#     if num > 30:
#         print(num)
#
# list_2 = [2, 5, '1', 8, 6, 0]
#
# for i in list_2:
#     print(i)
# for i in range (0, 10, 3): # for (let i = 0; i < 10; i+=3)
#     print(i)
#
# for i in range(10, 0, -2):
#     print(i)
#
#
# my_list = [1, 2, 7, 4, 5, 10, 6, 99]
#
# a = my_list[0:3]
#
# a[0] = 10000
#
# print(my_list[len(my_list)::-1])
#
# print(a)
# print(my_list)


# a = 3
# if a == 3:
#     print('OK')
# else:
#     print('Not OK')
#
# first = int(input('Enter a > '))
# second = int(input('Enter b > '))
# third = int(input('Enter c > '))
#
# num_list = [first, second, third]
#
# num_list.sort()
#
# print(num_list)

numbers = [2, 17, 13, 6, 22, 31, 45, 66, 100, -18]

# for i in numbers:
#     print(i)

# for i, num in enumerate(numbers):
#     if i % 3 == 1:
#         print(num)

#
# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# for i, num in enumerate(numbers):
#     if num % 3 == 0:
#         numbers[i] = 'Okten'
#
# print(numbers)

# print(numbers[len(numbers)::-1])
#
#
# nums = []
#
# for i in range(0, 50):
#     nums.append(i*2)
#
# print(nums)
# print(len(nums))

prices = [100, 250, 50, 168, 120, 345, 188]
avg_price = 0;

for price in prices:
    avg_price += price

print(avg_price)

rand = [2, 2.3, 'HELLO', 'dadada', 0, True, '0']

for val in rand:
    if val.isnumeric(): # діч
        print('r')