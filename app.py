from helpers import *
import json


token = None
for i in range(1, 40):
    followers = fetch_kc_followers(token)
    token = followers["meta"]["next_token"]
    with open(f'kc/data{i}.json', 'w') as f:
        json.dump(followers, f)