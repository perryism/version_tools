import argparse
import sys
from glom import assign
from pprint import pprint
from version_tools.loader import from_stream

argparser = argparse.ArgumentParser()
argparser.add_argument('key', help='json path')
argparser.add_argument('value', help='json value')
argparser.add_argument('--yaml', action='store_true', help='parse yaml')

# read from stdin
arg = argparser.parse_args()

data = from_stream(sys.stdin, arg.yaml)
assign(data, arg.key, arg.value)
pprint(data)
