import requests
import time
# import tqdm
httpurl = "https://www.nexon.com/api/maplestory/no-auth/v1/ranking/na?type=overall&id=legendary&reboot_index=0&page_index="
real = 24494210
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
        if int(player["level"])<280:
            checkBreak = True
            break
        print(player)
    if checkBreak:
        break
    time.sleep(1)
    