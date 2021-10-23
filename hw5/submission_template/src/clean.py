import argparse
import os, sys, json
from zipfile import ZipFile


parser = argparse.ArgumentParser()
parser.add_argument('-i', help='input file(JSON file)', required=True)
parser.add_argument('-o', help='output file(JSON file)', required=True)
args = parser.parse_args()
INPUTFILE = '{}'.format(args.i) 
OUTPUTFILE = '{}'.format(args.i) 

def clean(input, output):
    for i in input:
        print(i)
    return
def main():
    f = open(INPUTFILE)
    input =  json.load(f)
    clean(input, OUTPUTFILE)
    print(f"{OUTPUTFILE} file created successfully >3<")


if __name__ == "__main__":
    main()

