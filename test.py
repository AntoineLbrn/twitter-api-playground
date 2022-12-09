import json

ids = []
for i in range (1, 75):
    with open(f'kc/data{i}.json', 'r') as f1:
        data1 = json.load(f1)
        ids = ids + [i["id"] for i in data1["data"]]
with open('test.json', 'w') as f2:
    json.dump(ids, f2)