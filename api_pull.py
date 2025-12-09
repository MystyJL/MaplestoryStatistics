import requests
import time
# import tqdm
#          https://www.nexon.com/api/maplestory/no-auth/ranking/v2/na?type=overall&id=weekly&reboot_index=0&page_index=1
httpurl = "https://www.nexon.com/api/maplestory/no-auth/ranking/v2/na?type=overall&id=legendary&reboot_index=0&page_index="
real = int(requests.get(httpurl+str(0)).json()["totalCount"])
worldid = {1:"bera",19:"Scania",45:"Kronos",70:"Hyperion"}
classes = {}
counter= 0
checkBreak = False
for i in range(0,real,10):
    counter +=1
    u = httpurl+str(i)
    response = requests.get(u)
    jsonData = response.json()
    players = jsonData["ranks"]
    for player in players:
        if int(player["level"])<270:
            checkBreak = True
            break
        new = {"ign":player["characterName"],"lvl":player["level"], "job":player["jobName"], "world": worldid[int(player["worldID"])]}
        print(new)
    if checkBreak:
        break
    time.sleep(1)
    