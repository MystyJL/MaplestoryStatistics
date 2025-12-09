import json
# master list of class names and job details 
class_rename = {('Magician',32):"Bishop",('Magician',22):"Archmage(I/L)",('Magician',12):"Archmage(F/P)",
                ('Thief',22):"Shadower",('Thief',12):"Night Lord",
                ('Bowman',22):"Marksman",('Bowman',12):"Bowmaster",
                ('Warrior',32):"Dark Knight",('Warrior',22):"Paladin",('Warrior',12):"Hero",
                ('Pirate',32):"Cannon Master",('Pirate',22):"Corsair",('Pirate',12):"Buccaneer"}

# read the playerData file
file = open("playerData.txt","r",encoding="UTF-8")
text = file.read()

# clean the data
json_strings = text.strip().replace("'",'"').split("\n")

for i in range(len(json_strings)):
    json_strings[i] = json.loads(json_strings[i])


# 280,285,290,295 respectively
classes_all = [{},{},{},{},{},{},{}]
class_name = set()

# count the jobs
for i in json_strings:
    maple_class = i["job"]
    class_name.add(maple_class)
    # sort the data
    for j in range(7):
        if int(i["lvl"]) >= 270+(j*5):
            if maple_class not in classes_all[j]:
                classes_all[j][maple_class] = 0
            classes_all[j][maple_class] += 1
print(classes_all)


class_name = list(class_name)
class_name.sort()



# format for markdown table and print

formatting_short = "|{}\t\t\t\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|"
formatting_long = "|{}\t\t\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|"
formatting_longer = "|{}\t\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|"
print(formatting_short.format("class","270+","275+","280+","285+","290+", "295+","300"))
print("|:-|:-|:-|:-|:-|:-|:-|:-|")

for i in class_name:
    for j in range(7):
        if i not in classes_all[j]:
            classes_all[j][i] = 0
    if len(i)< 7:
        print(formatting_short.format(i,classes_all[0][i],classes_all[1][i],classes_all[2][i],classes_all[3][i],classes_all[4][i],classes_all[5][i],classes_all[6][i]))
    elif len(i)<15:
        print(formatting_long.format(i,classes_all[0][i],classes_all[1][i],classes_all[2][i],classes_all[3][i],classes_all[4][i],classes_all[5][i],classes_all[6][i]))
    else:
        print(formatting_longer.format(i,classes_all[0][i],classes_all[1][i],classes_all[2][i],classes_all[3][i],classes_all[4][i],classes_all[5][i],classes_all[6][i]))



