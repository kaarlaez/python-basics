# 1task
name = "Карл"
age = 20
city = "Алматы"
print(f"Меня зовут {name}, мне {age} года, я из {city}")

# 2task
name = input("Как тебя зовут? ")
print(f"Привет, {name}!")

# 3task
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = a + b
print("Сумма:", c)

# 4task
age = (int(input("Введите ваш возраст: ")))
print(f"Через 10 лет тебе будет {age + 10}")

# 5task
price_product = float(input("Введите цену товара: "))
quantity_product = int(input("Введите количество товара: "))
print(f"Итого: {price_product * quantity_product:.2f} тенге")

# 6task
C = float(input("Введите температуру: "))
F = C * 9 / 5 + 32
print(f"{C} по Цельсию = {F:.1f} по Фаренгейту")

# 7task
a = (input("Введите число a: "))
print("До преобразования:", type(a))
a = int(a)
print("После преобразования:", type(a))
    

# 8task
a = 5
b = 10
c = a
a = b
b = c
print(f"a = {a}, b = {b}")

# 9task
amount_kzt = int(input("Введите сумму в тенге: "))
usd_rate = float(input("Введите курс доллара: "))
print(f"{amount_kzt:,} тенге = {amount_kzt / usd_rate:.2f} долларов".replace(",", " "))

