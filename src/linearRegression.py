# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:30:43 2015

@author: abdul
"""

import numpy as np
from numpy import matrix
import pandas as pd

def computeCost(X, y, theta):
    '''
    X is matrix of [m,n]
    theta is matrix of [n,1]
    y is matrix of [m,1]
    '''
    J = 0;
    m = y.shape[0];
    H = X*theta;
    sumOfSquareErrors = np.square(H-y).sum();
    J = sumOfSquareErrors / (2*m);
    return J;

def gradientDescent(X, y, theta, alpha = 1, nIteration = 20):
    '''
    X is matrix of [m,n]
    theta is matrix of [n,1]
    y is matrix of [m,1]
    alpha is learning rate of float
    nIteration is the number of iteration in int
    '''
    m = y.shape[0];
    JHistory = [];
    
    for i in range(nIteration):
        h = X*theta;
        delta = (1/m) * X.T * (h-y);
        theta = theta - alpha * delta;
        
        J = computeCost(X,y,theta);
        JHistory.append(J);
    
    return theta, pd.Series(JHistory);

if __name__ == '__main__':
    data = pd.read_csv('../../data/baseball_data.csv');
    X = matrix(data[['height', 'weight']]);
    y = matrix(data[['HR']]);