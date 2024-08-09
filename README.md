# Quicksort Algorithm in Python
**Introduction**

Quicksort is an efficient, in-place, comparison-based sorting algorithm. It employs a divide-and-conquer approach by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted. This process results in a sorted array.

**Time Complexity**
* Best Case: O(n log n)
* Average Case: O(n log n)
* Worst Case: O(n²)
Here, n is the number of elements in the array.

**Explanation**

1) Quicksort Function:

* Parameters: arr - The array to be sorted.
* Base Case: If the array has 0 or 1 element, it is already sorted.
* Pivot Selection: The last element of the array is chosen as the pivot.
* Partitioning: The array is split into two sub-arrays:
* left: Contains all elements less than or equal to the pivot.
* right: Contains all elements greater than the pivot.
* Recursion: The function recursively applies quicksort to the left and right sub-arrays.
* Combining: The sorted left sub-array, the pivot, and the sorted right sub-array are combined to produce the final sorted array.

2) Main Execution:

* Prompts the user to enter the elements of the array.
* Applies the quicksort function to sort the array.
* Outputs the sorted array.

**Usage**
* Run the code.
* Enter the elements of the array when prompted (space-separated).
* The program will output the sorted array.
