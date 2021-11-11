import argparse
import os
import random
import pandas as pd
import json


BASE_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.join(BASE_DIR, '..')
parser = argparse.ArgumentParser()
parser.add_argument('-o', help='Output file', required=True)
parser.add_argument('json', help='json file')
parser.add_argument('num', help='number of posts')
args = parser.parse_args()
OUTPUTFILE = os.path.join(PARENT_DIR, '{}'.format(args.o))
INPUT_JSON = os.path.join(PARENT_DIR, '{}'.format(args.json))
NUM_POST = int(args.num)

def random_chose():
    all = list(open(INPUT_JSON).read().splitlines())
    
    num_post = min(NUM_POST, len(all))
    random_select = random.sample(all, num_post)
    
    df = pd.DataFrame(columns=["Name", "title", "coding"])
    for post in random_select:
        post_dict = json.loads(post)
        df = df.append({'Name': post_dict['data']["author_fullname"], "title": post_dict['data']["title"], "coding": None}, ignore_index=True)
    df.to_csv(OUTPUTFILE, sep='\t', index=False)

if __name__ == "__main__":
    random_chose()
            
