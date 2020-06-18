# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    #if test doesn't pass, it's possible you don't need to set
    #start and end variables
    # start = 0
    # end = len(arr) - 1

    middle = (start + end) // 2
    # 3 rules:
        #1. must have base case:
            # array is narrowed down to one item
            # indexes value either = target or not
    if len(arr) < 1:
        return -1
    if len(arr) == 1 and arr[middle] == target:
        return middle
    if len(arr) <= 1 and arr[middle] != target:
        return -1
    #set up for list that still needs to split
    #if guess to the middle of list is correct return middle
    if len(arr) > 1 and arr[middle] == target:
        return middle
    #if length of array is greater than one and middle > target
    if len(arr) > 1 and arr[middle] > target:
        #now we need to split the array so it only contains the indices
        #middle + 1 through end
        # arr = arr[start:middle]
        return binary_search(arr, target, start, middle)
    if len(arr) > 1 and arr[middle] < target:
        #get rid of middle and everything below it
        # arr = arr[middle+1:end+1]
        return binary_search(arr, target, middle, end)




arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
binary_search(arr1, -8, 0, len(arr1)-1 )


    #if length of array is greater than one and middle < target


    
        

        #2. must move twoards base case
        #3. must call itself.
    









# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
