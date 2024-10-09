"""Platform for alarm control panel integration."""

from homeassistant.components.alarm_control_panel import (
    # SensorDeviceClass,
    # SensorEntity,
    # SensorStateClass,
    AlarmControlPanelEntity,
    AlarmControlPanelEntityFeature,
    # AlarmControlPanelEntityDescription,
    CodeFormat,
)
from homeassistant.const import (
    # CONF_HOST,
    STATE_ALARM_ARMED_AWAY,
    STATE_ALARM_ARMED_CUSTOM_BYPASS,
    STATE_ALARM_ARMED_HOME,
    STATE_ALARM_ARMED_NIGHT,
    STATE_ALARM_ARMED_VACATION,
    # STATE_ALARM_TRIGGERED,
    STATE_ALARM_DISARMED,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .alarm_system import XGenConnectAlarmSystem
from .const import LOGGER
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

    # pylint: disable=fixme, import-outside-toplevel
    # pylint: disable=fixme, hass-relative-import

    from homeassistant.components.xgenconnect.entity_factory import (
        XGenConnectEntityFactory,
    )

    factory = XGenConnectEntityFactory(hass, config_entry)
    async_add_entities(factory.get_alarm_panels())


# Alarm panel implementation


class xGenConnectAlarmPartition(
    CoordinatorEntity[DataUpdateCoordinator[None]],
    AlarmControlPanelEntity,
    # AlarmControlPanelEntity
):
    """Representation of a xGenConnect alarm partition."""

    system: XGenConnectAlarmSystem
    partition_index: int

    def __init__(self, system: XGenConnectAlarmSystem, partition_index: int) -> None:
        """Initialize the alarm panel."""
        self.supported_features = (
            AlarmControlPanelEntityFeature.ARM_AWAY
            | AlarmControlPanelEntityFeature.ARM_CUSTOM_BYPASS
            | AlarmControlPanelEntityFeature.ARM_HOME
            | AlarmControlPanelEntityFeature.ARM_NIGHT
            | AlarmControlPanelEntityFeature.ARM_VACATION
            | AlarmControlPanelEntityFeature.TRIGGER
        )
        super().__init__(system.coordinator)

        # self.entity_description = AlarmControlPanelEntityDescription()

        self.system = system
        self.partition_index = partition_index

        self._attr_name = self.system.get_partition_name(self.partition_index)
        self._attr_native_value = 123
        self._attr_state = STATE_ALARM_DISARMED
        self._attr_code_arm_required = True
        self._attr_code_format = CodeFormat.NUMBER
        self._attr_unique_id = system.config_entry.entry_id
        self._attr_device_info = system.device_info

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

    @property
    def unique_id(self) -> str | None:
        """Return a unique ID."""

        return f"{self.system.name}_partition_{self.partition_index}"

    def update(self) -> None:
        """Fetch new state data for the alarm panel.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._attr_native_value = 23
        self.changed_by = "Basss"
