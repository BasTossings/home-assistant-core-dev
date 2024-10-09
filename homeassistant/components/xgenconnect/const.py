"""Constants for the xGenConnect integration."""

from datetime import timedelta
import logging
from typing import Final

DATA_API_CLIENT: Final = "api_client"

DOMAIN = "xgenconnect"
DEFAULT_USER_NAME = "installer"
DEFAULT_PANEL_NAME = "xGenConnect Alarm System"
LOGGER = logging.getLogger(__package__)

PARTITION_STATUS_UPDATE_INTERVAL = timedelta(seconds=5)
