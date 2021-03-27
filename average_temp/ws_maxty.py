#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt


list_date = ['january', 'february', 'march',
'april', 'may', 'june', 'juily', 'august', 
'september', 'october', 'november', 'december']

list_2011 = [3, 6, 9, 16, 18, 19, 19, 22, 19, 13, 10, 4]

list_2016 = [6, 7, 8, 12, 15, 18, 22, 23, 20, 13, 9, 8]

list_2020 = [8, 10, 10, 16, 18, 20, 23, 24, 21, 13, 11, 6]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'ro-')
    plt.ylabel('T°C MAX')
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.title('Maximum of temperatures by MONTH')
    plt.legend(['max temp 2011', 'max temp 2016', 'max temp 2020'])
    plt.grid(show_grid)

    plt.show()
