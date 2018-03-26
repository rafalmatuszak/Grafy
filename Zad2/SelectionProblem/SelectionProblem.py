import random
import csv
import sys

def selection(array,k):

    #CHECKING ARRAY CORRECTNESS
    #if the array contains less than 10 elements, 
    #simply sort it and select the k-th element
    #if not array:
    #    sys.exit("Input array is empty!")
    #elif len(array) == 1:
    #    return("Array has only one element and it value is: ", array[0])
    #elif len(array) <= 140:
    #    array.sort()
    #    return array[k]

    if len(array) <= 140:
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

    f = open('subsets.txt','w')
    for sub in subsets:
        f.write(str(sub))


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

##MAIN EXECUTION
el = int(input("Please choose element to find:"))

#######################################################
##RUNNING ALGORITHM FOR RANDOM NUMBERS
#######################################################
num = 12341
#for i in range(num):
#    tablica.append(i)

#tablica = [random.randint(1,1000) for n in range(num)]
tablica = random.sample(range(1,100000),15000)
random.shuffle(tablica)
random.shuffle(tablica)

## n-th element and it's value
kval = selection(tablica,el)
print("SELECTION ALGORITHM:")
print("The ",el,"-th number value is: ",kval)

#testing and comparing

tablica_sort = sorted(tablica)
kval2 = tablica_sort[el]
print("SORT AND INDEX:")
print("The ",el,"-th number value is: ",kval2)
assert tablica_sort[el] == kval

###################################################################
##RUNNING ALGORITHM FOR NUMBERS FROM CSV FILE
##Datasets can be chosen from file datasets.csv from columns A to E
###################################################################
#tab = []
#with open('datasets.csv') as f:
#    reader = csv.DictReader(f)
#    for row in reader:
#        tab.append(int(row['B']))

##EVALUATION
#kval_sel = selection(tab,el)
#tab_sorted = sorted(tab)
#kval_sort = tab_sorted[el]
#print("Element no ",el," has been found with selection algorithm, value is: ",kval_sel,"\n")
#print("Element no ",el," has been found by sorting and indexing, value is: ",kval_sort,"\n")

