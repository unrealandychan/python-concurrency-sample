import asyncio
import time


# This is a coroutine function that simulates fetching data from a URL
async def fetch_data_fake(delay, task_name):
    print(f"Fetching data from for id {task_name} with a delay of {delay} seconds")
    await asyncio.sleep(delay)
    print(f"Data fetched for {task_name}")
    return {task_name: f"Data fetched after {delay} seconds"}
#
async def main():
    start = time.time()
    task1 = fetch_data_fake(2, "task1")
    task2 = fetch_data_fake(1, "task2")
    task3 = fetch_data_fake(3, "task3")
    task4 = fetch_data_fake(4, "task4")

    # This will block the main coroutine until the task is completed
    result1 = await task1
    print("Received result:", result1)
    result2 = await task2
    print("Received result:", result2)
    result3 = await task3
    print("Received result:", result3)
    result4 = await task4
    print("Received result:", result4)

    print("End of main coroutine")
    print(f"Total time taken: {time.time() - start:.2f} seconds")

# It takes 10 seconds to complete all the tasks
asyncio.run(main())