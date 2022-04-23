# subroll
Automatically choose a random IPv6 address from your subnet.  
Currently it only supports Linux and requests.

# AnyIP

**AnyIP** is a new feature of the Linux kernel, you need to **enable AnyIP** in order to use this library.

```
sudo ip -6 route add local 0123:4567:89ab::/48 dev lo
```

This will enable AnyIP, replace `0123:4567:89ab::/48` with your subnet and run this command on a shell.
___(this will not persist after reboot)___

# Example with requests
```python3
from subroll import SubRoll

roll = SubRoll("0123:4567:89ab::/48")

for _ in range(100):
    session = roll.get_session()
    print(session.get("https://ipv6.wtfismyip.com/text").text)
```

# Example with any library
```python3
import aiohttp
import asyncio
from subroll import SubRoll


async def main():
    roll = SubRoll("0123:4567:89ab::/48")
    roll.wrap_socket()

    for _ in range(100):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://ipv6.wtfismyip.com/text") as response:
                print(await response.text())


asyncio.run(main())
```
