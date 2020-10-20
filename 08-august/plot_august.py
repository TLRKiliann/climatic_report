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

list_2011 = [21,24,21,22,22,20,19,16,15,17,20,20,22,22,20,22,25,
26,25,26,28,29,27,26,24,25,14,18,18,19,22]

list_2016 = [21,22,25,25,17,20,22,24,18,16,17,21,24,25,24,24,24,
20,23,19,18,21,24,26,26,27,26,26,20,21,23]

list_2020 = [28,22,16,17,21,24,27,29,29,28,27,27,26,23,25,25,22,
22,23,27,28,22,21,21,23,24,22,21,14,15,16]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'mo-')
    plt.ylabel('Temperatures (°C)', fontsize=14)
    plt.xlabel('Days', fontsize=14)
    plt.xticks(rotation=45)
    plt.title('Temperatures for August 2011-2016-2020 (after-noon)',
    	fontsize=16)
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()