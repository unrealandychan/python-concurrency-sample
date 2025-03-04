import time
import asyncio
import multiprocessing
import matplotlib.pyplot as plt
from utils import fetch_url, URLS, count_primes_in_range

from threaded import run_io_bound_threading, run_cpu_bound_threading
from multiprocess import run_io_bound_multiprocessing, run_cpu_bound_multiprocessing
from async_io import run_io_bound_async, run_cpu_bound_async

def run_sequential_io():
    """Run IO-bound tasks sequentially."""
    start_time = time.time()
    results = [fetch_url(url) for url in URLS]
    elapsed = time.time() - start_time
    total_size = sum(results)
    print(f"Sequential (IO-bound) - Total data size: {total_size}, Time: {elapsed:.2f} seconds")
    return elapsed, total_size

def run_sequential_cpu():
    """Run CPU-bound tasks sequentially."""
    start_time = time.time()
    total_primes = count_primes_in_range(1, 100000)
    elapsed = time.time() - start_time
    print(f"Sequential (CPU-bound) - Total primes: {total_primes}, Time: {elapsed:.2f} seconds")
    return elapsed, total_primes

def compare_results(io_results, cpu_results):
    """Plot comparison of results."""
    labels = list(io_results.keys())
    times = [io_results[label][0] for label in labels]

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(labels, times, color='skyblue')
    plt.title('IO-Bound Task Performance')
    plt.ylabel('Time (seconds)')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    cpu_labels = list(cpu_results.keys())
    cpu_times = [cpu_results[label][0] for label in cpu_labels]

    plt.subplot(1, 2, 2)
    plt.bar(cpu_labels, cpu_times, color='lightgreen')
    plt.title('CPU-Bound Task Performance')
    plt.ylabel('Time (seconds)')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig('concurrency_comparison.png')
    plt.show()

    print("\nSummary:")
    print("IO-Bound Task:")
    for label in labels:
        print(f"  {label}: {io_results[label][0]:.2f} seconds")

    print("\nCPU-Bound Task:")
    for label in cpu_labels:
        print(f"  {label}: {cpu_results[label][0]:.2f} seconds")

async def main():
    print("Comparing different concurrency approaches in Python\n")

    # Store results
    io_results = {}
    cpu_results = {}

    print("\n--- IO-Bound Tasks (Fetching URLs) ---")
    io_results['Sequential'] = run_sequential_io()
    io_results['Threading'] = run_io_bound_threading()
    io_results['Multiprocessing'] = run_io_bound_multiprocessing()
    io_results['Asyncio'] = await run_io_bound_async()

    print("\n--- CPU-Bound Tasks (Counting Primes) ---")
    cpu_results['Sequential'] = run_sequential_cpu()
    cpu_results['Threading'] = run_cpu_bound_threading()
    cpu_results['Multiprocessing'] = run_cpu_bound_multiprocessing()
    cpu_results['Asyncio+Executor'] = await run_cpu_bound_async()

    compare_results(io_results, cpu_results)

    print("\nKey Differences:")
    print("1. Threading:")
    print("   - Shares memory between threads but limited by Global Interpreter Lock (GIL)")
    print("   - Good for IO-bound tasks where GIL is released during IO operations")
    print("   - Poor for CPU-bound tasks due to GIL preventing true parallelism")

    print("2. Multiprocessing:")
    print("   - Uses separate processes with their own Python interpreters")
    print("   - Bypasses the GIL limitation for CPU-bound tasks")
    print("   - Has overhead from process creation and inter-process communication")

    print("3. Asyncio:")
    print("   - Single-threaded, cooperative multitasking using coroutines")
    print("   - Perfect for IO-bound tasks with many concurrent operations")
    print("   - Must use executors for CPU-bound tasks")

if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    asyncio.run(main())