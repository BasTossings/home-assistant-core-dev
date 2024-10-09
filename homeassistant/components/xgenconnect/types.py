"""Typing for the xGenConnect integration."""

from typing import TypedDict

from homeassistant.config_entries import ConfigEntry

from .api.xGenConnectApi import XGenConnectApi

type XGenConnectConfigEntry = ConfigEntry[XGenConnectData]  # noqa: F821


class XGenConnectData(TypedDict):
    """Data for the xGenConnect integration."""

    api_client: XGenConnectApi
