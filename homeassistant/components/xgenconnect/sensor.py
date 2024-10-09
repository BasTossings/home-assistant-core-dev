"""Platform for sensor integration."""

from dataclasses import dataclass

from homeassistant.components.sensor import (
    # SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    # SensorStateClass,
)
from homeassistant.core import HomeAssistant

# from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .alarm_system import XGenConnectAlarmSystem
from .types import XGenConnectConfigEntry


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: XGenConnectConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""

    # pylint: disable=fixme, import-outside-toplevel
    # pylint: disable=fixme, hass-relative-import

    from .entity_factory import XGenConnectEntityFactory

    factory = XGenConnectEntityFactory(hass, config_entry)
    async_add_entities(factory.get_sensors())


# Sensor implementations


@dataclass(frozen=True, kw_only=True)
class XGenConnectSensorEntityDescription(SensorEntityDescription):
    """Sensor entity description."""

    # json_key: str


class XGenConnectSensorEntity(
    CoordinatorEntity[DataUpdateCoordinator[None]], SensorEntity
):
    """Base class for all xGenConnect sensors."""

    _attr_has_entity_name = True

    entity_description: XGenConnectSensorEntityDescription
    system: XGenConnectAlarmSystem

    def __init__(
        self,
        description: XGenConnectSensorEntityDescription,
        system: XGenConnectAlarmSystem,
    ) -> None:
        """Initialize the sensor."""

        super().__init__(system.coordinator)

        self.entity_description = description
        self.system = system
        self._attr_device_info = system.device_info

    @property
    def unique_id(self) -> str | None:
        """Return a unique ID."""

        return f"{self.system.name}_{self.entity_description.key}"

    @property
    def native_value(self) -> str | None:
        """Return the state of the sensor."""
        # return self.system.get_data(self.entity_description.json_key)
