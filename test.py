from src.subroll import SubRoll
import requests

roll = SubRoll("2a06:a003:5021::/48")

for _ in range(100):
    session = roll.get_session()
    response = session.get("https://ipv6.wtfismyip.com/text")
    print(response.text)