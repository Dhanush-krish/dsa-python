### Binary search

*    Eliminates half elements each time.
*    the array must sorted.
*    reduce the time complexity to O(Log n). 

```

    **why is mid calculated as mid = beg + (end-beg)/2 ?**

    Integer range is -2,147,483,648 to 2,147,483,647. If you are searching in an array of size 2,000,000,000 and the element searched for is located at index 1,999,999,999. When you search in the upper half of array, beg=1,000,000,001 and end=2,000,000,000. If mid is calculated as (low+high)/2, low+high = 3,000,000,001; which exceeds the range of int, resulting in overflow errors. But mid calculated as beg + (end-beg) = 1,000,000,001 + 999,999,999 = 2,000,000,000; which fits in the integer range.



```