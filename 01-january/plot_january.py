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

list_2011 = [1, -1, -3, -3, 1, 5, 7, 10, 5, 4, 3, 5, 9, 9, 8, 
9, 7, 7, 2, -1, -3, -5, -5, -2, -1, 1, 1, 1, 2, 0, 0]

list_2016 = [6, 5, 6, 5, 6, 5, 7, 8, 8, 8, 8, 5, 3, 4, 2, 
0, 0, -3, 2, 3, 0, 4, 6, 7, 9, 9, 9, 10, 9, 9, 9]

list_2020 = [8, 8, 9, 8, 5, 9, 8, 8, 10, 8, 6, 7, 8, 9, 9, 
10, 8, 6, 3, 3, 5, 8, 5, 8, 8, 6, 9, 8, 5, 8, 11]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'ro-')
    plt.ylabel('Temperatures (°C)')
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.title('Temperatures for january 2011-2016-2020 (after-noon)')
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()
