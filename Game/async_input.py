import asyncio

user_input = None

async def get_input(timeout):
    try:
        global user_input
        # user_input = await asyncio.to_thread(lambda : input(f'Enter shit within {timeout} sec: '))
        user_input = await asyncio.to_thread(input)
    except asyncio.CancelledError:
        print('Cancelled')
        raise

async def countdown(timeout):
    # print('Time remaining: ', end='\n')
    for i in range(0, timeout):
        print(f'Time remaining: {timeout - i} seconds\rEnter your shit: ', end='\r')
        await asyncio.sleep(1)
    print()

async def main(timeout):
    in_task = asyncio.create_task(get_input(timeout))
    time_task = asyncio.create_task(countdown(timeout))

    done, pending = await asyncio.wait(
        [in_task, time_task], return_when=asyncio.FIRST_COMPLETED
    )

    for t in pending:
        t.cancel()
    
    for t in done:
        if t is in_task:
            return user_input
        else:
            return None