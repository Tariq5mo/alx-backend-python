#!/usr/bin/env python3
"""
This module contains an asynchronous routine called task_wait_n that spawns
task_wait_random n times with the specified max_delay.

Functions:
    task_wait_n(n: int, max_delay: int) -> List[float]:
        Spawns task_wait_random n times with the specified max_delay and
        returns
        the list of all the delays (float values) in ascending order without
        using sort() because of concurrency.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
    n (int): The number of times to spawn task_wait_random.
    max_delay (int): The maximum delay value for task_wait_random.

    Returns:
    List[float]: A list of all the delays (float values)
    in ascending order.
    """
    list_tasks = [task_wait_random(max_delay) for i in range(n)]
    list_delays = []

    for task in asyncio.as_completed(list_tasks):
        delay = await task
    list_delays.append(delay)

    return list_delays
