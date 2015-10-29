# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:43:57 2015

@author: abdul
"""

import sys
import string

def mapper():
    for line in sys.stdin:
        data = line.strip().split(" ");
        
        for i in data:
            key = i.translate(str.maketrans("","",string.punctuation)).lower();
            if len(key) == 0:
                continue;
            print("{0}\t{1}".format(key,1));
            
mapper();