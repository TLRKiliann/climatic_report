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
'28', '29']

list_2011 = [0,0,2,6,8,10,11,9,8,9,11,8,8,8,5,4,6,6,6,3,3,2,2,3,5,5,4,2, None]

list_2016 = [11,11,7,4,9,9,7,8,9,3,3,4,7,6,2,3,4,5,3,7,11,13,7,6,6,3,7,7,5]

list_2020 = [11,11,13,11,6,5,9,10,10,11,9,6,8,8,11,13,11,7,5,9,9,12,14,13,10,3,5,6,12]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'mo-')
    plt.ylabel('Temperatures (°C)', fontsize=14)
    plt.xlabel('Days', fontsize=14)
    plt.xticks(rotation=45)
    plt.title('Temperatures for February 2011-2016-2020 (after-noon)',
    	fontsize=16)
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()
