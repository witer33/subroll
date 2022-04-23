# subroll
Automatically choose a random IPv6 address from your subnet.

# Example
```python3
from src.subroll import SubRoll

roll = SubRoll("0123:4567:89ab::/48")

for _ in range(100):
    session = roll.get_session()
    print(session.get("https://ipv6.wtfismyip.com/text").text)
```
