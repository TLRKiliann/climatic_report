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

list_2011 = [17,19,13,14,17,19,21,20,21,19,20,17,18,16,10,13,17,19,19,19,19,20,20,22,21,22,13,16,17,17,15]

list_2016 = [7,13,12,14,16,17,17,18,18,18,16,12,14,13,11,12,14,16,15,15,16,19,9,12,16,14,18,17,15,14,16]

list_2020 = [11,12,15,20,16,15,19,21,21,20,14,12,15,15,13,13,18,20,20,21,22,23,17,17,18,19,19,20,18,17,18]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'ro-')
    plt.ylabel('Temperatures (°C)', fontsize=14)
    plt.xlabel('Days', fontsize=14)
    plt.xticks(rotation=45)
    plt.title('Temperatures for May 2011-2016-2020 (after-noon)',
    	fontsize=16)
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()