import asyncio
import time


# This is a coroutine function that simulates fetching data from a URL
async def fetch_data(id, sleep_time):
    print(f"Fetching data for id {id} with a delay of {sleep_time} seconds")
    await asyncio.sleep(sleep_time)
    print(f"Data fetched for {id}")
    return {id: f"Data fetched after {sleep_time} seconds"}

# Using tasks for concurrent
async def main():
    start = time.time()
    task1 = asyncio.create_task(fetch_data(1, 1))
    task2 = asyncio.create_task(fetch_data(2, 2))
    task3 = asyncio.create_task(fetch_data(3, 3))
    task4 = asyncio.create_task(fetch_data(4, 4))

    # This will block the main coroutine until the task is completed
    result1 = await task1
    result2 = await task2
    result3 = await task3
    result4 = await task4

    print("Received results:", result1, result2, result3, result4)
    print(f"Total time taken: {time.time() - start:.2f} seconds")

# It takes 4 seconds to complete all the tasks
asyncio.run(main())