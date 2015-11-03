# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:48:40 2015

@author: abdul
"""

import pandas as pd;

def parseFile():
    data = pd.read_csv("data/beatles-diskography.csv", nrows=10);
    data = data.fillna("");
    data = data.T.to_dict();
    return data;

def test():
    d = parseFile();
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

test()