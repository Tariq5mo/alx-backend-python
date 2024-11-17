#!/usr/bin/env python3
"""
This module contains a function that creates an asyncio.Task.

The function `task_wait_random` takes an integer `max_delay` and returns an asyncio.Task
that waits for a random delay between 0 and `max_delay` seconds.
"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that waits for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio.Task that waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
