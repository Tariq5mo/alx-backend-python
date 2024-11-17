# 0x02. Python - Async Comprehension

## Overview

This project is part of the ALX Software Engineering Program. It's designed to help me understand and implement asynchronous comprehensions in Python. By the end of this project, I should be able to explain various concepts related to async comprehensions without needing to look them up.

## Learning Objectives

By completing this project, I aim to understand:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file is mandatory
- Code should use the `pycodestyle` style (version 2.5.x)
- The length of files will be tested using `wc`
- All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All functions should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
- Documentation should not be a simple word; it should be a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)
- All functions and coroutines must be type-annotated

## Key Python Async Comprehension Concepts

### Writing an Asynchronous Generator

Asynchronous generators are defined using the `async def` syntax and yield values using the `yield` keyword. These generators can be paused and resumed, making them useful for streaming data asynchronously.

### Using Async Comprehensions

Async comprehensions are similar to list comprehensions but allow you to iterate over asynchronous iterables. They provide a concise way to create lists, sets, and dictionaries from asynchronous iterables.

### Type-Annotating Generators

Type annotations for generators indicate the types of values that the generator yields. This helps with static type checking and improves code readability.

## Tasks

### 0. Async Generator

Write a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously waiting 1 second, then yielding a random number between 0 and 10. Use the `random` module.

Example:

```python
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
```

### 1. Async Comprehensions

Import `async_generator` from the previous task and write a coroutine called `async_comprehension` that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehension over `async_generator`, then return the 10 random numbers.

Example:

```python
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())
```

### 2. Run time for four parallel comprehensions

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.

`measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

Example:

```python
#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await measure_runtime()

print(asyncio.run(main()))
```
