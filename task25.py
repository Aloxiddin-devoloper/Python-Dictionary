# Task 25: Yosh bo‘yicha guruhlash
#**Funksiya yarat**:
#def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
#**Shart**: Har bir odamni `age` bo‘yicha guruhlab, ismlarini list ko‘rinishida qaytar.

def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    result = {}
    
    for person in people:
        age = person["age"]
        name = person["name"]
        
        if age not in result:
            result[age] = []
        result[age].append(name)
    
    return result    



people = [
    {"name" :"Ali", "age" : 20},
    {"name" :"Vali", "age" : 23},
    {"name" :"Sora", "age" : 19}
]
print(group_by_age(people))