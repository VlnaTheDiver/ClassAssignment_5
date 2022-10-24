#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''
#SOLUTION FOUND VIA https://www.geeksforgeeks.org/python-program-for-quicksort/

import numbers


def partition(numbers_in_a_list,low,high):

    #CHOOSE THE RIGHTMOST ELEMENT AS PIVOT
    pivot = numbers_in_a_list[high]
    i = low -1

    for j in range(low,high):
        if numbers_in_a_list[j] <= pivot:
            i = i + 1

        #SWAPPING ELEMENT AT i WITH ELEMENT AT j
            (numbers_in_a_list[i],numbers_in_a_list[j]) = (numbers_in_a_list[j], numbers_in_a_list[i])
        
        #SWAP THE PIVOT ELEMENT WITH THE GREATER ELEMENT SPECIFIED BY i
    (numbers_in_a_list[i+1], numbers_in_a_list[high]) = (numbers_in_a_list[high], numbers_in_a_list[i + 1])
    
    #RETURN THE POSITION FROM WHERE THE PARTITION IS DONE
    return i + 1

def quicksort(numbers_in_a_list, low, high):
#WRITE YOUR CODE HERE FOR THE RECURSIVE SORTING FUNCTION
    if low < high:
        pi = partition(numbers_in_a_list,low,high)
        quicksort(numbers_in_a_list,low,pi - 1)
        quicksort(numbers_in_a_list,pi + 1, high)
    return numbers_in_a_list

def main():
# WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM, 
# AND WRITE OUT YOUR FILE
    global sorted_numbers_in_a_list
    sorted_numbers_in_a_list = list()
    unsorted_list = []

    f = open("numbers.txt","r")
    data = f.read()
    str_list = data.replace("[","").replace("]","").replace(" ","").split(",")

    for element in str_list:
            unsorted_list.append(int(element))

    print(f"This is the unsorted list:\n {unsorted_list}")
    size = len(unsorted_list)

    quicksort(unsorted_list,0,size - 1)
    print(f"\nThis is the sorted list:\n {unsorted_list}")

    #Output sorted list to .txt file
    with open(r"sorted.txt","x") as outF:
        outF.write(",".join(str(item) for item in unsorted_list))
    outF.close()
    return outF

if __name__ == "__main__":
    main()
