# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:47:32 2015

@author: abdul
"""

import numpy as np
from numpy import matrix
import pandas as pd

import gradientDescent


if __name__ == "__main__":
    data = pd.read_csv('../../data/ex1data2.txt', header=None);
    X = matrix(data[[0, 1]]);
    y = matrix(data[[2]]);
    
    XNorm, mu, std = gradientDescent.featureNormalization(X);
    ones = np.ones(y.shape);
    XNorm = np.hstack((ones,XNorm));
    
    theta = np.zeros([XNorm.shape[1],1]);
    result = gradientDescent.gradientDescent(XNorm, y, theta, 0.01, 1000);