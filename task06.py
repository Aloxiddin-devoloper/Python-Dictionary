#Task 6:
#Foydalanuvchidan `kalit` nomini input orqali so‘ra.
# Agar dictda shu kalit bo‘lsa, qiymatini chiqarsin, aks holda `"Topilmadi"` chiqarsin.

kalit = input("kalit = ")

student = {
    "name" : "Aloxiddin",
    "age" : 20
}

if kalit in student:
    print(student[kalit])
else:
    print("topilmadi")