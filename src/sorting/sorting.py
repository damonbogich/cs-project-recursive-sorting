# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    total_length = len(arrA) + len(arrB)
    merged_arr = [None] * total_length #what is this line doing?
    #are we filling merged array with None values for the length
    #of arrA and arrB combined?

    pointerA = 0
    pointerB = 0 
    # Your code here
    for index in range(0, total_length):
        #place smallest element from either a or b
        if pointerA >= len(arrA):
            merged_arr[index] = arrB[pointerB]
            pointerB += 1
        elif pointerB >= len(arrB):
            merged_arr[index] = arrA[pointerA]
            pointerA += 1
        elif arrA[pointerA] < arrB[pointerB]:
            merged_arr[index] = arrA[pointerA]
            pointerA += 1
        else:
            merged_arr[index] = arrB[pointerB]
            pointerB += 1


        



    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid] # why not include mid in the bottom half of array
                    # if we're doing floor division?
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


    # return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

