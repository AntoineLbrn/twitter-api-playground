import requests

kc_twitter_id = 1322196660232114177
token = "AAAAAAAAAAAAAAAAAAAAAG29kAEAAAAAtxB0w%2BClJ2%2FdGmPQU7TWpxqBeWU%3DITm2RhcfZKjqu98UMxnKS9PPzELmRQ19DR5n95nP4rL2fZeqV1"
headers = {"Authorization": f"Bearer {token}"}

def fetch(url, params= None):
    r = requests.get(url, params, headers= headers)
    print(r)
    return r.json()

def fetch_kc_followers(pagination_token= None):
    if pagination_token:
        return fetch(f'https://api.twitter.com/2/users/{kc_twitter_id}/followers?max_results=1000&pagination_token={pagination_token}')
    else:
        return fetch(f'https://api.twitter.com/2/users/{kc_twitter_id}/followers?max_results=1000')
