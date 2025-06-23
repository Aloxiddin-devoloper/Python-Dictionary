#Task 22: Talabalarni guruhlash
#**Funksiya yarat**:
#def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:

#**Shart**: Har bir talaba ismini u tegishli bo‘lgan `group` bo‘yicha dict shaklida qaytar.
#Natija: `{"A": ["Ali", "Soli"], "B": ["Vali", "Karim"]}`

def group_students(students: list[dict[str, str]])     -> dict[str, list[str]]:
    groups = {}
    
    for student in students:
        groups[student["group"]] = []
        
    for student in students:
        groups[student["group"]].append(student["name"])

    return groups

students = [
    {
        "name" : "Ali",
        "group" : "A"
    },
    {
       "name" : "Soli",
        "group" : "A"  
    },
    {
       "name" : "Vali",
        "group" : "B"  
    },
    {
       "name" : "Karim",
        "group" : "B"  
    }
]

result = group_students(students)
print(result)