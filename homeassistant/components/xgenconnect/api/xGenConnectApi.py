"""Boop."""

from __future__ import annotations

import asyncio
import socket
import sys

# import httpx
from requests import Session

from .const import HTTP_TIMEOUT, LOGGER


class XGenConnectApi:
    """xGenConnect API."""

    host: str
    base_url: str
    session_id: str
    session: Session

    def __init__(self, host: str) -> None:
        """Initialize the xGenConnect API."""

        self.host = host
        self.base_url = f"http://{self.host}"
        self.session = Session()

    def _test_tcp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect((self.host, 80))
        s.connect(("192.168.1.180", 8888))

        msg = (
            "POST http://192.168.1.169/login.cgi HTTP/1.1\r\n"
            "Host: 192.168.1.169\r\n"
            "User-Agent: Mozilla/5.0 (Foo)\r\n"
            "Accept-Encoding: gzip, deflate\r\n"
            "Accept: */*\r\n"
            "Connection: keep-alive\r\n"
            "Content-Length: 27\r\n"
            "Content-Type: application/x-www-form-urlencoded\r\n"
            "\r\n"
            "lgname=installer&lgpin=9713\r\n"
        )

        s.send(msg.encode(encoding="ascii"))
        s.close()

    def do_http_post(self, url: str, data=None):
        """Perform a HTTP POST."""

        headers = {
            "User-Agent": "Mozilla/5.0 (Foo)",
            # "Transfer-Encoding": None,
            # "content-length": "27",
        }

        # proxies = {
        #     "http": "http://192.168.1.180:8888",
        #     "https": "http://192.168.1.180:8888",
        # }

        return self.session.post(
            f"{self.base_url}{url}",
            data=data,
            timeout=HTTP_TIMEOUT,
            headers=headers,
            allow_redirects=False,
            stream=False,
            # proxies=proxies,
        )

    async def _async_do_http_post(self, url: str, data=None):
        return await asyncio.to_thread(self.do_http_post, url, data)

    async def async_authenticate(self, user: str, pin: str):
        """Authenticate the user to the xGenConnect webserver."""

        # self._test_tcp()

        LOGGER.info(f"Python version: {sys.version}.")

        url = "/login.cgi"
        data = {"lgname": user, "lgpin": pin}

        response = await self._async_do_http_post(url, data)

        # data = f"lgname={user}&lgpin={pin}".encode(encoding="ascii")

        # data = f"lgname={user}&lgpin={pin}"  # {"lgname": user, "lgpin": pin}

        # request = Request(
        #     "POST", url, headers=headers, data=f"lgname={user}&lgpin={pin}"
        # )
        # preppedRequest = request.prepare()

        # # preppedRequest.body = f"lgname={user}&lgpin={pin}"

        # response = await asyncio.to_thread(
        #     self.session.send, preppedRequest, timeout=HTTP_TIMEOUT
        # )

        # response = await asyncio.to_thread(
        #     self.http.request, "POST", url, body=data, headers=headers, chunked=False
        # )

        # response = await asyncio.to_thread(
        #     self.session.post,
        #     url,
        #     data=data,
        #     timeout=HTTP_TIMEOUT,
        #     headers=headers,
        #     # proxies=proxies,
        # )

        # response = await self.session.post(url, data=data, headers=headers)
        # , proxies=

        # response = await httpx.post (url,data=data)

        # async with self.aiohttp_session.post(url="/login.cgi", data=data) as response:
        if not response.ok or response.status_code != 200:
            LOGGER.error(
                f"Authentication to alarm system at {self.base_url} failed: {response.reason}"
            )
        else:
            LOGGER.info("Authentication to alarm system succeeded")


# response = requests.post(url, data=data, timeout=HTTP_TIMEOUT)

# get the session ID

# response.text
