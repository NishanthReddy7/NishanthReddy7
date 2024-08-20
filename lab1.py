from array import array
from numpy import random
import time
import matplotlib.pyplot as plt

# Question 1
"""print("Enter the number of elements: ")
n = int(input())
list1 = []

for i in range(n):
    x = int(input("Enter the next value: "))
    list1.append(x)

def Insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

Insertion_sort(list1, n)
print(list1)
"""
"""

def Insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

print("Enter the number of elements: ")
n = int(input())
list1 = []

for i in range(n):
    x = int(input("Enter the next value: "))
    list1.append(x)

# Measure time complexity
start_time = time.time()
Insertion_sort(list1, n)
end_time = time.time()
execution_time = end_time - start_time

print("Sorted list:", list1)
print("Execution time:", execution_time)

# Plot time complexity graph
sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
times = []

for size in sizes:
    list1 = [random.randint(0, 100) for _ in range(size)]
    start_time = time.time()
    Insertion_sort(list1, size)
    end_time = time.time()
    execution_time = end_time - start_time
    times.append(execution_time)

plt.plot(sizes, times)
plt.xlabel("Input size (n)")
plt.ylabel("Execution time (seconds)")
plt.title("Time Complexity of Insertion Sort")
plt.show()
"""
# Question 2
"""
def traditional_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def improved_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid
        j = i - 1
        while j >= left:
            arr[j + 1] = arr[j]
            j -= 1
        arr[left] = key
    return arr

# Generating a random array to get better results


print("Enter the number of elements")
n = 1000
arr = [random.randint(0, 100) for _ in range(n)]

print("Original array:")
print(arr)

# Measuring time complexity
start_time = time.time()
traditional_sorted_arr = traditional_insertion_sort(arr.copy())
traditional_time = time.time() - start_time
print("\nTraditional Insertion Sort:")
print(traditional_sorted_arr)
print(f"Time: {traditional_time:.6f} seconds")

start_time = time.time()
improved_sorted_arr = improved_insertion_sort(arr.copy())
improved_time = time.time() - start_time
print("\nImproved Insertion Sort:")
print(improved_sorted_arr)
print(f"Time: {improved_time:.6f} seconds")

# Plotting time complexity
plt.plot([traditional_time, improved_time])
plt.xlabel("Insertion Sort Variant")
plt.ylabel("Time (seconds)")
plt.title("Time Complexity Comparison")
plt.show()




sizes = [100, 1000, 5000, 10000]
traditional_times = []
improved_times = []

for size in sizes:
    arr = [random.randint(0, 100) for _ in range(size)]
    start_time = time.time()
    traditional_insertion_sort(arr.copy())
    traditional_time = time.time() - start_time
    traditional_times.append(traditional_time)

    start_time = time.time()
    improved_insertion_sort(arr.copy())
    improved_time = time.time() - start_time
    improved_times.append(improved_time)

plt.plot(sizes, traditional_times, label='Traditional Insertion Sort')
plt.plot(sizes, improved_times, label='Improved Insertion Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity Comparison')
plt.legend()
plt.show()
"""

# Question 3

print("Input 5 sorted lists of fixed size 4")
list1 = []
for i in range(4):
    x = int(input("Enter the next value(list1): "))
    list1.append(x)
print("This is the second array")
list2 = []
for i in range(4):
    x = int(input("Enter the next value(list2): "))
    list2.append(x)
print("This is the third array")
list3 = []
for i in range(4):
    x = int(input("Enter the next value(list3): "))
    list3.append(x)
print("This is the fourth array")
list4 = []
for i in range(4):
    x = int(input("Enter the next value(list4): "))
    list4.append(x)
print("This is the fifth array")
list5 = []
for i in range(4):
    x = int(input("Enter the next value(list5): "))
    list5.append(x)

def merge(list1, list2, list3, list4, list5):
    list1.extend(list2)
    list1.extend(list3)
    list1.extend(list4)
    list1.extend(list5)
    list1.sort()
    return list1

merge(list1, list2, list3, list4, list5)
print(list1)