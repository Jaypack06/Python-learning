import numpy as np

np.random.seed(1350)

def problem1():
    arr1 = np.arange(10,51,5)
    print(arr1)

    arr2 = np.zeros((3,4))
    print(arr2)
    
    identity = np.eye(3)
    print(identity)
    
    linespace_arr = np.linspace(0,5,10)
    print(linespace_arr)
    
    random_arr = np.random.rand(2,5)
    print(random_arr)
problem1()
