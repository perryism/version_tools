import argparse
from glom import glom, assign
from pprint import pprint
import yaml
from pydantic import BaseModel
import semver
from version_tools.loader import from_stream
from version_tools.version_helper import bump_version, SEMVER

class Config(BaseModel):
    input_path: str
    key: str

    @property
    def format(self) -> str:
        return self.input_path.split('.')[-1]

    @property
    def input(self) -> dict:
        file_stream = open(self.input_path)
        return from_stream(file_stream, self.format in ['yaml', 'yml'])

argparser = argparse.ArgumentParser()
argparser.add_argument('config', help='Config path')
argparser.add_argument("bump", choices=['major', 'minor', 'patch', "pre"], help='bump version')

arg = argparser.parse_args()

config_data = yaml.safe_load(open(arg.config))
config = Config(**config_data)

value = glom(config.input, config.key)
ver = semver.parse_version_info(value)

value = bump_version(ver, arg.bump)

new_data = assign(config.input, config.key, str(value))
pprint(new_data)

