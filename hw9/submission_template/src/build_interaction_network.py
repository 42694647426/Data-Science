import json
import argparse
import pandas as pd

def interaction():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i')
    parser.add_argument('-o')
    args = parser.parse_args()

    df = pd.read_csv(args.i, usecols=['title','pony'])

    df['pony'] = df['pony'].str.lower()

    remove_words=['other','ponies', 'and', 'all']
    # remove some speakers
    df['pony'] = [None if any(x in p for x in remove_words) else p for p in df['pony'] ]
    
    # get 101 most frequent ponies
    tmp_df = df['pony'].value_counts().to_dict()
    lst = [(key,value) for key,value in tmp_df.items()]
    lst.sort(key=lambda x: x[1], reverse=True)
    frequent_pony = [p for p, _ in lst[:101]]
    
    # remove other speakers
    df['pony'] = [p if p in frequent_pony else None for p in df['pony']]
    
    #drop the Nones
    df.dropna()

    iterator = df.itertuples(index=False)
    
    # prepare result dict
    output_res = {p:{} for p in frequent_pony}
    
    #first speaker
    previous_eps, previous_pony = next(iterator)
    for row in iterator:
        cur_ep, cur_pony = row

        if cur_pony and previous_pony and cur_ep == previous_eps and cur_pony != previous_pony:
            if previous_pony in output_res[cur_pony]:
                output_res[cur_pony][previous_pony] += 1
            else:
                output_res[cur_pony][previous_pony] = 1
            
            if cur_pony in output_res[previous_pony]:
                output_res[previous_pony][cur_pony] += 1
            else:
                output_res[previous_pony][cur_pony] = 1

        
        previous_pony = cur_pony
        previous_eps = cur_ep

    with open(args.o, 'w') as f:
        json.dump(output_res, f)

if __name__ == '__main__':
    interaction()
    
