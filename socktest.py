import aiohttp
import asyncio
from src.subroll.main import SubRoll


async def main():
    roll = SubRoll("2a06:a003:5021::/48")
    roll.wrap_socket()

    for _ in range(100):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://ipv6.wtfismyip.com/text") as response:
                print(await response.text())


asyncio.run(main())
