import argparse
import os
import random
import pandas as pd
import json

BASE_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.join(BASE_DIR, '..')
ENV_PATH = os.path.join(PARENT_DIR, '.env')
parser = argparse.ArgumentParser()
parser.add_argument('-i', help='tsv file', required=True)
parser.add_argument('-o', help='output file (optional)')
args = parser.parse_args()
INPUTFILE = os.path.join(PARENT_DIR, '{}'.format(args.i))

def analyze():
    df = pd.read_csv(INPUTFILE, sep='\t')
    
    category = df.groupby("coding").size()
    category = dict(category)
    for i in ['c', 'f', 'r', 'o']:
        if i not in category:
            category[i] = 0
    category["course-related"] = int(category.pop("c"))
    category["food-related"] = int(category.pop("f"))
    category["residence-related"] = int(category.pop("r"))
    category["other"] = int(category.pop("o"))
    if args.o:
        OUTFILE = os.path.join(PARENT_DIR, '{}'.format(args.o))
        with open(OUTFILE, 'w') as f: 
            json.dump(category, f)
            
    else:
        print(category)

if __name__ == "__main__":
    analyze()