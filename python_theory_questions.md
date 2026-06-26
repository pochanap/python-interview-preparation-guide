````python

1. What is Python? Or Why Python?

   Python is a high-level, interpreted, object-oriented, dynamically typed programming language known for its simplicity and readability.

   Features:
   - Easy to learn
   - Platform independent
   - Large standard library
   - Supports OOP and Functional Programming
   - Automatic memory management
   - Extensive third-party packages

2. Is Python compiled or interpreted?

   Python is both. Python is interpreted, but internally it first compiles code into bytecode (.pyc) and then executes it using the Python Virtual Machine (PVM).

3. What are the key features of Python?

   - Easy syntax
   - Dynamically typed
   - Interpreted
   - Huge standard library
   - Object-oriented support
   - Cross-platform

4. What is PEP 8?

   PEP 8 is the Python style guide that defines how to write clean and readable Python code.

5. What is dynamic typing?

   In Python, you don’t need to declare variable types explicitly. Type is decided at runtime.
   x = 10
   x = "hello"

6. What are Python data types?

   int
   float
   str
   list
   tuple
   set
   dict

7. Difference between list and tuple?

| List | Tuple |
|------|-------|
| List is mutable (elements can be added, removed, or modified). | Tuple is immutable (cannot be changed after creation). |
| Represented using square brackets `[]`. | Represented using parentheses `()`. |
| Supports many built-in methods like `append()`, `extend()`, `insert()`, `remove()`, `pop()`, and `sort()`. | Supports only two built-in methods: `count()` and `index()`. |
| Slightly slower because it is mutable. | Slightly faster because it is immutable. |
| Uses more memory. | Uses less memory. |
| Cannot be used as a dictionary key because it is mutable. | Can be used as a dictionary key if all its elements are hashable. |
| Best for data that changes frequently. | Best for fixed or constant data. |

### Similarities
- Both are ordered collections.
- Both allow duplicate elements.
- Both can store heterogeneous (different) data types.
- Both support indexing and slicing.
- Both can be nested.

### Example
```python
# List
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits[0] = "grapes"
print(fruits)

# Tuple
numbers = (1, 2, 3)
print(numbers)

# numbers[0] = 10      # TypeError
# numbers.append(4)    # AttributeError
````

8. Why use tuple?

   Faster
   Safer
   Hashable
   Can be used as dictionary key

9. What is a namespace?

   A namespace is a system that ensures names are unique and avoid conflicts.

10. What are Python functions?

    Functions are reusable blocks of code defined using def.

11. What is `*args` and `**kwargs`?

- `*args` collects variable positional arguments into a tuple.
- `**kwargs` collects variable keyword arguments into a dictionary.

def fun(\*args, \*\*kwargs):
print(args)
print(kwargs)

12. What is a lambda function?

    A small anonymous function.
    square = lambda x: x \* x

13. What is a module?

    A module is a .py file containing Python code (functions, variables, classes).

14. What is a package?

    A package is a collection of modules grouped in directories.

15. What is OOP?

    Object-Oriented Programming is a paradigm based on:
    - Class
    - Object
    - Inheritance
    - Polymorphism
    - Encapsulation

16. What is inheritance?

    Inheritance allows a class to reuse properties and methods of another class.
    - Single inheritance
    - Multiple inheritances
    - Multilevel inheritance
    - Hierarchical Inheritance

17. What is polymorphism?

    Same function name behaves differently based on object type.

18. What is encapsulation?

    Encapsulation means restricting access to data using private/protected members.

19. What is the difference between deep copy and shallow copy?

    Shallow copy → copies reference
    Deep copy → copies actual object

20. What are Python decorators?

    Decorators are functions that modify or extend the behavior of another function without changing its original code. They are commonly used for logging, authentication, caching, and measuring execution time.
    Example:
    def decorator(func):
    def wrapper():
    print("Before")
    func()
    print("After")
    return wrapper

    @decorator
    def greet():
    print("Hello")

21. What is memory management in Python?

    Python uses:
    - Private heap space
    - Garbage collection
    - Reference counting

```

```
