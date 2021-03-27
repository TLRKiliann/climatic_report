#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt


list_date = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
'jui', 'aug', 'sep', 'oct', 'nov', 'dec']

list_2011 = [0, 2, 5, 10, 12, 13, 13, 16, 14, 8, 5, 2]

list_2016 = [4, 5, 5, 9, 12, 15, 18, 19, 17, 10, 7, 5]

list_2020 = [6, 7, 7, 13, 14, 16, 20, 20, 17, 11, 9, 5]

precip_2011 = [27, 18, 33, 28, 67, 93, 75, 51, 44, 34, 3, 150]

precip_2016 = [80, 69, 53, 34, 63, 70, 58, 39, 25, 29, 46, 1]

precip_2020 = [117, 244, 190, 88, 163, 291, 200, 247, 143, 297, 55, 251]

style = dict(color="C4", linewidth=1, linestyle='--', marker='.', mec="C5")
style2 = dict(color="C4", linewidth=1, linestyle='--', marker='.', mec="C6")
style3 = dict(color="C4", linewidth=1, linestyle='--', marker='.', mec="C9")
style4 = dict(color="C4", linewidth=1, linestyle='--', marker='.', mec="C5")
style5 = dict(color="C4", linewidth=1, linestyle='--', marker='.', mec="C6")
style6 = dict(color="C4", linewidth=1, linestyle='--', marker='.', mec="C9")

with plt.style.context(("seaborn-darkgrid")):
    fig, (axes, axes2) = plt.subplots(2, 3, constrained_layout=True)
    #fig.set_size_inches(5, 5)

    axes[0].plot(list_date, list_2011, **style)
    #axes[0].set_xlabel('Dates', fontsize=12)
    axes[0].set_ylabel('Average of temperatures (°C)', fontsize=12)
    axes[0].set_title('2011')
    axes[0].legend(['2011']) 
    axes[0].grid(color='w', linestyle='-', linewidth=1)

    axes[1].plot(list_date, list_2016, **style2)
    #axes[1].set_xlabel('Dates', fontsize=12)
    axes[1].set_title('2016')
    axes[1].legend(['2016']) 
    axes[1].grid(color='w', linestyle='-', linewidth=1)

    axes[2].plot(list_date, list_2020, **style3)
    #axes[2].set_xlabel('Dates', fontsize=12)
    axes[2].set_title('2020')
    axes[2].legend(['2020']) 
    axes[2].grid(color='w', linestyle='-', linewidth=1)

    axes2[0].plot(list_date, precip_2011, **style4)
    axes2[0].set_xlabel('Dates', fontsize=12)
    axes2[0].set_ylabel('Total precipitations (mm)', fontsize=12)
    #axes2[0].set_title('2011')
    axes2[0].legend(['2011']) 
    axes2[0].grid(color='w', linestyle='-', linewidth=1)

    axes2[1].plot(list_date, precip_2016, **style5)
    axes2[1].set_xlabel('Dates', fontsize=12)
    #axes2[1].set_title('2016')
    axes2[1].legend(['2016']) 
    axes2[1].grid(color='w', linestyle='-', linewidth=1)

    axes2[2].plot(list_date, precip_2020, **style6)
    axes2[2].set_xlabel('Dates', fontsize=12)
    #axes2[2].set_title('2020')
    axes2[2].legend(['2020']) 
    axes2[2].grid(color='w', linestyle='-', linewidth=1)

    plt.show()
