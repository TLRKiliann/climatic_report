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

list_2011 = [17,19,18,10,14,18,21,19,20,18,18,9,9,9,10,13,14,17,17,19,19,19,18,15,18,15,14,12,13,15]

list_2016 = [11,17,16,13,13,12,9,7,8,13,14,15,12,12,11,11,13,12,11,12,18,14,11,6,6,8,6,10,13,12]

list_2020 = [10,10,11,13,15,16,16,18,18,19,19,18,16,12,17,18,18,18,18,15,17,18,18,19,19,16,17,12,14,10]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'mo-')
    plt.ylabel('Temperatures (°C)', fontsize=14)
    plt.xlabel('Days', fontsize=14)
    plt.xticks(rotation=45)
    plt.title('Temperatures for April 2011-2016-2020 (after-noon)',
    	fontsize=16)
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()