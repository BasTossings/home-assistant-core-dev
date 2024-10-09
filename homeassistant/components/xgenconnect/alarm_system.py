"""xGenConnect alarm system."""

from datetime import timedelta

from homeassistant.const import CONF_HOST, CONF_NAME
from homeassistant.core import HomeAssistant  # , callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
)  # , UpdateFailed

from .const import DOMAIN, LOGGER, PARTITION_STATUS_UPDATE_INTERVAL
from .types import XGenConnectConfigEntry


class XGenConnectAlarmSystem:
    """Foo."""

    hass: HomeAssistant
    config_entry: XGenConnectConfigEntry
    device_info: DeviceInfo
    coordinator: DataUpdateCoordinator[None]

    def __init__(
        self, hass: HomeAssistant, config_entry: XGenConnectConfigEntry
    ) -> None:
        """Init."""

        self.config_entry = config_entry
        self.hass = hass

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

    def get_partition_name(self, partition_index: int) -> str:
        """Get the name for the specified partition."""
        return f"Partition {partition_index}"

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
