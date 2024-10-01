"""Platform for alarm control panel integration."""

from homeassistant.components.alarm_control_panel import (
    AlarmControlPanelEntity,
    CodeFormat,
    # SensorDeviceClass,
    # SensorEntity,
    # SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import LOGGER


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the alarm panel platform."""
    add_entities([xGenConnectAlarmPanel()])


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the alarm panel platform."""
    async_add_entities([xGenConnectAlarmPanel()])


class xGenConnectAlarmPanel(AlarmControlPanelEntity):
    """Representation of a xGenConnect alarm panel."""

    def __init__(
        self,
    ) -> None:
        """Initialize the alarm panel."""
        self._attr_name = "My First Alarm Panel"
        self._attr_native_value = 123
        self._attr_state = "disarmed"
        self._attr_code_arm_required = True
        self._attr_code_format = CodeFormat.NUMBER

    # _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    # _attr_device_class = SensorDeviceClass.TEMPERATURE
    # _attr_state_class = SensorStateClass.MEASUREMENT

    def alarm_disarm(self, code: str | None = None) -> None:
        """Send disarm command."""
        LOGGER.info("Disarm: %s", code)

    async def async_alarm_disarm(self, code: str | None = None) -> None:
        """Send disarm command."""
        LOGGER.info("Disarm: %s", code)

    def alarm_arm_home(self, code: str | None = None) -> None:
        """Send arm home command."""
        LOGGER.info("Arm Home: %s", code)

    async def async_alarm_arm_home(self, code: str | None = None) -> None:
        """Send arm home command."""
        LOGGER.info("Arm Home: %s", code)

    def alarm_arm_away(self, code: str | None = None) -> None:
        """Send arm away command."""
        LOGGER.info("Arm Away: %s", code)

    async def async_alarm_arm_away(self, code: str | None = None) -> None:
        """Send arm away command."""
        LOGGER.info("Arm Away: %s", code)

    def alarm_arm_vacation(self, code: str | None = None) -> None:
        """Send arm vacation command."""
        LOGGER.info("Arm Vacation: %s", code)

    async def async_alarm_arm_vacation(self, code: str | None = None) -> None:
        """Send arm vacation command."""
        LOGGER.info("Arm Vacation: %s", code)

    def alarm_arm_custom_bypass(self, code: str | None = None) -> None:
        """Send arm custom bypass command."""
        LOGGER.info("Arm Custom Bypass: %s", code)

    async def async_alarm_arm_custom_bypass(self, code: str | None = None) -> None:
        """Send arm custom bypass command."""
        LOGGER.info("Arm Custom Bypass: %s", code)

    def update(self) -> None:
        """Fetch new state data for the alarm panel.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._attr_native_value = 23
        self.changed_by = "Basss"
