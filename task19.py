#Task 19:
#Quyidagi dictdagi barcha `qiymat`lar soni bo‘lsa, ularni yig‘indisini hisobla:
#scores = {"math": 90, "english": 85, "science": 92}

jami = 0
scores = {"math": 90, "english": 85, "science": 92}

for i in scores:
    jami += scores[i]

print(jami)
    
