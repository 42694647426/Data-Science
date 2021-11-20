import argparse
import sys
import json
import math


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--counts')
    parser.add_argument('-n', '--num', type=int)
    args = parser.parse_args()

    with open(args.counts) as f:
        word_count_json = json.load(f)

    pony_num = len(word_count_json)

    num_pony_for_word = {}

    for pony in word_count_json:
        for w in word_count_json[pony]:
            if w in num_pony_for_word:
                num_pony_for_word[w] += 1
            else:
                num_pony_for_word[w] = 1

    output_dict = {}
    # tfidf
    for pony in word_count_json:
        
        tfidf_lst = []
        word_lst = []
        for w in word_count_json[pony]:
            idf = math.log10(pony_num/num_pony_for_word[w])
            tfidf = word_count_json[pony][w] * idf
            
            if not tfidf_lst:
                tfidf_lst.append(tfidf)
                word_lst.append(w)
            else:
                i = 0
                while i < len(tfidf_lst) and i < args.num and tfidf <= tfidf_lst[i]:
                    i += 1
                if i < args.num:
                    tfidf_lst.insert(i, tfidf)
                    word_lst.insert(i, w)
                
                if len(tfidf_lst) > args.num:
                    del tfidf_lst[-1]
                    del word_lst[-1]
                    
        output_dict[pony] = word_lst


    print(output_dict)
    


if __name__ == '__main__':
    main()
    
