bill_amount = float(input("Введите сумму счета: "))
tip_percent = float(input("Введите процент чаевых: "))
tip_amount = bill_amount * (tip_percent / 100)
print(f"Чаевые: {tip_amount:.2f} тенге")
total_amount = bill_amount + tip_amount
print(f"Итого к оплате: {total_amount:.2f} тенге")




