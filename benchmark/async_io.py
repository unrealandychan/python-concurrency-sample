import asyncio
import aiohttp
import time
from utils import URLS, count_primes_in_range, split_range


async def fetch_url_async(url):
    """Fetch data from a URL asynchronously."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.text()
                return len(data)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return 0


async def run_io_bound_async():
    """Run IO-bound task using asyncio."""
    start_time = time.time()

    tasks = [fetch_url_async(url) for url in URLS]
    results = await asyncio.gather(*tasks)

    elapsed = time.time() - start_time
    total_size = sum(results)

    print(f"Asyncio (IO-bound) - Total data size: {total_size}, Time: {elapsed:.2f} seconds")
    return elapsed, total_size


async def run_cpu_bound_async():
    """Run CPU-bound task using asyncio with executor."""
    start_time = time.time()

    # Split the computation range
    ranges = split_range(1, 100000, 8)
    loop = asyncio.get_event_loop()
    tasks = []

    # Run CPU-bound tasks in a ThreadPoolExecutor (default executor)
    for start, end in ranges:
        tasks.append(loop.run_in_executor(None, count_primes_in_range, start, end))

    results = await asyncio.gather(*tasks)

    elapsed = time.time() - start_time
    total_primes = sum(results)

    print(f"Asyncio with executor (CPU-bound) - Total primes: {total_primes}, Time: {elapsed:.2f} seconds")
    return elapsed, total_primes