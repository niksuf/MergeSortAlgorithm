from random import random, seed, randint
from time import time

def isSorted(array, size):                                                              # Проверка на упорядоченность
    for i in range (0, size - 1):
        if array[i] > array[i + 1]:
            return False
    return True

def printArray(array, size):                                                            # Вывод массива
    if isSorted(array, size):
        print('Sorted!')
    else:
        print('Unsorted!')
    for i in range (0, size):
        if i < 10: print(array[i], end = '\n')
        else: break
    print('\n')

def mergeSort(array, left, right):                                                      # Сортировка массива
    if left >= right:
        return
    mid = (left + right) // 2
    mergeSort(array, left, mid)
    mergeSort(array, mid + 1, right)
    merge(array, left, right, mid)

def merge(array, left, right, mid):
    left_copy = array[left:mid + 1]
    right_copy = array[mid + 1:right + 1]
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
        sorted_index += 1
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1
    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1

seed(time())                                                                            # Инициализация таймера
print('Input array size: ')
size = int(input())                                                                     # Размер массива
random_array = []
for i in range (0, size):                                                               # Заполнение массива случайными числами
    random_array.append(random() * size)
printArray(random_array, size)

l = 0
r = size - 1

t1 = time()
mergeSort(random_array, l, r)                                                           # Сортировка
t2 = time()
elapsed = 1000 * (t2-t1)                                                                # Время, затраченное на операцию, мс

printArray(random_array, size)
print('Time: ', elapsed, 'ms')
