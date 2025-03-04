import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import time
from utils import fetch_url, URLS, count_primes_in_range, split_range


# Define this at the module level, not inside another function
def download_task_mp(i, url, results):
    results[i] = fetch_url(url)

def run_io_bound_multiprocessing():
    """Run IO-bound task using multiprocessing."""
    start_time = time.time()

    with multiprocessing.Manager() as manager:
        results = manager.list([0] * len(URLS))
        processes = []

        for i, url in enumerate(URLS):
            # Use the module-level function instead
            process = multiprocessing.Process(target=download_task_mp, args=(i, url, results))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        total_size = sum(results)

    elapsed = time.time() - start_time

    print(f"Multiprocessing (IO-bound) - Total data size: {total_size}, Time: {elapsed:.2f} seconds")
    return elapsed, total_size


# Define this at the module level in multiprocess.py
def process_range(range_tuple):
    """Process a range of numbers to count primes."""
    start, end = range_tuple
    return count_primes_in_range(start, end)

def run_cpu_bound_multiprocessing():
    """Run CPU-bound task using multiprocessing."""
    start_time = time.time()

    ranges = split_range(1, 100000, multiprocessing.cpu_count())

    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        # Use the module-level function instead of lambda
        results = list(executor.map(process_range, ranges))

    elapsed = time.time() - start_time
    total_primes = sum(results)

    print(f"Multiprocessing (CPU-bound) - Total primes: {total_primes}, Time: {elapsed:.2f} seconds")
    return elapsed, total_primes