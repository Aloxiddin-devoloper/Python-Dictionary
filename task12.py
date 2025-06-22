#Task 12:
#`inventory` dict bor. Agar mahsulot yo‘q bo‘lsa, uni `quantity = 0` bilan qo‘sh.

inventory = {}

while True:
    quantity = input("quantity kiriting: ")
    qiymat = input("qiymatni kiriting: ")
    inventory[quantity] = qiymat
    
    if qiymat == "":
        inventory[quantity] = 0
        break

print(inventory)
    
