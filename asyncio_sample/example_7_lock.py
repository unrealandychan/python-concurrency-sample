import asyncio

# A shared resource
counter = 0

lock = asyncio.Lock()

async def modify_counter():
    global counter
    async with lock:
        print("Acquired lock")
        print("Resouce counter before modification:", counter)
        counter += 1
        print("Resource counter after modification:", counter)
        print("Releasing lock")

async def main():
    await asyncio.gather(*[modify_counter() for _ in range(10000)])
    
asyncio.run(main())