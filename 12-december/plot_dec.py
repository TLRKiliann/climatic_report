#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt

list_date = ['01/12', '02/12', '03/12',
'04/12', '05/12', '06/12', '07/12',
'08/12', '09/12', '10/12', '11/12',
'12/12', '13/12', '14/12', '15/12',
'16/12', '17/12', '18/12', '19/12',
'20/12', '21/12', '22/12', '23/12',
'24/12', '25/12', '26/12', '27/12',
'28/12', '29/12', '30/12', '31/12']

list_2011 = []

list_2016 = []

list_2020 = []

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'ro--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'co--')
    plt.ylabel('T°C')
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.title('Comparison of temperatures for january after-noon')
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()