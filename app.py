from helpers import *
import json, time


i= 0
token= None
while True:
    followers = fetch_popcorn_followers(token)
    if (not "meta" in followers):
        # wait 15 minutes (twitter api request cooldown)
        time.sleep(950)
        continue
    else:
        i = i+1
        token = followers["meta"]["next_token"]
        with open(f'popcorn/data{i}.json', 'w') as f:
            json.dump(followers, f)
