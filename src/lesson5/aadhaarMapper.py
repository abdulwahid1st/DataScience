# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:07:48 2015

@author: abdul
"""

import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(",");
        if len(data) != 12 or data[0] == "Registrar": continue;
        print("{0}\t{1}".format(data[3], data[8]));
        
mapper();