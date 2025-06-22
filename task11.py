#Task 11:
#Bo‘sh `config` dict yarat. 
# Foydalanuvchidan 3 ta `setting` nomi va qiymati so‘raladi. Ularni dictga joyla.

config = {}

for i in range(1,4):
    key = input(f"{i} - key nomini kiriting: ")
    qiymat = input(f"{i} - qiymat nomini kiriting: ")
    config[key] = qiymat
    
print(config)
