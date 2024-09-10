#!/usr/bin/env python
# coding: utf-8

# In[9]:


from time import time
import matplotlib.pyplot as plt
import random

def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A

X = [10, 50, 500, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 20000, 25000, 30000, 40000, 50000]  # Different sizes of lists to sort
Y = []  # To store time taken for each list size

for size in X:
    randomlist = random.sample(range(5, 50010), size)
    start_time = time()
    selection_sort(randomlist)
    end_time = time()
    elapsed = end_time - start_time
    Y.append(elapsed)

# Plotting
plt.plot(X, Y, marker='o')
plt.title('Selection Sort Performance on Random Order Arrays')
plt.xlabel('List Size')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.show()


# In[ ]:


from time import time
import matplotlib.pyplot as plt

def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A

X = [10, 50, 500, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 20000, 25000, 30000, 40000, 50000]  # Different sizes of lists to sort
Y_asc = []  # To store time taken for each list size in ascending order

for size in X:
    sortedlist_asc = list(range(5, 50010))  # Generating a perfectly sorted array in ascending order
    start_time = time()
    selection_sort(sortedlist_asc)
    end_time = time()
    elapsed = end_time - start_time
    Y_asc.append(elapsed)

# Plotting
plt.plot(X, Y_asc, marker='o')
plt.title('Selection Sort Performance on Ascending Order Sorted Arrays')
plt.xlabel('List Size')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.show()


# In[ ]:


from time import time
import matplotlib.pyplot as plt
import random

def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
    return A

X = [10, 50, 500, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 20000, 25000, 30000, 40000, 50000]  # Different sizes of lists to sort
Y = []  # To store time taken for each list size

for size in X:
    randomlist = random.sample(range(5, 50010), size)
    start_time = time()
    insertion_sort(randomlist)
    end_time = time()
    elapsed = end_time - start_time
    Y.append(elapsed)

# Plotting
plt.plot(X, Y, marker='o')
plt.title('Insertion Sort Performance on Random Order Arrays')
plt.xlabel('List Size')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.show()


# In[ ]:


from time import time
import matplotlib.pyplot as plt

def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
    return A

X = [10, 50, 500, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 20000, 25000, 30000, 40000, 50000]  # Different sizes of lists to sort
Y_asc = []  # To store time taken for ascending order sorted lists

for size in X:
    # Generating a perfectly sorted array in ascending order
    sortedlist_asc = list(range(5, 50010))
    start_time = time()
    insertion_sort(sortedlist_asc)
    end_time = time()
    elapsed = end_time - start_time
    Y_asc.append(elapsed)

# Plotting
plt.plot(X, Y_asc, marker='o')
plt.title('Insertion Sort Performance on Ascending Order Sorted Arrays')
plt.xlabel('List Size')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.show()


# In[ ]:


from time import time
import matplotlib.pyplot as plt
import random

def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        # Flag to detect any swap
        swapped = False
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                swapped = True
                A[j], A[j+1] = A[j+1], A[j]
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            return

X = [10, 50, 500, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 20000, 25000, 30000, 40000, 50000]  # Different sizes of lists to sort
Y = []  # To store time taken for each list size

for size in X:
    randomlist = random.sample(range(5, 50010), size)
    start_time = time()
    bubble_sort(randomlist)  # Corrected to use bubble_sort
    end_time = time()
    elapsed = end_time - start_time
    Y.append(elapsed)

# Plotting
plt.plot(X, Y, marker='o')
plt.title('Bubble Sort Performance on Random Order Arrays')
plt.xlabel('List Size')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.show()


# In[ ]:


from time import time
import matplotlib.pyplot as plt

def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        # Flag to detect any swap
        swapped = False
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                swapped = True
                A[j], A[j+1] = A[j+1], A[j]
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            return

X = [10, 50, 100, 500, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 20000, 25000, 30000, 40000, 50000]  # Different sizes of lists to sort, adjusted for demonstration
Y = []  # To store time taken for each list size

for size in X:
    # Generating a perfectly sorted array in ascending order
    sortedlist = list(range(5, 50010))
    start_time = time()
    bubble_sort(sortedlist)  # Sorting the already sorted array
    end_time = time()
    elapsed = end_time - start_time
    Y.append(elapsed)

# Plotting
plt.plot(X, Y, marker='o')
plt.title('Bubble Sort Performance on Sorted Arrays in Ascending Order')
plt.xlabel('List Size')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.show()


# In[ ]:


from time import time
import matplotlib.pyplot as plt

def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                swapped = True
                A[j], A[j+1] = A[j+1], A[j]
        if not swapped:
            break
            
def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A

def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
    return A

# List sizes to sort
X = [10, 50, 500, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 20000, 25000, 30000, 40000, 50000]

# Times for each sort
Y_selection = []
Y_insertion = []
Y_bubble = []

for size in X:
    list_to_sort = list(range(size))
 
    start_time = time()
    bubble_sort(list_to_sort[:])
    Y_bubble.append(time() - start_time)
    
    start_time = time()
    selection_sort(list_to_sort[:])
    Y_selection.append(time() - start_time)
    
    start_time = time()
    insertion_sort(list_to_sort[:])
    Y_insertion.append(time() - start_time)

# Plotting
plt.scatter(X, Y_selection, color='red', label='Selection Sort')
plt.scatter(X, Y_insertion, color='blue', label='Insertion Sort')
plt.scatter(X, Y_bubble, color='green', label='Bubble Sort')

plt.title('Sorting Algorithm Performance on Sorted Arrays')
plt.xlabel('List Size')
plt.ylabel('Time Taken (seconds)')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




