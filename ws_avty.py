#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt

list_date = ['january', 'february', 'march',
'april', 'may', 'june', 'juily', 'august', 
'september', 'october', 'november', 'december']

list_2011 = []

list_2016 = []

list_2020 = []

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'ro--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'co-')
    plt.ylabel('T°C')
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.title('Comparison of temperatures by year')
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()