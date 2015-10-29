# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:19:21 2015

@author: abdul
"""

#! /bin/bash

cat data/aadhaar_data.csv | python aadhaarMapper.py | sort | python aadhaarReducer.py