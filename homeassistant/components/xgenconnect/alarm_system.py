"""xGenConnect alarm system."""

from datetime import timedelta

from homeassistant.const import CONF_HOST, CONF_NAME
from homeassistant.core import HomeAssistant  # , callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
)  # , UpdateFailed

from .api.data import PartitionInfo
from .api.xGenConnectApi import XGenConnectApi
from .const import DATA_API_CLIENT, DOMAIN, LOGGER, PARTITION_STATUS_UPDATE_INTERVAL
from .types import XGenConnectConfigEntry


class XGenConnectAlarmSystem:
    """Foo."""

    hass: HomeAssistant
    config_entry: XGenConnectConfigEntry
    device_info: DeviceInfo
    coordinator: DataUpdateCoordinator[None]
    api: XGenConnectApi
    partitions: list[PartitionInfo]

    def __init__(
        self, hass: HomeAssistant, config_entry: XGenConnectConfigEntry
    ) -> None:
        """Init."""

        self.config_entry = config_entry
        self.hass = hass
        self.api = self.config_entry.runtime_data[DATA_API_CLIENT]

        self.device_info = DeviceInfo(
            identifiers={(DOMAIN, self.config_entry.data[CONF_HOST])},
            manufacturer="Interlogix",
        )

        self.coordinator = DataUpdateCoordinator(
            self.hass,
            LOGGER,
            name=str(self),
            update_method=self.async_update_data,
            update_interval=self.update_interval,
        )

    async def async_update_api_data(self):
        """Retrieve and cache data for this alarm system from the API."""
        self.partitions = await self.api.async_retrieve_partitions()

    @property
    def update_interval(self) -> timedelta:
        """Update interval."""
        return PARTITION_STATUS_UPDATE_INTERVAL

    async def async_update_data(self) -> None:
        """Update data."""
        LOGGER.debug("async_update_data")

    @property
    def name(self) -> str:
        """Get the alarm system name."""
        return self.config_entry.data[CONF_NAME]
