from helpers import *
import json
import time


i = 0
token = None
while True:
    followers = fetch_mv_followers(token)
    if (not "meta" in followers):
        # wait 15 minutes (twitter api request cooldown)
        time.sleep(950)
        continue
    else:
        i = i+1
        token = followers["meta"]["next_token"]
        with open(f'mv/data{i}.json', 'w') as f:
            json.dump(followers, f)
