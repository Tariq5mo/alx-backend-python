#!/usr/bin/env python3
"""
This module contains a coroutine called async_generator that takes
no arguments.

The coroutine will loop 10 times, each time asynchronously waiting 1 second,
then yielding a random number between 0 and 10. Use the random module.

Functions:
    async_generator() -> AsyncGenerator[float, None]:
        Loops 10 times, each time asynchronously waits 1 second,
        then yields a random number between 0 and 10.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
