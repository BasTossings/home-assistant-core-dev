"""Constants for the xGenConnect integration."""

from datetime import timedelta
import logging
from typing import Final

from homeassistant.const import Platform

DATA_API_CLIENT: Final = "api_client"

NAME = "xGenConnect Integration"
VERSION = "0.0.1"
ISSUE_URL = "https://github.com/TODO"

DOMAIN = "xgenconnect"
DEFAULT_USER_NAME = "installer"
DEFAULT_PANEL_NAME = "xGenConnect Alarm System"
LOGGER = logging.getLogger("custom_components.xgenconnect")
PLATFORMS: list[Platform] = [Platform.ALARM_CONTROL_PANEL, Platform.SENSOR]

PARTITION_STATUS_UPDATE_INTERVAL = timedelta(seconds=5)

STARTUP_MESSAGE = f"""
----------------------------------------------------------------------------
{NAME}
Version: {VERSION}
Domain: {DOMAIN}
If you have any issues with this custom component please open an issue here:
{ISSUE_URL}
----------------------------------------------------------------------------
"""
