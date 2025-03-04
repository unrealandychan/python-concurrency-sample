import threading
from concurrent.futures import ThreadPoolExecutor
import time
from utils import fetch_url, URLS, count_primes_in_range, split_range


def run_io_bound_threading():
    """Run IO-bound task using threading."""
    start_time = time.time()

    threads = []
    results = [0] * len(URLS)

    def download_task(i, url):
        results[i] = fetch_url(url)

    for i, url in enumerate(URLS):
        thread = threading.Thread(target=download_task, args=(i, url))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    elapsed = time.time() - start_time
    total_size = sum(results)

    print(f"Threading (IO-bound) - Total data size: {total_size}, Time: {elapsed:.2f} seconds")
    return elapsed, total_size


def run_cpu_bound_threading():
    """Run CPU-bound task using threading."""
    start_time = time.time()
    threads = []
    results = [0] * 8  # 8 chunks

    ranges = split_range(1, 100000, 8)

    def calculation_task(i, start, end):
        results[i] = count_primes_in_range(start, end)

    for i, (start, end) in enumerate(ranges):
        thread = threading.Thread(target=calculation_task, args=(i, start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    elapsed = time.time() - start_time
    total_primes = sum(results)

    print(f"Threading (CPU-bound) - Total primes: {total_primes}, Time: {elapsed:.2f} seconds")
    return elapsed, total_primes