#Task 23: Qiymatlar bo‘yicha indekslarni guruhlash
#**Funksiya yarat**:
#def group_indices(numbers: list[int]) -> dict[int, list[int]]:
#**Shart**: Har bir noyob son uchun u ro‘yxatda qayerda turganini ko‘rsatuvchi dict qaytar.
#Natija: `{1: [0, 2, 5], 2: [1, 4], ...}`

def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    group = {}
    
    for index,number in enumerate(numbers):
        if number in group:
            group[number].append(index)
        else:
            group[number] = [index]
    return group

print(group_indices([1, 2, 1, 3, 2, 1]))


        