# myapp.py
from random import random
from bokeh.layouts import column, row
from bokeh.models import Button, sources
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc, show
import pandas as pd
from bokeh.io import show
from bokeh.models import CustomJS, Dropdown, Select
from bokeh.models import ColumnDataSource
from pandas._config.config import options

# create a plot and style its properties
data = pd.read_csv("/home/annas/comp598-2021/hw4/submission_template/data/clean_data.csv")

data['created_date'] = pd.to_datetime(data['created_date'])
data['closed_date'] = pd.to_datetime(data['closed_date'] )
data['zipcode'] = data['zipcode'].astype(str)
zipcodes = list(data.zipcode.unique())
zipcodes = sorted(zipcodes)
print(data.zipcode.dtypes)
print(data.closed_date.dtypes)
def get_average(data: pd.DataFrame, zipcode = None):
    if zipcode:
        zip_data = data.loc[data['zipcode'] == zipcode]
    else:
        zip_data = data
    month = zip_data.closed_date.dt.to_period("M")
    #group_by_month =  zip_data.assign(diff_h=(zip_data.closed_date - zip_data.created_date).dt.total_seconds()/3600)
    group_by_month = zip_data.groupby(month)['closed_date', 'diff_h'].mean()
    return group_by_month

dropdown1 = Select(title="Zipcode 1", options=zipcodes, value="")
dropdown2 = Select(title="Zipcode 2", options=zipcodes, value="")

source1, source2 = pd.DataFrame(columns=["closed_date", "diff_h"]), pd.DataFrame(columns=["closed_date", "diff_h"])
source1 = ColumnDataSource(source1)
source2 = ColumnDataSource(source2)

zipcode1, zipcode2 = "", ""
def on_click_handler1(attrname, old, new):
    zipcode1 = dropdown1.value
    zip1_graph = get_average(data, zipcode1)
    new_data = ColumnDataSource(zip1_graph)
    source1.data = dict(new_data.data)

def on_click_handler2(attrname, old, new):
    zipcode2 = dropdown2.value
    zip2_graph = get_average(data, zipcode2)
    new_data = ColumnDataSource(zip2_graph)
    source2.data = dict(new_data.data)

dropdown1.on_change('value', on_click_handler1)
dropdown2.on_change('value', on_click_handler2)

all_graph = get_average(data)
print(all_graph.head())
source = ColumnDataSource(all_graph)


p = figure(title="Average response hour", x_axis_label='month', y_axis_label='time(h)', x_axis_type='datetime')
p.line(x ="closed_date", y="diff_h", legend_label='all', line_width=2, source=source)
p.line(x ="closed_date", y="diff_h", legend_label="zipcode1", color = "orange", line_width=2, source=source1)
p.line(x ="closed_date", y="diff_h",legend_label="zipcode2", color = "green", line_width=2, source=source2)

# put the button and plot in a layout and add to the document
curdoc().add_root(row(column(dropdown1, dropdown2), p))