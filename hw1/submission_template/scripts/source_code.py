import pandas as pd
import re
if __name__ == '__main__':
    #Data Collection
    raw_data = pd.read_csv("./data/IRAhandle_tweets_1.csv")
    raw_data = raw_data.head(10000)
    raw_data = raw_data[raw_data["content"].apply(lambda x: "?" not in x)]
    raw_data = raw_data.loc[(raw_data["language"] == "English")]
    raw_data = raw_data[["tweet_id","publish_date","content"]]
    raw_data.to_csv("./scripts/tweets.tsv", sep='\t', index=False)
    
    #Data Annotation
    comments = pd.read_csv("./data/tweets.tsv", sep='\t')
    comments["trump_mention"] = comments["content"].apply(lambda x : True if bool(re.search('\WTrump\W|^Trump\W|\WTrump$', x)) else False)
    comments.to_csv("dataset.tsv", sep='\t', index=False)
    

    #Analysis
    result = pd.DataFrame(columns=["result","value"])
    frac_trump_mentions =  len(comments.loc[comments["trump_mention"] == True]) / len(comments)
    print("total number of rows:", len(comments))
    print("fraction of trump mentioned:", frac_trump_mentions)
    result.loc[0] = ["frac_trump_mentions", round(frac_trump_mentions, 4)]
    result.to_csv("results.tsv", sep='\t', index=False)

    # Eliminate the repeating ones
    comments.drop_duplicates(subset ="content", keep = False, inplace = True)
    comments.to_csv("dataset.tsv", sep='\t', index=False)
    frac_trump_mentions =  len(comments.loc[comments["trump_mention"] == True]) / len(comments)
    print("total number of rows after eliminating duplicates:", len(comments))
    print("fraction of trump mentioned:", frac_trump_mentions)
    result.loc[0] = ["frac_trump_mentions", round(frac_trump_mentions, 4)]
    result.to_csv("results.tsv", sep='\t', index=False)

    # Checking if lower-case trumps are eliminated
    print("----------------------------------------------------------")
    trump = comments[comments["content"].apply(lambda x : "trump" in x)]
    print(trump)
    print('After looking at the output rows, even the lowercase "trump" are all relevant to "Trump" ! ')

    trumped =  comments[comments["content"].apply(lambda x : bool(re.search("\wTrump\w", x)))]
    print(trumped)
    print('After looking at the output rows, even the "Trump" with alphanumeric characters before or after are also relevant to "Trump" ! ')

 

    
