import argparse
import sys
import pandas as pd
import os
import json
import string

def main(args=sys.argv[1:]):
    pony_names = ['twilight sparkle', 'applejack', 'rarity', 'pinkie pie', 'rainbow dash', 'fluttershy']
    puncs = list(string.punctuation)

    stop_words = []
    with open(os.path.join(os.path.dirname(__file__), '..', 'data',  'stopwords.txt')) as f:
        for line in f:
            if not line.startswith('#'):
                stop_words.append(line.strip('\n'))

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-d', '--dialog')
    args = parser.parse_args()

    df = pd.read_csv(args.dialog, usecols=['pony','dialog'])
    
    df['pony'] = df['pony'].str.lower()
    df['dialog'] = df['dialog'].str.lower()
    
    df = df[df['pony'].isin(pony_names)]
    
    
    for punc in puncs:
        df['dialog'] = df['dialog'].str.replace(punc, ' ', regex=False)
    
    
    df = df.groupby('pony').agg(' '.join).reset_index()
    

    df['dialog'] = df['dialog'].str.split()
    
    # remove stop words 
    d = {}
    for pony in pony_names:
        if pony in df['pony'].values:
            d[pony] = [w for w in df[df['pony'] == pony].iloc[0]['dialog'] if w.isalpha() and w not in stop_words]
    
    total_count = {}
    res_dict = {}
    for pony in d:
        count = {}

        for w in d[pony]:
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
        
        for w in count:
            if w in total_count:
                total_count[w] += count[w]
            else:
                total_count[w] = count[w]
        
        res_dict[pony] = count

    # remove < 5 
    final_dict = {}
    for pony in res_dict:
        freq = {}
        for w in res_dict[pony]:
            if total_count[w] >= 5:
                freq[w] = res_dict[pony][w]
        final_dict[pony] = freq
    
    # check output directory
    if os.path.dirname(args.output):
        os.makedirs(os.path.dirname(args.output), exist_ok=True)

    with open(args.output, 'w') as f:
        json.dump(final_dict, f)

if __name__ == '__main__':
    
    main()
