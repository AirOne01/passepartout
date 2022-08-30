from configparser import SafeConfigParser
from pathlib import Path

from src import version, default_path

list = default_path.split('/')
if list.__len__() != 1:
  list.pop(-1)
  default_directory_path = '/'.join(list)
del list

class ConfigLoader:
  """ Class for fetching the config """

  config: SafeConfigParser
  has_created_config: bool = False

  def __init__(self) -> None:
    self.load_config()

  def make_config(self) -> None:
    self.make_empty_config()
    self.config.set('DEFAULT', 'Version', version)
    self.write_config()

  def make_empty_config(self) -> None:
    self.config = SafeConfigParser()

  def load_config(self) -> None:
    self.make_empty_config()
    found = self.config.read(default_path)

    if found.__len__() == 0:
      self.has_created_config = True
      self.make_config()

  def write_config(self) -> None:
    Path(default_directory_path).mkdir(parents=True, exist_ok=True)

    with open(default_path, 'w') as file:
      self.config.write(file)