#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine called wait_random that waits
for a random delay between 0 and max_delay seconds and eventually returns it.

Functions:
    wait_random(max_delay: int = 10) -> float:
        Waits for a random delay between 0 and max_delay seconds and returns
        the delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and
    returns the delay.

    Args:
        max_delay (int): The maximum delay value (default is 10).

    Returns:
        float: The time that wait_random waits for.
    """
    sleep_time = random.uniform(0, max_delay)
    await asyncio.sleep(sleep_time)
    return sleep_time
