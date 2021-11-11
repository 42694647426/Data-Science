import os
import json
import requests
import requests.auth
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.join(BASE_DIR, '..')
ENV_PATH = os.path.join(PARENT_DIR, '.env')
SAMPLE1 = os.path.join(PARENT_DIR, 'sample1.json')
SAMPLE2 = os.path.join(PARENT_DIR, 'sample2.json')

SUBREDDITS_SAMPLE1 = ['funny', 'AskReddit', 'gaming', 'aww', 'pics', 'Music', 'science', 'worldnews', 'videos', 'todayilearned']
SUBREDDITS_SAMPLE2 = ['AskReddit', 'memes', 'politics', 'nfl', 'nba', 'wallstreetbets', 'teenagers', 'PublicFreakout', 'leagueoflegends', 'unpopularopinion']

load_dotenv(ENV_PATH)

def authenticate():
    client_auth = requests.auth.HTTPBasicAuth(
        'RbBh-OmTV_2hyP_LAx9D3Q', 'GOMoGJykOQQH7BV2LtT2WTGHopcDqg')
    post_data = {'grant_type': 'password',
                 'username': os.environ.get("REDDIT_USER"),
                 'password': os.environ.get("REDDIT_PWD")}

    headers = {'User-Agent': 'myapp/0.0.1'}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    #print(response.json())
    TOKEN = response.json()['access_token']

    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    return headers

def create_samples(file_name, sub_lst, headers, num_post):
    with open(file_name, 'w') as f:
        for subr in sub_lst:
            response = requests.get(
                f'https://oauth.reddit.com/r/{subr}/new', headers=headers, params={'limit':num_post})
            for post in response.json()['data']['children']:
                f.write(json.dumps(post) + '\n')
            
def main():
    headers = authenticate()
    create_samples(SAMPLE1, SUBREDDITS_SAMPLE1, headers, 100)
    create_samples(SAMPLE2, SUBREDDITS_SAMPLE2, headers, 100)


if __name__ == '__main__':
    main()