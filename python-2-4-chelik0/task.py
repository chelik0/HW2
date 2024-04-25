import numpy as np
import datetime


"""Напишите функцию, возвращающую нулевой вектор размера n 
с i-ым элементом равным 1"""
def task1(n, i):
    vec = np.array([0] * n)
    vec[i] = 1
    return vec

"""Напишите функцию, возвращающую вектор значений от a до b"""
def task2(a, b):
    return np.array([i for i in range(a, b)])


"""Напишите функцию, возвращающую матрицу размера n х n, заполненную числами от 0 до n^2 - 1"""
def task3(n):
    matrix = np.matrix([i for i in range(n * n)]).reshape(n, n)
    return matrix


"""Напишите функцию, возвращающую индексы ненулевых элементов из вектора v"""
def task4(v):
    tmp = list()
    for i in range(len(v)):
        if v[i] != 0:
            tmp.append(i)
    return(np.array(tmp))
            


"""Напишите функцию, возвращающую случайную матрицу размера n х n x n"""
def task5(n):
    pass


"""Напишите функцию, меняющую знак на противоположный у элементов, лежащих в диапазоне от a до b в векторе v"""
def task6(v, a, b):
    for i in range(a,b+1):
        v[i] = -v[i]
    return v


"""Напишите функцию, возвращающую вектор, состоящий из элементов, присутствующих в обоих векторах"""
def task7(v1, v2):
    set_1 = set(list(v1))
    set_2 = set(list(v2))
    all_in_one = set_1.intersection(set_2)
    return np.array(list(all_in_one))

print(task7(np.array([1, 2, 3, 4, 5]), np.array([3, 4, 5, 6, 7])),
task7(np.array([1, 2, 3, 4, 5]), np.array([6, 7, 8, 9, 10])),
task7(np.array([1, 2, 3, 4, 5]), np.array([5, 4, 3, 2, 1])),
task7(np.array([1, 2, 3, 4, 5]), np.array([1, 2, 3, 4, 5])))


"""Напишите функцию, возвращающую вектор дат, соответствующих месяцу m и году y"""
def task8(m, y):
    str_m = str(m)
    if len(str_m) == 1:
        str_m = f"0{m}"
    if m == 2:
        if y % 4 == 0:
            return np.array([datetime.date(y, m, i) for i in range(1, 30)])
        else:
            return np.array([datetime.date(y, m, i) for i in range(1, 29)])
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        return np.array([datetime.date(y, m, i) for i in range(1, 32)])
    else:
        return np.array([datetime.date(y, m, i) for i in range(1, 31)])