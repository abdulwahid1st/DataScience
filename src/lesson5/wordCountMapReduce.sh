# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:03:02 2015

@author: abdul
"""

#! /bin/bash

cat data/aliceInWonderland.txt | python wordCountMapper.py | sort | python wordCountReducer.py