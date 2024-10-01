"""The xGenConnect integration."""

from __future__ import annotations

# import socket
from typing import TypedDict

# from aiohttp import ClientError
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

# from homeassistant.exceptions import ConfigEntryNotReady
# from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .api.xGenConnectApi import MyApi
from .const import LOGGER

PLATFORMS: list[Platform] = [Platform.ALARM_CONTROL_PANEL]

type XGenConnectConfigEntry = ConfigEntry[XGenConnectData]  # noqa: F821


class XGenConnectData(TypedDict):
    """Data for the xGenConnect integration."""

    api_client: MyApi


# async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
#     """Foo Bar."""
#     # hass.states.async_set("hello_state.world", "Paulus")

#     return True


# Update entry annotation
async def async_setup_entry(hass: HomeAssistant, entry: XGenConnectConfigEntry) -> bool:
    """Set up xGenConnect from a config entry."""

    # session = async_get_clientsession(hass)
    api = MyApi()

    LOGGER.info("Test")

    # 1. Create API instance
    # 2. Validate the API connection (and authentication)
    # 3. Store an API object for your platforms to access
    # entry.runtime_data = MyAPI(...)

    # try:
    #     response = await api.get_details(entry.data[CONF_SITE_ID])
    # except (TimeoutError, ClientError, socket.gaierror) as ex:
    #     LOGGER.error("Could not retrieve details from SolarEdge API")
    #     raise ConfigEntryNotReady from ex

    # if "details" not in response:
    #     LOGGER.error("Missing details data in SolarEdge response")
    #     raise ConfigEntryNotReady

    # if response["details"].get("status", "").lower() != "active":
    #     LOGGER.error("SolarEdge site is not active")
    #     return False

    entry.runtime_data = XGenConnectData(api_client=api)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


# Update entry annotation
async def async_unload_entry(
    hass: HomeAssistant, entry: XGenConnectConfigEntry
) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
