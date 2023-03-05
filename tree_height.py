# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    height = 0 [0] * n
    max_height = 0
    for i in range(n):
        node = i
        while node != -1:
            if height[node] != 0:
                height[i] = height[node] + 1
                break
            node = parents[node]
        if height[i] == 0:
            height[i] = 1
        if height[i] > max_height:
            max_height = height[i]
    return max_height


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
