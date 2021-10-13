from datetime import datetime
import pandas as pd
import csv    
import string
import datetime as dt

if __name__ == '__main__':
    # with open("data/nyc_311_limit.csv", 'r') as infile:
    #     reader = csv.DictReader(infile)
    #     fieldnames = reader.fieldnames
    #     print(fieldnames)
    # date = dt.datetime.strptime('07/20/2020 10:51:12 AM', '%m/%d/%Y %H:%M:%S %p')
    # print(date)
    cols = range(1,42)
    print(cols)
    data = pd.read_csv("data/trimed.csv", usecols=[0,1,2,8], parse_dates=[1,2], names = ['unique_key', 'created_date', 'closed_date', 'zipcode' ], index_col=False)
    print(len(data))
    data = data.dropna()
    print(len(data))
    data = data.loc[data["closed_date"] >= data["created_date"]]
    print(len(data))

    
