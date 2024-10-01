"""Platform for alarm control panel integration."""

from homeassistant.components.alarm_control_panel import (
    # SensorDeviceClass,
    # SensorEntity,
    # SensorStateClass,
    AlarmControlPanelEntity,
    AlarmControlPanelEntityFeature,
    CodeFormat,
)
from homeassistant.const import (
    CONF_HOST,
    CONF_NAME,
    STATE_ALARM_ARMED_AWAY,
    STATE_ALARM_ARMED_CUSTOM_BYPASS,
    STATE_ALARM_ARMED_HOME,
    STATE_ALARM_ARMED_NIGHT,
    STATE_ALARM_ARMED_VACATION,
    # STATE_ALARM_TRIGGERED,
    STATE_ALARM_DISARMED,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, LOGGER
from .types import XGenConnectConfigEntry

# def setup_platform(
#     hass: HomeAssistant,
#     config: ConfigType,
#     add_entities: AddEntitiesCallback,
#     discovery_info: DiscoveryInfoType | None = None,
# ) -> None:
#     """Set up the alarm panel platform."""
#     add_entities([xGenConnectAlarmPanel()])


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: XGenConnectConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the alarm panel platform."""
    async_add_entities([xGenConnectAlarmPanel(config_entry)])


class xGenConnectAlarmPanel(AlarmControlPanelEntity):
    """Representation of a xGenConnect alarm panel."""

    def __init__(self, config_entry: XGenConnectConfigEntry) -> None:
        """Initialize the alarm panel."""
        self.supported_features = (
            AlarmControlPanelEntityFeature.ARM_AWAY
            | AlarmControlPanelEntityFeature.ARM_CUSTOM_BYPASS
            | AlarmControlPanelEntityFeature.ARM_HOME
            | AlarmControlPanelEntityFeature.ARM_NIGHT
            | AlarmControlPanelEntityFeature.ARM_VACATION
            | AlarmControlPanelEntityFeature.TRIGGER
        )
        self._attr_name = config_entry.data[CONF_NAME]
        self._attr_native_value = 123
        self._attr_state = STATE_ALARM_DISARMED
        self._attr_code_arm_required = True
        self._attr_code_format = CodeFormat.NUMBER
        self._attr_unique_id = config_entry.entry_id
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, config_entry.data[CONF_HOST])},
            manufacturer="Interlogix",
        )

    # _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    # _attr_device_class = SensorDeviceClass.TEMPERATURE
    # _attr_state_class = SensorStateClass.MEASUREMENT

    def alarm_disarm(self, code: str | None = None) -> None:
        """Send disarm command."""
        LOGGER.info("Disarm: %s", code)
        self._attr_state = STATE_ALARM_DISARMED

    async def async_alarm_disarm(self, code: str | None = None) -> None:
        """Send disarm command."""
        LOGGER.info("Disarm: %s", code)
        self._attr_state = STATE_ALARM_DISARMED

    def alarm_arm_home(self, code: str | None = None) -> None:
        """Send arm home command."""
        LOGGER.info("Arm Home: %s", code)
        self._attr_state = STATE_ALARM_ARMED_HOME

    async def async_alarm_arm_home(self, code: str | None = None) -> None:
        """Send arm home command."""
        LOGGER.info("Arm Home: %s", code)
        self._attr_state = STATE_ALARM_ARMED_HOME

    def alarm_arm_away(self, code: str | None = None) -> None:
        """Send arm away command."""
        LOGGER.info("Arm Away: %s", code)
        self._attr_state = STATE_ALARM_ARMED_AWAY

    async def async_alarm_arm_away(self, code: str | None = None) -> None:
        """Send arm away command."""
        LOGGER.info("Arm Away: %s", code)
        self._attr_state = STATE_ALARM_ARMED_AWAY

    def alarm_arm_vacation(self, code: str | None = None) -> None:
        """Send arm vacation command."""
        LOGGER.info("Arm Vacation: %s", code)
        self._attr_state = STATE_ALARM_ARMED_VACATION

    async def async_alarm_arm_vacation(self, code: str | None = None) -> None:
        """Send arm vacation command."""
        LOGGER.info("Arm Vacation: %s", code)
        self._attr_state = STATE_ALARM_ARMED_VACATION

    def alarm_arm_night(self, code: str | None = None) -> None:
        """Send arm night command."""
        LOGGER.info("Arm Night: %s", code)
        self._attr_state = STATE_ALARM_ARMED_NIGHT

    async def async_alarm_arm_night(self, code: str | None = None) -> None:
        """Send arm night command."""
        LOGGER.info("Arm Night: %s", code)
        self._attr_state = STATE_ALARM_ARMED_NIGHT

    def alarm_arm_custom_bypass(self, code: str | None = None) -> None:
        """Send arm custom bypass command."""
        LOGGER.info("Arm Custom Bypass: %s", code)
        self._attr_state = STATE_ALARM_ARMED_CUSTOM_BYPASS

    async def async_alarm_arm_custom_bypass(self, code: str | None = None) -> None:
        """Send arm custom bypass command."""
        LOGGER.info("Arm Custom Bypass: %s", code)
        self._attr_state = STATE_ALARM_ARMED_CUSTOM_BYPASS

    def update(self) -> None:
        """Fetch new state data for the alarm panel.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._attr_native_value = 23
        self.changed_by = "Basss"
