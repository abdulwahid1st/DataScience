# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 08:38:52 2015

@author: abdul
"""

import csv

def parseCsv():
    data = [];
    with open("data/beatles-diskography.csv") as f:
        r = csv.DictReader(f);
        for line in r:
            data.append(line);
            print(line);
    return data;

if __name__ == '__main__':
    data = parseCsv();
    