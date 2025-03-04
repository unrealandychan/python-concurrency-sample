# Python Concurrency Programming
This repository contains examples of Python concurrency programming using threading, multiprocessing, and asyncio and when to use each method based on the type of task.

## TL;DR
- **Threading**: Best for IO-bound tasks with moderate concurrency needs. Limited by GIL for CPU-bound tasks.
- **Multiprocessing**: Best for CPU-bound tasks requiring true parallelism. Higher overhead for IO-bound tasks.
- **Asyncio**: Best for high-concurrency IO-bound tasks. Requires executors for CPU-bound tasks, which can add complexity.
- Each method has its strengths and weaknesses, and the choice depends on the specific requirements of the task at hand.8

## Threading
IO-bound tasks: Threading performs well because the Global Interpreter Lock (GIL) is released during IO operations, allowing other threads to run.
CPU-bound tasks: Threading performs poorly due to the GIL, which prevents true parallel execution of threads. Only one thread can execute Python bytecode at a time.
## Multiprocessing
IO-bound tasks: Multiprocessing can handle IO-bound tasks, but it has more overhead compared to threading due to process creation and inter-process communication.
CPU-bound tasks: Multiprocessing excels in CPU-bound tasks as it bypasses the GIL by using separate processes, allowing true parallel execution on multiple CPU cores.
## Asyncio
IO-bound tasks: Asyncio is highly efficient for IO-bound tasks, especially when dealing with many concurrent operations. It uses a single-threaded, cooperative multitasking approach with coroutines.
CPU-bound tasks: Asyncio is not suitable for CPU-bound tasks unless combined with executors (e.g., ThreadPoolExecutor or ProcessPoolExecutor), which introduces additional complexity and overhead.
## Summary
Threading: Best for IO-bound tasks with moderate concurrency needs. Limited by GIL for CPU-bound tasks.
Multiprocessing: Best for CPU-bound tasks requiring true parallelism. Higher overhead for IO-bound tasks.
Asyncio: Best for high-concurrency IO-bound tasks. Requires executors for CPU-bound tasks, which can add complexity.
Each method has its strengths and weaknesses, and the choice depends on the specific requirements of the task at hand.

## References
- [Python Threading](https://docs.python.org/3/library/threading.html)
- [Python Multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
- [Python Asyncio](https://docs.python.org/3/library/asyncio.html)
- [Real Python - Python Concurrency](https://realpython.com/python-concurrency/)
- [Real Python - Async IO in Python](https://realpython.com/async-io-python/)
- [Multithreading VS Multiprocessing VS Asyncio (With Code examples)](https://www.linkedin.com/pulse/multithreading-vs-multiprocessing-asyncio-code-examples-kaushik-yxgjc/)