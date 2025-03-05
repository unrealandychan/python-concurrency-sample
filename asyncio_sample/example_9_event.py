import asyncio

async def wait_for_event(event):
    print("Waiting for event to be set")
    await event.wait()
    print("Event has been set")

async def setter(event):
    print("Event setter called")
    await asyncio.sleep(2)
    print("Setting the event")
    event.set()

async def main():
    event = asyncio.Event()
    task1 = asyncio.create_task(wait_for_event(event))
    task2 = asyncio.create_task(setter(event))
    await asyncio.gather(task1, task2)

asyncio.run(main())