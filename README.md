# SortingAlgorithms

 This is the README file for the Sorting Algorithms Homework assignment by Dylan Shapiro and Alyssa Kutney. Here you will find the python file(s) that are being used:

 Algorithms.py
    This file contains a class that contains parameters such as the the algorithm name, size, type(sorted, half sorted, random), and time in seconds in epoch. Withthis class you can list the results and there is a toString function that returns the listResults as a string.

     We run some checks on the arrays we are using. These checks are  printIfArrayIsInOrder(), printIfArraySizeHasChanged(), appendResultTolist(), timeThisSortAlgo(), and  timeThisSortAlgoReturnValue(). 

     Next, we have our sorting algorithms. These sorting algorithms include the following:
     -bubbleSort()
     -insertionSort()
     -selection_sort()
     -mergeSort()
     -specialMergeSort() with use of insertion sort
     -heapSort()
     -binarySearchTreeSort()
     -LLRB()

     To test our algorithms we create a function, where we pass an array that we generate and the type of the array(sorted, half sorted, random). This is where we use our timeThisSortAlgo() function.
