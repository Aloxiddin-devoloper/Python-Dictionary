#Task 20 (Muhim):
#Quyidagi dictda faqat qiymati `True` bo‘lgan kalitlarni chiqar:
#permissions = {"read": True, "write": False, "delete": True}
# chiqishi: read, delete

permissions = {"read": True, "write": False, "delete": True}

for i in permissions:
    if permissions[i] == True:
        print(i)
