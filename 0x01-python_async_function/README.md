# 0x01. Python - Async

## Overview

This project is part of the ALX Software Engineering Program. It's designed to help me understand and implement asynchronous programming in Python. By the end of this project, I should be able to explain various concepts related to async programming without needing to look them up.

## Learning

By completing this project, I aim to understand:

- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

## Requirements

### General

- A `README.md` file, at the root of the folder of the project, is mandatory
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- All files must be executable
- The length of files will be tested using `wc`
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the `pycodestyle` style (version 2.5.x)
- All functions and coroutines must be type-annotated
- All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All functions should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
- Documentation should not be a simple word; it should be a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)

## Key Python Async Concepts

### `async` and `await` Syntax

The `async` and `await` keywords are used to define asynchronous functions in Python. These functions allow you to write code that can perform multiple operations concurrently.

### Executing an Async Program with `asyncio`

`asyncio` is a library to write concurrent code using the async/await syntax. It provides a framework for writing asynchronous programs in Python.

### Running Concurrent Coroutines

Coroutines are a type of function that can pause and resume execution. Using `asyncio`, you can run multiple coroutines concurrently, making your program more efficient.

### Creating `asyncio` Tasks

Tasks are used to schedule coroutines to run concurrently. `asyncio` provides mechanisms to create and manage these tasks.

### Using the `random` Module

The `random` module in Python provides functions to generate random numbers, which can be useful in asynchronous programs for simulating unpredictable events.

## Tasks

### 0. The basics of async

Write an asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it.

Use the `random` module.

Example:

```python
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```

### 1. Let's execute multiple coroutines at the same time with async

Import `wait_random` from the previous Python file and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified `max_delay`.

`wait_n` should return the list of all the delays (float values). The list of the delays should be in ascending order without using `sort()` because of concurrency.

Example:

```python
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
```

### 2. Measure the runtime

From the previous file, import `wait_n` into `2-measure_runtime.py`.

Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. Your function should return a float.

Use the `time` module to measure an approximate elapsed time.

Example:

```python
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
```

### 3. Tasks

Import `wait_random` from `0-basic_async_syntax`.

Write a function (do not create an async function, use the regular function syntax to do this) `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

Example:

```python
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```

### 4. Tasks

Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.

Example:

```python
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
```
