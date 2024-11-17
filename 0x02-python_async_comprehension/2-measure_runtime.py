#!/usr/bin/env python3
"""This module implements the measure_runtime coroutine.
"""
import asyncio
import time
from tracemalloc import start
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This coroutine measures the runtime of async_comprehension called four

    Returns:
        float: The runtime of async_comprehension called four times.
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time
