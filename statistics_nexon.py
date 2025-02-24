import json

class_rename = {('Magician',32):"Bishop",('Magician',22):"Archmage(I/L)",('Magician',12):"Archmage(F/P)",
                ('Thief',22):"Shadower",('Thief',12):"Night Lord",
                ('Bowman',22):"Marksman",('Bowman',12):"Bowmaster",
                ('Warrior',32):"Dark Knight",('Warrior',22):"Paladin",('Warrior',12):"Hero",
                ('Pirate',32):"Cannon Master",('Pirate',22):"Corsair",('Pirate',12):"Buccaneer"}


file = open("playerData.txt","r",encoding="UTF-8")
text = file.read()
json_strings = text.strip().replace("'","\"").replace("False,","\"False\",").split("\n")
for i in range(len(json_strings)):

    json_strings[i] = json.loads(json_strings[i])


# 280,285,290,295 respectively
classes_all = [{},{},{},{}]
class_name = set()
for i in json_strings:
    maple_class = (i["jobName"],i["jobDetail"])
    # get a list of class names for later
    if maple_class in class_rename:
        class_name.add(class_rename[maple_class])
    else:
        class_name.add(i["jobName"])
    # sort the data
    for j in range(4):
        if int(i["level"]) >= 280+(j*5):
            if maple_class not in classes_all[j]:
                classes_all[j][maple_class] = 0
            classes_all[j][maple_class] += 1

formatting_short = "|{}\t\t\t\t|{}\t|{}\t|{}\t|{}|"
formatting_long = "|{}\t\t\t|{}\t|{}\t|{}\t|{}|"

for index in range(4):
    new_dict = {}
    for i,j in classes_all[index].items():
        if i in class_rename:
            new_dict[class_rename[i]] = j
        else:
            if i[0] not in new_dict:
                new_dict[i[0]] = 0
            new_dict[i[0]] += j
    classes_all[index] = new_dict

class_name = list(class_name)
class_name.sort()


# format for markdown table
print(formatting_short.format("class","280+","285+","290+", "295+"))
print("|:-|:-|:-|:-|:-|")

for i in class_name:
    for j in range(4):
        if i not in classes_all[j]:
            classes_all[j][i] = 0
    if len(i)< 8:
        print(formatting_short.format(i,classes_all[0][i],classes_all[1][i],classes_all[2][i],classes_all[3][i]))
    else:
        print(formatting_long.format(i,classes_all[0][i],classes_all[1][i],classes_all[2][i],classes_all[3][i]))



