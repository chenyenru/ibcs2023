# 3_networking/nonblocking/async_test.py

import asyncio
import time

async def message(message: str, delay: int=2):
    await asyncio.sleep(delay)
    print(message)

async def no_tasks():
    print(f"Started at {time.strftime('%X')}")

    delay = 1
    for i in range(3):
        await message(f"First loop {i}", delay)

    delay = 2
    for i in range(3):
        await message(f"First loop {i}", delay)

    print(f"Finished at {time.strftime('%X')}")

async def task_list():
    print(f"Started at {time.strftime('%X')}")

    tasks = []
    delay = 1
    for i in range(3):
        # creating co routines. NOT calling a function
        tasks.append(message(f"First loop {i}", delay))

    delay = 2
    for i in range(3):
        # creating co routines. NOT calling a function
        tasks.append(message(f"First loop {i}", delay))
    
    for task in tasks:
        # calling the co routines
        await task

    print(f"Finished at {time.strftime('%X')}")

async def tasks_gather():
    print(f"Started at {time.strftime('%X')}")

    tasks = []
    delay = 1
    for i in range(3):
        # creating co routines. NOT calling a function
        tasks.append(message(f"First loop {i}", delay))

    delay = 2
    for i in range(3):
        # creating co routines. NOT calling a function
        tasks.append(message(f"First loop {i}", delay))
    
    # calling the co routines
    await asyncio.gather(*tasks) # *task is like pointers
    

    print(f"Finished at {time.strftime('%X')}")

if __name__ == "__main__":
    # asyncio.run(no_tasks())
    # asyncio.run(tasks_list())
    asyncio.run(tasks_gather())