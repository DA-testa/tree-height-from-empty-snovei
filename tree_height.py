# python3

import sys
import threading
import numphy

def compute_height(n, parents):
    heights = [0] * n
    for node in range(n):
        if heights[node] != 0:
            continue
        if parents[node] == -1:
            heights[node] = 1
        else:
            parent_height = compute_height(parents[node], parents)
            heights[node] = parent_height + 1
    return max(heights)


def main():
   input_method = input("Enter input method (K for keyboard or F for file): ")
    while input_method.upper() not in ['K', 'F']:
        input_method = input("Invalid input method. Enter K or F: ")
    if input_method.upper() == 'K':
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parents array: ").split()))
    else:
        file_name = input("Enter file name (without 'a' in name): ")
        while 'a' in file_name or file_name.upper() == 'README':
            file_name = input("Invalid file name. Enter another name: ")
        try:
            with open('folder/' + file_name, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print("File not found.")
            return
    print("Tree height:", compute_height(n, parents))
    if __name__ == '__main__':
        sys.setrecursionlimit(10**7)  # max depth of recursion
        threading.stack_size(2**27)   # new thread will get stack of such size
        threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
