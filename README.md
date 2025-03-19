## Searching Algorithms
### Introduction
Searching algorithms are fundamental in computer science, enabling quick data retrieval and analysis. Choosing the appropriate searching technique can optimize performance and resource usage. This document explores three widely used searching methods: Linear Search, Binary Search, and Ternary Search. We will discuss their mechanisms, efficiency, and ideal use cases.

### 1. Linear Search
#### Description
Linear Search is a straightforward method of searching where each element in the list is checked one by one until the target element is found or the list ends.

#### Algorithm Steps
1. Start from the beginning of the list.
2. Compare the target element with the current element.
3. If they match, return the position.
4. If not, move to the next element.
5. Repeat until the end of the list.
6. If the target is not found, return an indication of failure.

### 2. Binary Search
#### Description
Binary Search is an efficient searching algorithm applied to sorted arrays. It works by repeatedly dividing the search interval in half.

#### Algorithm Steps
1. Determine the middle element of the list.
2. If it matches the target, return its position.
3. If the target is smaller, focus on the left subarray.
4. If the target is larger, focus on the right subarray.
5. Repeat steps 1-4 until the target is found or the interval is empty.

### 3. Ternary Search
#### Description
Ternary Search is a divide-and-conquer algorithm similar to Binary Search, but it divides the list into three parts instead of two.

#### Algorithm Steps
1. Find two midpoints dividing the list into three segments.
2. If either midpoint matches the target, return its position.
3. If the target is smaller, search the left segment.
4. If the target is between the midpoints, search the middle segment.
5. If the target is larger, search the right segment.
6. Repeat until the target is found or the segment is empty.

### Complexities
| Algorithm       | Best Case | Worst Case | Average Case |
|-----------------|-----------|------------|--------------|
| Linear Search   | O(1)      | O(n)       | O(n)         |
| Binary Search   | O(1)      | O(log₂ n)  | O(log₂ n)    |
| Ternary Search  | O(1)      | O(log₃ n)  | O(log₃ n)    |


## Coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. Then run `python -m coverage run -m unittest discover` and after that run `python -m coverage report` to get the following table:
```
Name                          Stmts   Miss  Cover
-------------------------------------------------
array_search\algorithms.py       36      2    94%
data\constants.py                 2      0   100%
data\data_generator.py            6      1    83%
test\test_algorithms.py          20      1    95%
test\test_data_generator.py      29      1    97%
-------------------------------------------------
TOTAL                            93      5    95%
```
---
If you want to see the lines that are not being used you can run 'python -m cover html' and then 'start htmlcov\index.html'