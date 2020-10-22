import time
#random array producer
import sys 
import random
import numpy as nprand

class AlgoResult:
    def __init__(self, algoName, arraySize, arrayType, secondsInEpoch):
        self.algoName =algoName
        self.arraySize =arraySize
        self.arrayType = arrayType
        self.secondsInEpoch = secondsInEpoch

    def listResults(self):
        return [self.algoName, self.arraySize, self.arrayType, self.secondsInEpoch]

    def toString(self):
        return "AlgoName:", self.algoName,"ArraySize:", self.arraySize, "ArrayType:",self.arrayType, "SecondsInEpochs:", self.secondsInEpoch 


def getTime():
    secondsSinceEpoch = time.time()
    return secondsSinceEpoch

def printIfArrayIsInOrder(arr):
    if (not(all(arr[i] <= arr[i+1] for i in range(len(arr)-1)))): 
        print("arrat is NOT in order")


def printIfArraySizeHasChanged(origArr, arr):
    if(not (len(arr) == len(origArr))):
        print("arrays are not the same len ")
        print(arr)
        print("orig size = ", len(origArr), "afterSortSize =", len(arr))

def appendResultTolist(arrylength,typeOfArray,algoName, elapsedTime):
    listofresults.append(AlgoResult(algoName,arrylength,typeOfArray,elapsedTime))



def timeThisSortAlgo(sortingAlgorithm, array, typeOfArray, AlgoName):
    arr = array.tolist()
    t1 = getTime() 
    sortingAlgorithm(arr)
    elapsed = (getTime() - t1)
    #print("this is the original array: ")
    #printArray(array)
    #print("this is the array after sorting:")
    #printArray(arr)
    printIfArrayIsInOrder(arr)
    #printIfArraySizeHasChanged(array.tolist(), arr)
    #print("elapsed time in epochs:",  elapsed)
    appendResultTolist(len(array), typeOfArray, AlgoName, elapsed)

def timeThisSortAlgoReturnValue(sortingAlgorithm, array, typeOfArray, AlgoName):
    t1 = getTime() 
    origArray = array.tolist()
    r = sortingAlgorithm(origArray)
    elapsed = (getTime() - t1)
    #print("this is the original array: ")
    #printArray(array.tolist())
    #print("this is the array after sorting:")
    #printArray(r)
    printIfArrayIsInOrder(r)
    #printIfArraySizeHasChanged(origArray, r)
    #print("elapsed time in epochs:",  elapsed)
    appendResultTolist(len(array), typeOfArray, AlgoName, elapsed)

def printArray(arr):
    for i in range(len(arr)): 
        print ("%d" %arr[i]) 

#SOURCE 
#https://www.geeksforgeeks.org/python-program-for-bubble-sort/
# Python program for implementation of Bubble Sort 
  
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Driver code to test above 
#SOURCE :
#https://www.geeksforgeeks.org/python-program-for-insertion-sort/
# Python program for implementation of Insertion Sort 
  
# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
# Driver code to test above   
# This code is contributed by Mohit Kumra 

#SOURCE 
#https://www.geeksforgeeks.org/python-program-for-selection-sort/
# Python program for implementation of Selection 
# Sort 
  
# Traverse through all array elements 
def selection_sort(arr):
    for i in range(len(arr)): 

        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 

        # Swap the found minimum element with  
        # the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
# Driver code to test above  

#SOURCE 
#https://www.geeksforgeeks.org/python-program-for-merge-sort/
  
# Python program for implementation of MergeSort 
def specialMergeSort(arr):
    if (len(arr)<8):
        print("specialMergeSort Algorithm used insertionSort")
        insertionSort(arr)
        return None
    else:
        print("specialMergeSort Algorithm used MergeSort")
        mergeSort(arr)


def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1
  
# Driver code to test above 
# This code is contributed by Mohit Kumra 
#SOURCE 
#https://www.geeksforgeeks.org/heap-sort/
# Python program for implementation of heap Sort 
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
  
# Driver code to test above 
# This code is contributed by Mohit Kumra 


class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
# A utility function to insert a new node with the given key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
def inorder(root, res):
    # Recursive travesal 
    if root:
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)

def treesort(arr):
    # Build BST
    if len(arr) == 0:
        return arr
    root = Node(arr[0])
    for i in range(1,len(arr)):
        insert(root, Node(arr[i]))
    # Traverse BST in order. 
    res = []
    inorder(root,res)
    return res

def testAllAlgorithms(arr, ArrayType):

    print ("Sorted array is bubbleSort:") 
    timeThisSortAlgo(bubbleSort,arr, ArrayType, "bubbleSort") 

    print ("Sorted array is insertionSort:") 
    timeThisSortAlgo(insertionSort, arr, ArrayType, "insertionSort") 

    print ("Sorted array selection_sort")   
    timeThisSortAlgo(selection_sort, arr, ArrayType, "selection_sort")

    print ("Sorted array is mergeSort") 
    timeThisSortAlgo(mergeSort, arr, ArrayType, "mergeSort") 

    print ("Sorted array is heapSort") 
    timeThisSortAlgo(heapSort, arr, ArrayType, "heapSort") 
     
    if (not (ArrayType == "FULL SORT" and len(arr) > 995) ):
        print ("Sorted array is treesort") 
        timeThisSortAlgoReturnValue(treesort,arr, ArrayType, "treesort")
    else:
        appendResultTolist(len(arr),"FULL SORT", "treesort","RecursionError: maximum recursion depth exceeded")
        print("skiped the Treesort algo because RecursionError: maximum recursion depth exceeded in comparison MAX: 995")

    print ("Sorted array is specialMergeSort") 
    timeThisSortAlgo(specialMergeSort, arr, ArrayType, "specialMergeSort") 


def createHalfSortedArr(arr):
    #TODO half sort the arr
    return arr    

listofresults =[]

numbersToPickfrom =1000
sizeOfArray  = 1000 #random.randint(0,1000)
if(numbersToPickfrom < sizeOfArray):
    print("you cant do that ")
    arr = nprand.random.choice(sizeOfArray,sizeOfArray,replace=False)
else:
    arr = nprand.random.choice(numbersToPickfrom,sizeOfArray,replace=False)

testAllAlgorithms(arr, "RANDOM")

#halfSortedArray = createHalfSortedArr(arr)

#testAllAlgorithms(halfSortedArray, "HALF SORT")

sortedArr = nprand.sort(arr)
testAllAlgorithms(sortedArr, "FULL SORT")

for result in listofresults:
    ## TODO append to excel sheet 
    print(result.toString())
