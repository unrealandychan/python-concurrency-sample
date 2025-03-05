# This tutorial is based on https://youtu.be/Qb9s3UiMSTA?si=8O60MPSLbZb8yVmR

import asyncio

async def main():
    print("Hello") # This will be printed first
    await asyncio.sleep(1) # This is a non-blocking call
    print("World") # This will be printed after 1 second

asyncio.run(main())