def finder(str_for_find):
    while True:
        s = (yield)
        if str_for_find in s:
            print('Found : "{}" in "{}"'.format(str_for_find, s))


f = finder('coroutine')
next(f)

f.send('PlanB')
f.send('This is coroutine')

########## Async / Await

import asyncio
import datetime
import random


# Async / Generator
@asyncio.coroutine
def display_date1(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(random.randint(0, 5))


loop1 = asyncio.get_event_loop()

asyncio.ensure_future(display_date1(1, loop1))
asyncio.ensure_future(display_date1(2, loop1))

loop1.run_forever()


# Async / Await
async def display_date2(num, loop, ):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(random.randint(0, 5))


loop2 = asyncio.get_event_loop()

asyncio.ensure_future(display_date2(1, loop2))
asyncio.ensure_future(display_date2(2, loop2))

loop2.run_forever()

# from https://hamait.tistory.com/830