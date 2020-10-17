#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt


list_date = ['january', 'february', 'march',
'april', 'may', 'june', 'juily', 'august',
'september', 'october', 'november', 'december']

list_2011 = [27, 18, 33, 28, 67, 93, 75, 51, 44, 34, 3, 150]

list_2016 = [80, 69, 53, 34, 63, 70, 58, 39, 25, 29, 46, 1]

list_2020 = [117, 244, 190, 88, 163, 291, 200, 247, 143, None, None, None]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'ro--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'co-')
    plt.ylabel('Total precipitations (mm)')
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.title('Total precipitations by MONTH (mm)')
    plt.legend(['2011', '2016', '2020'])
    plt.grid(show_grid)

    plt.show()
