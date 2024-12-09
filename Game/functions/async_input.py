import asyncio
import time

user_input = None
dt = 0

async def get_input(timeout, enemy_type = None):
    try:
        global user_input
        print(f'You have {timeout} seconds to answer this question.')
        user_input = await asyncio.to_thread(input)
    except asyncio.CancelledError:
        print('You have failed to answer the question on time.')
        print('Press enter to continue...')
        raise

async def countdown(timeout):
    await asyncio.sleep(timeout)
    print('\nTime is out!')


async def main(timeout):
    in_task = asyncio.create_task(get_input(timeout))
    time_task = asyncio.create_task(countdown(timeout))

    global dt
    start_time = time.time()

    done, pending = await asyncio.wait(
        [in_task, time_task], return_when=asyncio.FIRST_COMPLETED
    )

    dt = time.time() - start_time

    for t in pending:
        t.cancel()
    
    for t in done:
        if t is in_task:
            return user_input, round(dt, 2)
        else:
            return None, round(dt, 2)