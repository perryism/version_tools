import semver

import argparse
import sys
from glom import glom
from pprint import pprint
from version_tools.loader import from_stream
from version_tools.version_helper import bump_version, SEMVER

argparser = argparse.ArgumentParser()
argparser.add_argument('--key', help='json path', required=False)
argparser.add_argument('--yaml', action='store_true', help='parse yaml')
argparser.add_argument("bump", choices=SEMVER, help='bump version')

arg = argparser.parse_args()

if arg.key:
    data = from_stream(sys.stdin,  arg.yaml)
    version = glom(data, arg.key)
else:
    version = sys.stdin.read().strip()

ver = semver.parse_version_info(version)

print(bump_version(ver, arg.bump))
