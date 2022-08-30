import psutil
import pyudev

from src.resolver import resolve_ventoy
from src.config import ConfigLoader

def check_devices() -> bool:
  context = pyudev.Context()
  connected = False
  removable = [device for device in context.list_devices(subsystem='block', DEVTYPE='disk') if device.attributes.asstring('removable') == "1"]
  for device in removable:
    partitions = [device.device_node for device in context.list_devices(subsystem='block', DEVTYPE='partition', parent=device)]
    for p in psutil.disk_partitions():
      if p.device in partitions:
        connected = resolve_ventoy(p.mountpoint) or connected
  return connected

ConfigLoader()