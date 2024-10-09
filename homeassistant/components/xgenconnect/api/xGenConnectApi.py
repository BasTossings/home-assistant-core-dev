"""xGenConnect API."""

from __future__ import annotations

import asyncio
import urllib.parse

from requests import Session

from .const import HTTP_TIMEOUT, LOGGER
from .data import PartitionInfo

SESSION_ID_PREFIX = 'function getSession(){return "'
SESSION_ID_POSTFIX = '"'
AREANAMES_PREFIX = "var areaNames = ["
AREANAMES_POSTFIX = "];"


class XGenConnectApi:
    """xGenConnect API."""

    host: str
    base_url: str
    session: Session
    session_id: str

    def __init__(self, host: str) -> None:
        """Initialize the xGenConnect API."""

        self.host = host
        self.base_url = f"http://{self.host}"
        self.session = Session()

    def _do_http_post(self, url: str, data=None):
        """Perform a HTTP POST."""

        headers = {
            "User-Agent": "Mozilla/5.0",
        }

        return self.session.post(
            f"{self.base_url}{url}",
            data=data,
            timeout=HTTP_TIMEOUT,
            headers=headers,
            allow_redirects=False,
            stream=False,
        )

    async def _async_do_http_post(self, url: str, data=None):
        return await asyncio.to_thread(self._do_http_post, url, data)

    def _parse_string(self, string: str, prefix: str, postfix: str) -> str:
        sessionid_index = string.index(prefix) + len(prefix)
        sessionid_end_index = string.index(postfix, sessionid_index)
        return string[sessionid_index:sessionid_end_index]

    async def async_authenticate(self, user: str, pin: str):
        """Authenticate the user to the xGenConnect webserver."""

        data = {"lgname": user, "lgpin": pin}

        response = await self._async_do_http_post("/login.cgi", data)

        if not response.ok or response.status_code != 200:
            LOGGER.error(
                f"Authentication to alarm system at {self.base_url} failed: {response.reason}"
            )
            return

        response_body = response.content.decode()
        self.session_id = self._parse_string(
            response_body, SESSION_ID_PREFIX, SESSION_ID_POSTFIX
        )

        LOGGER.info(
            f"Authentication to alarm system succeeded. Session ID = {self.session_id}"
        )

    async def async_retrieve_partitions(self) -> list[PartitionInfo]:
        """Retrieve a list of areas for this alarm panel."""

        data = {"sess": self.session_id}
        response = await self._async_do_http_post("/user/area.htm", data)

        response_body = response.content.decode()

        area_names = [
            urllib.parse.unquote(s.strip('"'))
            for s in self._parse_string(
                response_body, AREANAMES_PREFIX, AREANAMES_POSTFIX
            ).split(",")
        ]

        try:
            area_count = area_names.index("!")
        except ValueError:
            area_count = len(area_names)

        return [PartitionInfo(i, area_names[i]) for i in range(area_count)]
