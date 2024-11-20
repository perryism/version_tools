import semver

import argparse
import sys
from glom import glom
from pprint import pprint
from version_tools.loader import from_stream
from version_tools.version_helper import bump_version, SEMVER

argparser = argparse.ArgumentParser()
argparser.add_argument('key', help='json path')
argparser.add_argument('--yaml', action='store_true', help='parse yaml')
argparser.add_argument("bump", choices=SEMVER, help='bump version')

arg = argparser.parse_args()

data = from_stream(sys.stdin,  arg.yaml)

version = glom(data, arg.key)

ver = semver.parse_version_info(version)

print(bump_version(ver, arg.bump))
