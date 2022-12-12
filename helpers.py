import requests

kc_twitter_id = 1322196660232114177
popcorn_twitter_id = 1271010224732811266
ponce_twitter_id = 2295736877
zevent_twitter_id = 1051093212729880576
otp_twitter_id = 1322466841978089472
ultia_twitter_id = 1940911441
sly_twitter_id = 920621546619760640
mv_twitter_id = 544902207

token = None
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

def fetch_popcorn_followers(pagination_token= None):
    if pagination_token:
        return fetch(f'https://api.twitter.com/2/users/{popcorn_twitter_id}/followers?max_results=1000&pagination_token={pagination_token}')
    else:
        return fetch(f'https://api.twitter.com/2/users/{popcorn_twitter_id}/followers?max_results=1000')
    
def fetch_ponce_followers(pagination_token= None):
    if pagination_token:
        return fetch(f'https://api.twitter.com/2/users/{ponce_twitter_id}/followers?max_results=1000&pagination_token={pagination_token}')
    else:
        return fetch(f'https://api.twitter.com/2/users/{ponce_twitter_id}/followers?max_results=1000')

def fetch_zevent_followers(pagination_token= None):
    if pagination_token:
        return fetch(f'https://api.twitter.com/2/users/{zevent_twitter_id}/followers?max_results=1000&pagination_token={pagination_token}')
    else:
        return fetch(f'https://api.twitter.com/2/users/{zevent_twitter_id}/followers?max_results=1000')

def fetch_otp_followers(pagination_token= None):
    if pagination_token:
        return fetch(f'https://api.twitter.com/2/users/{otp_twitter_id}/followers?max_results=1000&pagination_token={pagination_token}')
    else:
        return fetch(f'https://api.twitter.com/2/users/{otp_twitter_id}/followers?max_results=1000')

def fetch_ultia_followers(pagination_token= None):
    if pagination_token:
        return fetch(f'https://api.twitter.com/2/users/{ultia_twitter_id}/followers?max_results=1000&pagination_token={pagination_token}')
    else:
        return fetch(f'https://api.twitter.com/2/users/{ultia_twitter_id}/followers?max_results=1000')

def fetch_sly_followers(pagination_token= None):
    if pagination_token:
        return fetch(f'https://api.twitter.com/2/users/{sly_twitter_id}/followers?max_results=1000&pagination_token={pagination_token}')
    else:
        return fetch(f'https://api.twitter.com/2/users/{sly_twitter_id}/followers?max_results=1000')

def fetch_mv_followers(pagination_token= None):
    if pagination_token:
        return fetch(f'https://api.twitter.com/2/users/{mv_twitter_id}/followers?max_results=1000&pagination_token={pagination_token}')
    else:
        return fetch(f'https://api.twitter.com/2/users/{mv_twitter_id}/followers?max_results=1000')
