import asyncio

# This is a coroutine function that simulates fetching data from a URL
async def fetch_data_fake(delay):
    print(f"Fetching data from URL with a delay of {delay} seconds")
    await asyncio.sleep(delay)
    print(f"Data fetched")
    return f"Data fetched after {delay} seconds"

async def main():
    print("Starting the main coroutine")
    task = fetch_data_fake(2)
    # This will block the main coroutine until the task is completed
    result = await task
    print("Received result:", result)
    print("End of main coroutine")

asyncio.run(main())