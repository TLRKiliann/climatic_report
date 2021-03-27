#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt

list_date = ['01/11', '02/11', '03/11',
'04/11', '05/11', '06/11', '07/11',
'08/11', '09/11', '10/11', '11/11',
'12/11', '13/11', '14/11', '15/11',
'16/11', '17/11', '18/11', '19/11',
'20/11', '21/11', '22/11', '23/11',
'24/11', '25/11', '26/11', '27/11',
'28/11', '29/11', '30/11']

list_2011 = [13,14,13,12,15,15,12,11,13,10,9,11,11,9,6,6,8,7,9,9,9,
9,8,5,7,7,10,7,9,10]

list_2016 = [16,12,9,13,13,7,3,3,5,6,6,4,7,4,7,10,11,10,9,12,12,12,
14,13,9,9,10,4,4,7]

list_2020 = [15,18,15,8,9,13,14,14,14,13,12,14,13,14,15,12,10,13,11,
6,5,8,8,10,9,9,9,7,3,4]

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