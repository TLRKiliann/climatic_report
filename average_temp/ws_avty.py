#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import date2num
from matplotlib.dates import AutoDateLocator
from matplotlib.dates import AutoDateFormatter
import datetime


list_date = ['Jan', 'Feb', 'Mar',
'Apr', 'May', 'Jun', 'Jul', 'Aug',
'Sep', 'Oct', 'Nov', 'Dec']

list_2011 = [0, 2, 5, 10, 12, 13, 13, 16, 14, 8, 5, 2]

list_2016 = [4, 5, 5, 9, 12, 15, 18, 19, 17, 10, 7, 5]

list_2020 = [6, 7, 7, 13, 14, 16, 20, 20, 17, None, None, None]

converted_dates = list(map(datetime.datetime.strptime, list_date, len(list_date)*['%b']))
x_axis = converted_dates
formatter = dates.DateFormatter('%b')
b_axis = list_2011
c_axis = list_2016
y_axis = list_2020

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    figure, axes = plt.subplots()
    # apply autoformatter for displaying of dates 
    locator = AutoDateLocator()
    axes.xaxis.set_major_locator(locator)
    ax = plt.gcf().axes[0]
    ax.xaxis.set_major_formatter(formatter)
    #axes.xaxis.set_major_formatter(AutoDateFormatter(locator))
    #min_date = date2num(datetime.datetime.strptime('01-01', "%d-%m"))
    #max_date = date2num(datetime.datetime.strptime('01-12', "%d-%m"))
    #axes.set_xlim([min_date, max_date])
    #figure.autofmt_xdate()

    plt.plot(x_axis, b_axis, 'o--', color='cyan')
    plt.plot(x_axis, c_axis, 'o--', color='blue')
    plt.plot(x_axis, y_axis, 'o-', color='red')
    plt.ylabel('Average Of Temperatures (°C)', fontsize=14)
    plt.xlabel('Months', fontsize=14)
    plt.title('Average of temperatures for 2011-2016-2020',
        fontsize=16)
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()
