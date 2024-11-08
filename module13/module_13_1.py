from time import sleep
import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for ball in range(1, 5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {ball}')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Марио', 2))
    task2 = asyncio.create_task(start_strongman('Герман', 3))
    task3 = asyncio.create_task(start_strongman('Миха', 0.5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())