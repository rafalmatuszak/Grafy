import random
import csv
import sys

def selection(array,k):

    #CHECKING ARRAY CORRECTNESS
    #if array is empty, return error message,
    #if array length is equal to 1, returns that element 
    #if the array contains less than 10 elements, 
    #simply sort it and select the k-th element

    if not array:
        sys.exit("Array is empty!")
    elif len(array) == 1:
        print("Array has only one element and it is equal to: ",array[0])
        sys.exit()
    elif len(array) <= 140:
        array.sort()
        return array[k]

    #PARTITIONING INTO SUBSETS
    #partition the array into subsets of maximum of 5 elements

    subset_max = 5
    subsets = []
    medians_num = len(array) // subset_max

    if(len(array) % subset_max) > 0:
        medians_num +=1
    for n in range(medians_num):
        start = n*subset_max
        stop = min(len(array),start + subset_max)
        subset = array[start:stop]
        subsets.append(subset)    

    #MEDIANS FINDING
    #finding the median for each subset
    medians = []
    for subset in subsets:
        median = selection(subset,len(subset) // 2)
        medians.append(median)

    median_of_medians = selection(medians,len(medians) // 2)
    pivot = median_of_medians

    
    #PIVOT SELECTING
    #selecting recursively with pivot
    array_lt = []
    array_gt = []
    array_eq = []
    for it in array:
        if it < pivot:
            array_lt.append(it)
        elif it > pivot:
            array_gt.append(it)
        else:
            array_eq.append(it)

    if k < len(array_lt):
        return selection(array_lt,k)
    elif k < (len(array_lt) + len(array_eq)):
        return array_eq[0]
    else:
        normalized_k = k - (len(array_lt) + len(array_eq))
        return selection(array_gt,normalized_k)
##END OF SELECTION FUNCTION

#RUNNING ALGORITHM FOR RANDOM NUMBERS
#num = 10000
#tablica = [random.randint(1,1000) for n in range(num)]
#random.shuffle(tablica)
#random.shuffle(tablica)

## k-th element and it's value
#k = 7
#kval = selection(tablica,k)
#print("SELECTION ALGORITHM:")
#print("The ",k,"-th number value is: ",kval)

##testing and comparing
#tablica_sort = sorted(tablica)
#kval2 = tablica_sort[k]
#print("SORT AND INDEX:")
#print("The ",k,"-th number value is: ",kval2)
#assert tablica_sort[k] == kval

#RUNNING ALGORITHM FOR NUMBERS FROM CSV FILE
tab = []
el = int(input("Please choose element to find:"))

with open('datasets.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        tab.append(int(row['A']))

#EVALUATION
kval_sel = selection(tab,el)
tab_sorted = sorted(tab)
kval_sort = tab_sorted[el]
print("Element no ",el," has been found with selection algorithm, value is: ",kval_sel,"\n")
print("Element no ",el," has been found by sorting and indexing, value is: ",kval_sort,"\n")

