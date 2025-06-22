#Task 21: Ismlar sonini sanash
#**Funksiya yarat**:
#def count_names(names: list[str]) -> dict[str, int]:
#**Shart**: Berilgan `names` ro‘yxatidagi har bir ism necha marta uchraganini hisoblab, dict qaytar.
# Natija: `{"Ali": 3, "Vali": 2, "Sami": 1}`

def count_names(names: list[str]) -> dict[str, int]:
    """Ismlarni sanash 
    Args:
        (names: list[str]: ismlar ro'yxati
    Returns:
        dict[str, int]:  natija
    """
    result = {}
    for name in names:
        result[name] = names.count(name) 
    return result

name_list = {"ali","vali","jon","bob","ali","vali","jon","bob","ali"}

result = count_names(name_list)
print(result)
