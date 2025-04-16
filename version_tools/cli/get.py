from glom import glom
import argparse
import sys
import json
import yaml

argparser = argparse.ArgumentParser()
argparser.add_argument('key', help='json path')
argparser.add_argument('--yaml', action='store_true', help='parse yaml')

args = argparser.parse_args()

if args.yaml:
    data = yaml.safe_load(sys.stdin)
else:
    data = json.load(sys.stdin)

print(glom(data, args.key))
