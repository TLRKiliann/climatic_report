#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt


list_date = ['january', 'february', 'march',
'april', 'may', 'june', 'juily', 'august', 
'september', 'october', 'november', 'december']

list_2011 = [0, 2, 5, 10, 12, 13, 13, 16, 14, 8, 5, 2]

list_2016 = [4, 5, 5, 9, 12, 15, 18, 19, 17, 10, 7, 5]

list_2020 = [6, 7, 7, 13, 14, 16, 20, 20, 17, None, None, None]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'ro--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'co-')
    plt.ylabel('T°C')
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.title('Average of temperatures by month')
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()
