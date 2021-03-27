#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt


list_date = ['01', '02', '03',
'04', '05', '06', '07',
'08', '09', '10', '11',
'12', '13', '14', '15',
'16', '17', '18', '19',
'20', '21', '22', '23',
'24', '25', '26', '27',
'28', '29', '30', '31']

list_2011 = [20,19,20,19,17,18,10,6,10,14,17,16,13,11,13,13,12,14,
9,7,6,9,9,10,13,11,12,14,14,13,13]

list_2016 = [16,14,15,14,12,11,13,11,9,9,8,9,8,13,15,16,13,12,10,9,
9,11,10,18,14,14,12,16,14,13,13]

list_2020 = [15,16,12,14,11,13,14,16,17,13,10,9,10,8,10,10,10,13,15,
17,14,13,14,15,11,10,14,12,16,16]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'ro-')
    plt.ylabel('Temperatures (°C)', fontsize=14)
    plt.xlabel('Days', fontsize=14)
    plt.xticks(rotation=45)
    plt.title('Temperatures for September 2011-2016-2020 (after-noon)',
        fontsize=16)
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()
