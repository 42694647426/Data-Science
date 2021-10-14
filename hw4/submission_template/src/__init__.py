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
    # cols = range(1,42)
    # print(cols)
    # data = pd.read_csv("data/trimed.csv", usecols=[0,1,2,8], parse_dates=[1,2], names = ['unique_key', 'created_date', 'closed_date', 'zipcode' ],dtype={'zipcode': int}, index_col=False)
    # print(data.head())
    # data = data.dropna()
    # print(len(data))
    # data = data.loc[data["closed_date"] >= data["created_date"]]
    # print(len(data))
    # data.to_csv("data/clean_data.csv", index=False)
    data = pd.read_csv("data/clean_data.csv")
    data['created_date'] = pd.to_datetime(data['created_date'])
    data['closed_date'] = pd.to_datetime(data['closed_date'] )
    data['zipcode'] = data['zipcode'].astype(str)
    zipcode = 11210
    #zip_data = data.loc[data['zipcode'] == zipcode]
    zip_data = data
    print(zip_data)
    month = zip_data.closed_date.dt.to_period("M")
    group_by_month =  zip_data.assign(diff_h=(zip_data.closed_date - zip_data.created_date).dt.total_seconds()/3600)
    print(group_by_month.head())
    group_by_month = group_by_month.groupby(month)['closed_date', 'diff_h'].mean()
    print(group_by_month)
    group_by_month.plot.line()
    

    
