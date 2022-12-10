import json

ids = []
for i in range (1, 253):
    with open(f'popcorn/data{i}.json', 'r') as f1:
        data1 = json.load(f1)
        ids = ids + [i["id"] for i in data1["data"]]
with open('popcorn_followers_december_2022.json', 'w') as f2:
    json.dump(ids, f2)