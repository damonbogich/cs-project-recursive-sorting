def countdown_to_one(n):
    if n == 0:
        return
    print(n)
    countdown_to_one(n-1)

countdown_to_one(5)


def sum_list(items):
    # 1. base case
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:]) #2. recursive call
        #3. moves twoards base case


def quicksort(data):
    #check if data has 1 or 0 elements
    #base case: a side only contains a single element
    if len(data) <= 1:
        return data
    #choose a pivot
    pivot = data[0]
    #create storage for left and right side
    #partition the data

    left = []
    right = []
    #loop through each item
    for current in data[1:]:
        if current <= pivot:
            left.append(current)
        else:
            right.append(current)
    return quicksort(left) + [pivot] + quicksort(right)

        # if it's smaller or equal add to left hand side storage
        # if it's larger add to right hand side storage

    #recursive case: recursively quick sort left and right side until base case
    
