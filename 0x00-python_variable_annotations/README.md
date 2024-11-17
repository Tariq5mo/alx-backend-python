# 0x00. Python - Variable Annotations

## Overview

This project is part of the ALX Software Engineering Program. It's designed to help me understand and implement variable annotations in Python. By the end of this project, I should be able to explain various concepts related to variable annotations without needing to look them up.

## Learning Objectives

By completing this project, I aim to understand:

- Type annotations in Python 3
- How to use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file is mandatory
- Code should use the `pycodestyle` style (version 2.5.)
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- Documentation should not be a simple word; it should be a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)

## Key Python Variable Annotations Concepts

### Type Annotations in Python 3

Type annotations provide a way to specify the expected data types of variables and function return values, helping to make the code more understandable and maintainable.

### Specifying Function Signatures and Variable Types

Type annotations can be used to explicitly declare the types of function parameters and return values. This helps with static type checking and improves code readability.

### Duck Typing

Duck typing is a concept in Python where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit inheritance from a specific class.

### Validating Code with mypy

`mypy` is a static type checker for Python that checks the type annotations and ensures that the code follows the specified types, catching potential type errors before runtime.

## Tasks

### 0. Basic annotations - add

Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

Example:

```python
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
```

### 1. Basic annotations - concat

Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string.

Example:

```python
#!/usr/bin/env python3
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
```

### 2. Basic annotations - floor

Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.

Example:

```python
#!/usr/bin/env python3

import math

floor = __import__('2-floor').floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
```

### 3. Basic annotations - to string

Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.

Example:

```python
#!/usr/bin/env python3
to_str = __import__('3-to_str').to_str

pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
```

### 4. Define variables

Define and annotate the following variables with the specified values:

- `a`, an integer with a value of 1
- `pi`, a float with a value of 3.14
- `i_understand_annotations`, a boolean with a value of True
- `school`, a string with a value of “Holberton”

Example:

```python
#!/usr/bin/env python3

a = __import__('4-define_variables').a
pi = __import__('4-define_variables').pi
i_understand_annotations = __import__('4-define_variables').i_understand_annotations
school = __import__('4-define_variables').school

print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))
```

### 5. Complex types - list of floats

Write a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float.

Example:

```python
#!/usr/bin/env python3

sum_list = __import__('5-sum_list').sum_list

floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum == sum(floats))
print(sum_list.__annotations__)
print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))
```

### 6. Complex types - mixed list

Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

Example:

```python
#!/usr/bin/env python3

sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
```

### 7. Complex types - string and int/float to tuple

Write a type-annotated function `to_kv` that takes a string `k` and an int OR float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`. The second element is the square of the int/float `v` and should be annotated as a float.

Example:

```python
#!/usr/bin/env python3

to_kv = __import__('7-to_kv').to_kv

print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))
```

### 8. Complex types - functions

Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.

Example:

```python
#!/usr/bin/env python3

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
```

### 9. Let's duck type an iterable object

Annotate the below function’s parameters and return values with the appropriate types:

```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
```

Example:

```python
#!/usr/bin/env python3

element_length = __import__('9-element_length').element_length

print(element_length.__annotations__)
```
