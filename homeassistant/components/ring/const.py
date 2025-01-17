"""The Ring constants."""

from __future__ import annotations

from datetime import timedelta

from homeassistant.const import Platform

ATTRIBUTION = "Data provided by Ring.com"

NOTIFICATION_ID = "ring_notification"
NOTIFICATION_TITLE = "Ring Setup"

DOMAIN = "ring"
DEFAULT_ENTITY_NAMESPACE = "ring"

PLATFORMS = [
    Platform.BINARY_SENSOR,
    Platform.CAMERA,
    Platform.LIGHT,
    Platform.SENSOR,
    Platform.SIREN,
    Platform.SWITCH,
]


SCAN_INTERVAL = timedelta(minutes=1)
NOTIFICATIONS_SCAN_INTERVAL = timedelta(seconds=5)

RING_API = "api"
RING_DEVICES = "devices"

RING_DEVICES_COORDINATOR = "device_data"
RING_NOTIFICATIONS_COORDINATOR = "dings_data"

CONF_2FA = "2fa"
