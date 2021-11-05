import argparse
import json

# python src/collect_title_lengths.py -file sample1.json 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='Sample file (only json)', required=True)
    args = parser.parse_args()

    title_len = []
    with open(args.f) as f:
        for line in f:
            post = json.loads(line)
            title_len.append(len(post['data']['title']))
    print(sum(title_len)//len(title_len))

if __name__ == '__main__':
    main()