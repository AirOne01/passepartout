import pyudev
import psutil

def resolve_ventoy(mountpoint: str) -> bool:
  return mountpoint.endswith('/Ventoy')