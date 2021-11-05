import os
import argparse
import re
import bs4
import json
import requests

BASE_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.join(BASE_DIR, '..')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', required=True)
    parser.add_argument('-o', required=True)
    args = parser.parse_args()
    
    output = {}
    with open(args.c) as f:
        config = json.load(f)

    CACHE_DIR = os.path.join(PARENT_DIR, config['cache_dir'])
    if not os.path.isdir(CACHE_DIR):
        os.mkdir(CACHE_DIR)
    
    for person in config['target_people']:
        output[person] = []
        CACHE_PATH = os.path.join(CACHE_DIR, f"{person}.html")

        if not os.path.isfile(CACHE_PATH):
            response = requests.get(f'https://www.whosdatedwho.com/dating/{person}')
            
            with open(CACHE_PATH, 'w') as f:
                f.write(response.text)
        
        with open(CACHE_PATH) as f:
            name = person.split('-')

            soup = bs4.BeautifulSoup(f.read(), 'html.parser')

            status_heading = soup.find('h4', class_='ff-auto-status')
            status = status_heading.next_sibling
            output[person] += person_relation(status, name)

            relationship_heading = soup.find('h4', class_='ff-auto-relationships')
            cur_person = relationship_heading.next_sibling
            while cur_person.name == 'p':
                output[person] += person_relation(cur_person, name)
                cur_person = cur_person.next_sibling

    with open(args.o, 'w') as f:
        json.dump(output, f)

def person_relation(sec, target):
    lst = []
    links = sec.find_all('a')
    for link in links:
        words = [re.sub(r'\W', '', s.lower()) for s in link.find(text=True).split()]
        if words != target and r'/dating/' in link['href']:
            lst.append(link['href'].strip(r'/dating/'))
    return lst
    
if __name__ == '__main__':
    main()