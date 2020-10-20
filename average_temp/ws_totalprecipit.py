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

list_2011 = [27, 18, 33, 28, 67, 93, 75, 51, 44, 34, 3, 150]

list_2016 = [80, 69, 53, 34, 63, 70, 58, 39, 25, 29, 46, 1]

list_2020 = [117, 244, 190, 88, 163, 291, 200, 247, 143, None, None, None]

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
    min_date = date2num(datetime.datetime.strptime('Jan', "%b"))
    max_date = date2num(datetime.datetime.strptime('Dec', "%b"))
    axes.set_xlim([min_date, max_date])
    #figure.autofmt_xdate()

    plt.plot(x_axis, b_axis, 'o--', color='cyan')
    plt.plot(x_axis, c_axis, 'o--', color='blue')
    plt.plot(x_axis, y_axis, 'o-', color='red')
    plt.ylabel('Total precipitations (mm)', fontsize=14)
    plt.xlabel('Months', fontsize=14)
    plt.title('Total precipitations 2011-2016-2020 (mm)', fontsize=16)
    plt.legend(['2011', '2016', '2020'])
    plt.grid(show_grid)
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()
