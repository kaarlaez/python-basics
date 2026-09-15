
#task1
age = int(input("Ваш возраст?  "))

if age >= 18:
    print("Доступ разрешён")

else: 
    print("Доступ запрещён")

#task2
number = int(input("Введите число: "))

if number > 0:
    print("Положительное")
elif number < 0:
    print("Отрицательное")
else:
    print("Ноль")

#task3 

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if num1 >= num2: 
    print(f"Большее: {num1}")
else:
    print(f"Большее: {num2}")

#task4
year = int(input("Твой год рождения"))

age = 2026 - year

if age >= 18:
    print(f"Тебе {age} года, доступ разрешён")

else: 
    print(f"Тебе {age} лет, доступ запрещён")

#task5
num = int(input("Назови любое число: "))

if num % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")

#task6
point = int(input("Введите балл:"))

if point >= 90:
    print("A")
elif point >= 75:
    print("B")
elif point >= 60:
    print("C")
else:
    print("F")

#task7
login = input("Введите логин: ")
password = input("Введите пароль: ")

if login == "admin" and password == "1234":
    print("Вход выполнен")
else:
    print("Неверные данные")

#task8
week = input("Введите неделю: ")

if week == "суббота" or week == "воскресенье":
    print("Выходной")
else:
    print("Рабочий день")

#task9
purchase_amount = int(input("Введите сумму покупки: "))

loyalty_card = input("Есть карта лояльности (да/нет):")

if purchase_amount >= 50000 and loyalty_card == "да":
    print("Скидка: 20%")
    discount = 20

elif purchase_amount >= 50000 and loyalty_card == "нет":
    print("Скидка: 10%")
    discount = 10

elif purchase_amount < 50000 and loyalty_card == "да":
    print("Скидка: 5%")
    discount = 5

else:
    print("Скидка: 0%")
    discount = 0

discount_amount = purchase_amount * discount / 100
total_amount = purchase_amount - discount_amount

print(f"Сумма скидки: {discount_amount:.2f} тенге")
print(f"К оплате: {total_amount:.2f} тенге")
