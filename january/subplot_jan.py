#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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

fig, axes = plt.subplots(1,3)
fig.set_size_inches(5,5)

axes[0].plot(list_date, list_2011, **style)

axes[1].plot(list_date, list_2016, **style2)

axes[2].plot(list_date, list_2020, **style3)
plt.title('2020')

plt.show()

"""
show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'ro--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'co-')
    plt.ylabel('T°C')
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.title('Comparison of temperatures for january after-noon')
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()
"""