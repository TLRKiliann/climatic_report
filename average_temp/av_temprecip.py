#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt
#import seaborn as sns


list_date = ['01', '02', '03', '04', '05', '06', '07',
'08', '09', '10', '11', '12', '13', '14', '15', '16', 
'17', '18', '19', '20', '21', '22', '23', '24', '25', 
'26', '27', '28', '29', '30', '31']

list_2011 = [1, -1, -3, -3, 1, 5, 7, 10, 5, 4, 3, 5, 9, 9, 8, 
9, 7, 7, 2, -1, -3, -5, -5, -2, -1, 1, 1, 1, 2, 0, 0]

list_2016 = [6, 5, 6, 5, 6, 5, 7, 8, 8, 8, 8, 5, 3, 4, 2, 
0, 0, -3, 2, 3, 0, 4, 6, 7, 9, 9, 9, 10, 9, 9, 9]

list_2020 = [8, 8, 9, 8, 5, 9, 8, 8, 10, 8, 6, 7, 8, 9, 9, 
10, 8, 6, 3, 3, 5, 8, 5, 8, 8, 6, 9, 8, 5, 8, 11]

style = dict(color="C4", linewidth=1, linestyle='--', marker='.', mec="C5")
style2 = dict(color="C4", linewidth=1, linestyle='--', marker='.', mec="C6")
style3 = dict(color="C4", linewidth=1, linestyle='--', marker='.', mec="C9")

with plt.style.context(("seaborn-darkgrid",)):
    fig, axes = plt.subplots(1, 3, constrained_layout=True)
    fig.set_size_inches(5, 5)
    #sns.axes_style('dark')

    axes[0].plot(list_date, list_2011, **style)
    axes[0].set_xlabel('Days of january', fontsize=12)
    axes[0].set_ylabel('Temperatures (°C)', fontsize=12)
    axes[0].set_title('2011')
    axes[0].grid(color='w', linestyle='-', linewidth=1)

    axes[1].plot(list_date, list_2016, **style2)
    axes[1].set_xlabel('Days of january', fontsize=12)
    axes[1].set_title('2016')
    axes[1].grid(color='w', linestyle='-', linewidth=1)

    axes[2].plot(list_date, list_2020, **style3)
    axes[2].set_xlabel('Days of january', fontsize=12)
    axes[2].set_title('2020')
    axes[2].grid(color='w', linestyle='-', linewidth=1)

    plt.show()




list_date = ['january', 'february', 'march',
'april', 'may', 'june', 'juily', 'august', 
'september', 'october', 'november', 'december']

list_2011 = [0, 2, 5, 10, 12, 13, 13, 16, 14, 8, 5, 2]

list_2016 = [4, 5, 5, 9, 12, 15, 18, 19, 17, 10, 7, 5]

list_2020 = [6, 7, 7, 13, 14, 16, 20, 20, 17, None, None, None]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'ro-')
    plt.ylabel('T°C')
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.title('Average of temperatures by MONTH')
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()

list_2011 = [27, 18, 33, 28, 67, 93, 75, 51, 44, 34, 3, 150]

list_2016 = [80, 69, 53, 34, 63, 70, 58, 39, 25, 29, 46, 1]

list_2020 = [117, 244, 190, 88, 163, 291, 200, 247, 143, None, None, None]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'ro-')
    plt.ylabel('Total precipitations (mm)')
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.title('Total precipitations by MONTH (mm)')
    plt.legend(['2011', '2016', '2020'])
    plt.grid(show_grid)

    plt.show()