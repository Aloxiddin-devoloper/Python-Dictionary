#Task 24: Eng ko‘p uchragan harfni topish
#**Funksiya yarat**:
#def most_common_char(text: str) -> str:
#**Shart**: Berilgan matndagi eng ko‘p uchraydigan bitta harfni qaytar.

def most_common_char(text: str) -> str:
    n = 0
    eng_kop = ""
    
    for i in text:
        if text.count(i) > n:
            n == text.count(i)
            eng_kop = i
    return eng_kop

print(most_common_char("aaasdddfdgffaaa"))
            
        
