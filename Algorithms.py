import time
import sys 
import random
import numpy as nprand
import csv
import multiprocessing
#############################################################################
#   SOURCES :                                                               #
#   https://www.geeksforgeeks.org/left-leaning-red-black-tree-insertion/    # 
#   https://www.geeksforgeeks.org/heap-sort/                                #
#   https://www.geeksforgeeks.org/python-program-for-bubble-sort/           #
#   https://www.geeksforgeeks.org/python-program-for-insertion-sort/        #
#   https://www.geeksforgeeks.org/python-program-for-selection-sort/        #
#   https://www.geeksforgeeks.org/python-program-for-merge-sort/            #
#   https://www.geeksforgeeks.org/heap-sort/                                #
#############################################################################

class AlgoResult:
    def __init__(self, algoName, arraySize, arrayType, secondsInEpoch):
        self.algoName =algoName
        self.arraySize =arraySize
        self.arrayType = arrayType
        self.secondsInEpoch = secondsInEpoch

    def toArray(self):
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
        print("orig size = ", len(origArr), "afterSortSize =", len(arr))

def appendResultTolist(arrylength,typeOfArray,algoName, elapsedTime):
    writeResultToCSVFile(AlgoResult(algoName,arrylength,typeOfArray,elapsedTime))

def timeThisSortAlgoArray(sortingAlgorithm, array, typeOfArray, AlgoName):
    arr = array.tolist()
    t1 = getTime() 
    error = False
    try:
        sortingAlgorithm(arr)
    except Exception as e:
        error = True
        trace = e
    if error:
        elapsed = trace
    else:
        elapsed = (getTime() - t1)
        printIfArrayIsInOrder(arr)
        printIfArraySizeHasChanged(array.tolist(), arr)
    appendResultTolist(len(arr), typeOfArray, AlgoName, elapsed)

def timeThisSortAlgoRoot(sortingAlgorithm, root, typeOfArray, AlgoName):
    t1 = getTime() 
    error = False
    if root == None :
        return None
    r = []
    try:
        r = sortingAlgorithm(root)
    except Exception as e:
        error = True
        trace = e
    if error:
        elapsed = trace
        print(trace)
    else:
        elapsed = (getTime() - t1)
        printIfArrayIsInOrder(r)
    appendResultTolist(len(r), typeOfArray, AlgoName, elapsed)

def printArray(arr):
    for i in range(len(arr)): 
        print ("%d" %arr[i]) 

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1):  
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

def selection_sort(arr):
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j   
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 

def specialMergeSort(arr):
    if (len(arr)<8):
        insertionSort(arr)
        return None
    else:
        mergeSort(arr)

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L) 
        mergeSort(R)  
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1  
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

def heapify(arr, n, i): 
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest) 
  
def heapSort(arr): 
    n = len(arr) 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
   
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
    if root:
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)

def buildBST(arr, ArrayType):
    newArr = arr.tolist()
    if len(newArr) == 0:
        return newArr
    try:
        root = Node(newArr[0])
        for i in range(1,len(newArr)):
            insert(root, Node(newArr[i]))
    except Exception as e:
        appendResultTolist(len(arr), ArrayType, "treesort", "buildBST : " + e.__str__())
        return None
    return root

def treesort(root):
    res = []
    inorder(root,res)
    return res

def buildLLRB(arr, ArrayType):
    node = LLRBTREE()  
    newArr = arr.tolist()
    try:
        for val in newArr :
            node.root = node.insert(node.root, val)   
            node.root.color = False 
    except Exception as e:
        appendResultTolist(len(arr), ArrayType, "llrbSort", "buildLLRB" + e.__str__())
        return None
    return node 

def llrbSort(node):
    arr = []
    node.inorder(node.root, arr)
    return arr

def testAllAlgorithms(arr, ArrayType):
    arraySortingAlgorithms = [bubbleSort ,insertionSort, selection_sort,mergeSort, heapSort, specialMergeSort]
    for arraySortingAlgorithm in arraySortingAlgorithms:
        timeThisSortAlgoArray(arraySortingAlgorithm,arr, ArrayType, arraySortingAlgorithm.__qualname__) 
    timeThisSortAlgoRoot(treesort, buildBST(arr,ArrayType), ArrayType, treesort.__qualname__)
    timeThisSortAlgoRoot(llrbSort, buildLLRB(arr,ArrayType), ArrayType, llrbSort.__qualname__)

def createHalfSortedArr(arr):
    return  nprand.partition(arr,(int) (len(arr)/2))

def writeResultToCSVFile(result):
    with open("testfile.csv", "a") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(result.toArray())
        print(result.toString())

def createRandomArray(sizeOfArray, numbersToPickfrom=None):
    if numbersToPickfrom == None:
        numbersToPickfrom =sizeOfArray
    else:
        numbersToPickfrom =numbersToPickfrom
    sizeOfArray  = sizeOfArray #random.randint(0,1000)
    if(numbersToPickfrom < sizeOfArray):
        return nprand.random.choice(sizeOfArray,sizeOfArray,replace=False)
    else:
        return nprand.random.choice(numbersToPickfrom,sizeOfArray,replace=False)

def testAllAlgorithmsArrayTypes(randomArr):
    testAllAlgorithms(randomArr, "RANDOM")
    testAllAlgorithms(createHalfSortedArr(randomArr), "HALF SORT")
    testAllAlgorithms(nprand.sort(randomArr), "FULL SORT")

class node(object):  
    def __init__( self ,data):
        self.data = data  
        self.left = None  
        self.right = None  
        self.color = True  
  
class LLRBTREE(object):
    
    def __init__(self):
        self.root = None  

    def rotateLeft(self,myNode): 
        child = myNode.right 
        childLeft = child.left  
        child.left = myNode 
        myNode.right = childLeft  
        return child
    
    def rotateRight(self,myNode):
        child = myNode.left 
        childRight = child.right  
        child.right = myNode  
        myNode.left = childRight 
        return child
      
    def isRed(self,myNode):
        if myNode == None:  
            return False  
        return myNode.color == True
    
    def swapColors(self, node1,  node2): 
        temp = node1.color  
        node1.color = node2.color  
        node2.color = temp

    def insert(self, myNode,  data):
        if myNode == None:  
            return node(data)  
        if data < myNode.data:  
            myNode.left = self.insert(myNode.left, data) 
        elif data > myNode.data:  
            myNode.right = self.insert(myNode.right, data)  
        else:
            return myNode 
        if self.isRed(myNode.right) and  not self.isRed(myNode.left): 
            myNode = self.rotateLeft(myNode)
            self.swapColors(myNode, myNode.left) 
        if self.isRed(myNode.left) and self.isRed(myNode.left.left):  
            myNode = self.rotateRight(myNode)
            self.swapColors(myNode, myNode.right)  
        if self.isRed(myNode.left) and self.isRed(myNode.right):  
            myNode.color = not myNode.color
            myNode.left.color = False  
            myNode.right.color = False  
        return myNode   
    
    def inorder(self,node,arr): 
        if not (node == None):   
            self.inorder(node.left,arr)
            arr.append(node.data) 
            self.inorder(node.right,arr)  
import concurrent.futures 

if __name__ == '__main__': 
    x = [10, 1000, 10000]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(testAllAlgorithmsArrayTypes, createRandomArray(number)) for number in x]
    
