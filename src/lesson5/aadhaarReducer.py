# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:14:15 2015

@author: abdul
"""

import sys
import string

def reducer():
    #aadhaarGenerated
    count = 0;
    key = None;
    
    for line in sys.stdin:
        data = line.strip().split("\t");
        
        if len(data) != 2: continue;
        keyTemp, countTemp = data;
        
        if key != None and key != keyTemp:
            print("{0}\t{1}".format(key, count));
            count = 0;
        
        key = keyTemp;
        count += float(countTemp);
    
    if key != None:
        print("{0}\t{1}".format(key, count));

reducer();        