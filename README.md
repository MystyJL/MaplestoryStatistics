# MaplestoryStatistics

First pull from nexon's ranking api and pipe the stdout into a text file. If this file already exists then delete it as this will append to that file and will not overwrite the file.
```
python3 api_pull.py >> playerData.txt
```

After about 30 minutes to 1 hour you should have all the data from the ranking api of all characters lvl 280 and above. After that you can run the statistics python script to get the count of every class in a 
markdown table format.

```
python3 statistics_nexon.py
```
