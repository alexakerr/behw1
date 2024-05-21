'''
Task One - 

I would utilize either a dictionary or a message storage system for efficient retrieval.
By assigning timestamps as keys and messages as their corresponding values, searching for
a specific message based on its timestamp would be straightforward. Using the O(1) search
complexity would enhance the message retrieval efficiency.

Task Two - 

For real-time updates, WebSockets are the better option becayse they offer low latency by
maintaining open connections, contrasting with sporadic requests through polling or long polling.
Efficient WebSocket connection management minimizes idle connections.

Task Three-

For managing conversation lists, a hash table or dictionary appears to be the optimal choice.
The capability to search via key-value pairs simplifies locating specific threads by their 'name'. 
Filtering a dictionary offers various methods such as dictionary comprehension, the filter function,
or conditional statements and loops.
'''


def simple_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


'''
Task One -

The primary operations involve iterating through the indexes using nested for loops, which
leads to a quadratic time complexity. Sorting and swapping the indexes contribute to the overall
time complexity. 

Task Two- 

In this type of sorting, multiple checks and swaps are required to arrange the list in order.
As the size of the array gets bigger, the process becomes increasingly complex, as it involves
iterating through each value and performing comparisons and swaps.

Task Three-

Utilizing the .sort method appears to be the optimal approach for sorting an array. With this method,
sorting occurs within the existing list, eliminating the need for creating new lists.

'''