import argparse
import os
import json
import requests
import requests.auth
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.join(BASE_DIR, '..')
ENV_PATH = os.path.join(PARENT_DIR, '.env')
parser = argparse.ArgumentParser()
parser.add_argument('-o', help='Output file', required=True)
parser.add_argument('-s', help='subreddit', required=True)
args = parser.parse_args()
OUTPUTFILE = os.path.join(PARENT_DIR, '{}'.format(args.o) )
SUBREDDIT = args.s


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

def create_samples(headers, num_post = 100, sub = SUBREDDIT, file_name = OUTPUTFILE):
    with open(file_name, 'w') as f:
        response = requests.get(
            f'https://oauth.reddit.com/r/{sub}/new', headers=headers, params={'limit':num_post})
        for post in response.json()['data']['children']:
            f.write(json.dumps(post) + '\n')

def main():
    headers = authenticate()
    create_samples(headers)

if __name__ == '__main__':
    main()