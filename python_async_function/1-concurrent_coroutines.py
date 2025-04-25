#!/usr/bin/env python3
"""
Write an async routine called wait_n that takes
in 2 int arguments (in this order): n and max_delay.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random coroutines concurrently and collect their results
    in order of completion.
    """
    async_tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for completed in asyncio.as_completed(async_tasks):
        delay = await completed
        delays.append(delay)
    return delays