# Python Lists

1. What is a list in Python?
   A list is an ordered, mutable collection that can store elements of different data types.
   Example:

   ```python
   l = [1, 2, 3]

   ```

2. What are the characteristics of a list?
   Ordered
   Mutable
   Allows duplicate values
   Dynamic size
   Supports indexing and slicing

3. Difference between list and tuple?
   | List | Tuple |
   | ----------- | ----------- |
   | Mutable | Immutable |
   | Uses [] | Uses () |
   | Slower | Faster |
   | More memory | Less memory |

4. What is indexing?
   Indexing is the process of accessing elements in a list using their position (index). Indexing starts from **0**.

   ```python
   l = [10, 20, 30]
   print(a[1])

   ```

5. What is negative indexing?
   Negative indexing allows you to access elements from the end of the list.
   - `-1` → Last element
   - `-2` → Second last element

   ```python
   l = [10, 20, 30]
   print(l[-1])

   ```

6. What is slicing?
   Slicing is used to extract a portion of a list.

   ```python
   list[start:stop:step]
   l = [1, 2, 3, 4, 5]
   print(l[1:4])

   ```

7. Difference between `append()` and `extend()`
   `append()` - Adds a single element to the end of the list.

   ```python
   l = [1, 2]
   l.append([3, 4])
   print(l)
   ```

   `extend()` - Adds each element of an iterable individually.

   ```python
   l = [1, 2]
   l.extend([3, 4])
   print(l)

   ```

8. Difference between `append()` and `insert()`
   `append()` - Adds an element at the end of the list. Takes only one argument (value)
   `insert()` - Adds an element at a specified index. Takes two arguments (index, value).

   ```python
   l = [1, 2]
   l.append(3)
   print(l)

   l.insert(1, 100)
   print(l)

   ```

9. Difference between `remove()`, `pop()`, and `del`
   `remove()` - Removes the first occurrence of a specified value.
   `pop()` - Removes an element by index and returns it.
   `del` - Deletes an element or slice using its index.

   ```python
   l = [10, 20, 30, 40]
   l.remove(20)
   print(l)
   l.pop(1)
   print(l)
   del l[0]
   print(l)

   ```

10. How do you reverse a list?
    There are multiple ways to reverse a list:
    - `reverse()`
    - Slicing (`[::-1]`)
    - `reversed()`

    ```python
    l = [1, 2, 3, 4]
    print(l[::-1])

    l.reverse()
    print(l)
    print(list(reversed(l)))

    ```

11. How do you sort a list?
    Lists can be sorted using:
    - `sort()`
    - `sorted()`

    ```python
    l = [5, 2, 4, 1]
    l.sort()
    print(l)

    l = sorted([3, 8, 1])
    print(l)

    ```

12. Difference between `sort()` and `sorted()`
    `sort()`- Modifies the original list. Works only with lists.
    `sorted()` - Returns a new sorted list. Works with any iterable.

13. What is a nested list?
    A nested list is a list that contains another list as one of its elements.

    ```python
    l = [1, [2, 3], [4, 5]]
    print(l)

    ```

14. How do you flatten a nested list?
    A nested list can be flattened using:
    - Loops
    - Recursion
    - List comprehension

15. How do you copy a list?
    Common ways to copy a list:
    - `copy()`
    - Slicing (`[:]`)
    - `list()`

    ```python
    l = [1, 2, 3]
    l1 = l.copy()
    l2 = l[:]
    l3 = list(l)

    ```

16. What is list comprehension?
    List comprehension is a concise way to create lists.

    ```python
    squares = [x * x for x in range(5)]
    print(squares)

    ```

17. Time Complexity of Common List Operations
    | Operation | Time Complexity |
    |------------|-----------------|
    | `append()` | O(1) |
    | `insert()` | O(n) |
    | `remove()` | O(n) |
    | `pop()` (last element) | O(1) |
    | Search (`in`) | O(n) |
    | `sort()` | O(n log n) |

18. Can a list contain different data types?
    Yes. Python lists can store different data types.

    ```python
    l = [1, "Python", 3.5, True]
    print(l)

    ```

19. Can a list contain another list?
    Yes. A list can contain one or more lists.
    ```python
    l = [1, [2, 3], 4]
    print(l)
    ```
