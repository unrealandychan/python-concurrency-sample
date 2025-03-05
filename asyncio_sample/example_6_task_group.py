import asyncio
import time


async def fetch_data(id, sleep_time):
    print(f"Fetching data for id {id} with a delay of {sleep_time} seconds")
    await asyncio.sleep(sleep_time)
    print(f"Data fetched for {id}")
    return {id: f"Data fetched after {sleep_time} seconds"}

# There is no need to use asyncio.create_task() as TaskGroup will take care of it
# TaskGroup is a high-level interface for managing multiple tasks
# It is a context manager that creates a group of tasks and manages them
async def main():
    tasks = []
    start = time.time()
    # Create a TaskGroup context manager
    async with asyncio.TaskGroup() as tg:
        for i , sleeptime in enumerate([2, 1, 2, 3],start=1):
            task = tg.create_task(fetch_data(i, sleeptime))
            tasks.append(task)

    # This will block the main coroutine until all the tasks are completed
    result = [task.result() for task in tasks]

    for result in result:
        print("Received result:", result)
    print("End of main coroutine")
    print(f"Total time taken: {time.time() - start:.2f} seconds")

asyncio.run(main())