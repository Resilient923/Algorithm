import numpy as np
def perceptron(x,w,b):
    weigthed_sum = np.dot(w,x)+b
    
    if weigthed_sum>=0:
        a = 1
    else:
        a = 0
    return a
def and_gate(x1,x2):
    w = np.array([2,2])
    x = np.array([x1,x2])
    b = -3
    return perceptron(w,x,b)
in_zero = 0
in_one =1 
print("{} AND {} is {}".format(in_zero,in_zero,and_gate(in_zero,in_zero)))