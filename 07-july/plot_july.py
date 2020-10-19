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

list_2011 = [17,16,18,21,23,22,21,21,23,21,22,26,20,16,17,20,14,15,16,15,16,18,15,13,17,18,18,18,19,18,18]

list_2016 = [23,18,20,22,22,21,23,25,24,26,24,19,15,13,17,19,23,21,22,22,21,21,20,21,21,22,23,22,24,26,21]

list_2020 = [26,21,19,21,23,20,21,24,26,24,21,21,23,21,17,19,20,21,24,26,23,24,24,21,23,24,26,27,25,27,29]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'ro-')
    plt.ylabel('Temperatures (°C)', fontsize=14)
    plt.xlabel('Days', fontsize=14)
    plt.xticks(rotation=45)
    plt.title('Temperatures for July 2011-2016-2020 (after-noon)',
    	fontsize=16)
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()