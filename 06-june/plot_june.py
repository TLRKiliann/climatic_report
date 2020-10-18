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
'28', '29', '30']

list_2011 = [11,16,19,20,19,18,18,12,15,16,13,18,18,19,21,22,20,13,14,19,23,21,16,16,20,24,21,26,21,17]

list_2016 = [16,13,16,17,18,19,20,19,18,14,17,15,16,13,11,19,16,16,15,18,18,23,25,25,20,18,19,21,23,21]

list_2020 = [21,22,21,16,14,17,12,17,13,14,18,21,19,16,17,18,17,18,17,20,20,22,23,25,25,25,25,22,22,23]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'mo-')
    plt.ylabel('Temperatures (°C)', fontsize=14)
    plt.xlabel('Days', fontsize=14)
    plt.xticks(rotation=45)
    plt.title('Temperatures for June 2011-2016-2020 (after-noon)',
    	fontsize=16)
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()