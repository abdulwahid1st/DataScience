# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:49:49 2015

@author: abdul
"""

import sys

def reducer():
    
    count = 0;
    key = None;
    
    for line in sys.stdin:
        data = line.strip().split("\t");
        
        if len(data) != 2:
            continue;
        
        keyTemp, countTemp = data;
        if key != None and key != keyTemp:
            print("{0}\t{1}".format(key, count));
            count = 0;
        
        key = keyTemp;
        count += float(countTemp);
        
    if key != None:
        print("{0}\t{1}".format(key, count));

reducer();