#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt

list_date = ['01/01', '02/01', '03/01',
'04/01', '05/01', '06/01', '07/01',
'08/01', '09/01', '10/01', '11/01',
'12/01', '13/01', '14/01', '15/01',
'16/01', '17/01', '18/01', '19/01',
'20/01', '21/01', '22/01', '23/01',
'24/01', '25/01', '26/01', '27/01',
'28/01', '29/01', '30/01', '31/01']

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
    plt.title('Comparison of temperatures for january after-noon')
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()