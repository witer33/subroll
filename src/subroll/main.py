from requests.adapters import HTTPAdapter
from urllib3 import poolmanager
import socket
import ipaddress
import random
import requests


IP_FREEBIND = 15


class SubRoll:
    def __init__(self, ipv6_subnet: str) -> None:
        self.ipv6_subnet = ipaddress.ip_network(ipv6_subnet)

    def get_ipv6_address(self) -> str:
        return str(
            ipaddress.IPv6Address(
                self.ipv6_subnet.network_address
                + random.getrandbits(
                    self.ipv6_subnet.max_prefixlen - self.ipv6_subnet.prefixlen
                )
            )
        )

    def get_session(self) -> requests.Session:
        session = requests.Session()
        adapter = SubrollAdapter(source_address=self.get_ipv6_address())
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session


class SubrollAdapter(HTTPAdapter):
    def __init__(self, *args, source_address: str, **kwargs):
        self.source_address = (source_address, 0)
        super(SubrollAdapter, self).__init__(*args, **kwargs)

    def init_poolmanager(self, connections, maxsize, **kwargs):
        socket_options = [(socket.SOL_IP, IP_FREEBIND, 1)]

        self.poolmanager = poolmanager.PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            source_address=self.source_address,
            socket_options=socket_options,
            **kwargs
        )

    def proxy_manager_for(self, *args, **kwargs):
        kwargs["source_address"] = self.source_address
        return super(SubrollAdapter, self).proxy_manager_for(*args, **kwargs)
