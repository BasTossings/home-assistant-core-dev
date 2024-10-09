"""Entity factory."""

from collections.abc import Iterable

from homeassistant.components.sensor import (
    # SensorDeviceClass,
    # SensorEntity,
    # SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity

from .alarm_control_panel import xGenConnectAlarmPartition
from .alarm_system import XGenConnectAlarmSystem
from .api.data import PartitionInfo
from .sensor import XGenConnectSensorEntity, XGenConnectSensorEntityDescription

# from .const import DOMAIN, LOGGER
from .types import XGenConnectConfigEntry

SENSOR_DEFINITIONS = [
    XGenConnectSensorEntityDescription(
        key="lifetime_energy",
        # json_key="lifeTimeData",
        translation_key="lifetime_energy",
        state_class=SensorStateClass.MEASUREMENT,
        # native_unit_of_measurement=UnitOfEnergy.WATT_HOUR,
        # device_class=SensorDeviceClass.AQI,
    )
]


class XGenConnectEntityFactory:
    """Entity factory."""

    hass: HomeAssistant
    system: XGenConnectAlarmSystem

    def __init__(
        self, hass: HomeAssistant, config_entry: XGenConnectConfigEntry
    ) -> None:
        """Initialize the entity factory."""
        self.system = XGenConnectAlarmSystem(hass, config_entry)
        # config_entry.runtime_data.  # Cache XGenConnectAlarmSystem instance in runtime_data?
        self.hass = hass

    async def async_get_alarm_panels(self) -> Iterable[Entity]:
        """Get the alarm panel entities for this configuration entry."""

        await self.system.async_update_api_data()
        return [self.__create_partition(x) for x in self.system.partitions]

    async def async_get_sensors(self) -> Iterable[Entity]:
        """Get the sensor entities for this configuration entry."""

        await self.system.async_update_api_data()
        return [self.__create_sensor(x) for x in SENSOR_DEFINITIONS]

    def __create_sensor(
        self, description: XGenConnectSensorEntityDescription
    ) -> XGenConnectSensorEntity:
        return XGenConnectSensorEntity(description, self.system)

    def __create_partition(
        self, partition_info: PartitionInfo
    ) -> xGenConnectAlarmPartition:
        return xGenConnectAlarmPartition(self.system, partition_info)
