# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:19:27 2015

@author: abdul
"""

import pandas as pd
from ggplot import *

def lineplot():
    data = pd.read_csv('../../data/hr_year.csv');
    plot = ggplot(data, aes('yearID', 'HR')) +\
        geom_point(color='red') +\
        geom_line(color='red') +\
        ggtitle('Total HRs by Year') +\
        xlab('YEAR') +\
        ylab('HR');
    print(plot);

if __name__ == '__main__':
    lineplot();