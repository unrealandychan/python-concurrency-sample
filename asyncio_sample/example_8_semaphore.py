import asyncio

async def access_resource(semaphore, resource):
    async with semaphore:
        print(f"Acquired semaphore for {resource}")
        await asyncio.sleep(1)
        print(f"Released semaphore for {resource}")

async def main():
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*[access_resource(semaphore, i) for i in range(5)])

asyncio.run(main())