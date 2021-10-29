import argparse
import os, sys, json
from zipfile import ZipFile
from datetime import datetime
import pytz
from dateutil.parser import isoparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', help='input file(JSON file)', required=True)
parser.add_argument('-o', help='output file(JSON file)', required=True)
args = parser.parse_args()
INPUTFILE = '{}'.format(args.i) 
OUTPUTFILE = '{}'.format(args.o) 

def clean(json_lst, output):
    pos = 0
    if not json_lst:
        open(output, "w").close()
        return
    for line in json_lst:
        #1
        if "title" in line or "title_text" in line:
            if "title_text" in line:
                line["title"] = line.pop("title_text")   
        else:
            #print("delete for #1")
            continue
        #2
        try:
            dt = isoparse(line["createdAt"])
        except Exception as e:
            #print("delete for #2")
            #print(e)
            continue
        else:
            line["createdAt"] = dt.replace().astimezone(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
        
        #3
        if not line["author"] or line["author"].casefold() == 'N/A'.casefold() or line["author"].casefold() == 'null'.casefold():
            #print("delete for #3")
            continue
        #4
        if 'total_count' in line:
            if not (type(line['total_count']) == int or type(line['total_count']) == str or type(line['total_count']) == float):
                #print("delete for #4")
                continue
            try:
                int(line['total_count'])
            except:
                #print("delete for #4")
                continue
            else:
                line['total_count'] = int(line['total_count'])
        
        if 'tags' in line:
            temp = []
            for i in line['tags']:
                temp = temp + i.split()
            line['tags'] = temp

        json_lst[pos] = line
        pos +=1
    
    del json_lst[pos:]
    with open(output, 'w') as f:
        for line in json_lst:
            f.write(json.dumps(line))
    return  

def main():
    input_lst = []
    with open (INPUTFILE, 'r') as file:
        for line in file:
            try:
                json.loads(line)
            except:
                continue
            else:
                input_lst.append(json.loads(line))

    clean(input_lst, OUTPUTFILE)
    


if __name__ == "__main__":
    main()

