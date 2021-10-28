import asyncio

async def say(what, when):  # <1>
    await asyncio.sleep(when)  # <2>
    print(what)  # <3>

loop = asyncio.get_event_loop()  # <4>
loop.run_until_complete(say('hello, async world', 1))  # <5>
loop.close()  # <6>
