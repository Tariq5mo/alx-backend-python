#!/usr/bin/env python3
"""Module to demonstrate async comprehensions.

This module imports the async_generator from the previous task and defines
a coroutine called async_comprehension that collects 10 random numbers
using an async comprehension over async_generator.
"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collect 10 random numbers using an async comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]
