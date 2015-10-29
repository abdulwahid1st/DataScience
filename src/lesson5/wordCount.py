# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:51:29 2015

@author: abdul
"""

import sys
import string


def wordCount():
    wordCount = {};
    
#    for line in input("Enter the line:"):
    for line in sys.stdin:
        if len(line) == 0:
            continue;
        data = line.strip().split(" ");
        
        for i in data:
            if len(i) == 0:
                continue;
            key = i.translate(str.maketrans("","",string.punctuation)).lower();
            if len(key) == 0:
                continue;
            
            if key in wordCount.keys():
                wordCount[key] += 1;
            else:
                wordCount[key] = 1;
        
    print(wordCount);

if __name__ == "__main__":
    wordCount();