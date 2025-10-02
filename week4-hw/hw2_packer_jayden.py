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

def problem2():
    arr_a = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
    arr_b = np.array([10, 20, 30])
    
    result_add = arr_a + arr_b
    
    result_multiply = arr_a * arr_b
    
    result_square = arr_a ** 2
    
    column_means = np.mean(arr_a, axis=0)
    
    centered_arr = arr_a - column_means
    
    return result_add, result_multiply, result_square, column_means, centered_arr
print(problem2())