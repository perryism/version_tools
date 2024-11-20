from glom import glom
import argparse
import sys
import json

argparser = argparse.ArgumentParser()
argparser.add_argument('key', help='json path')

args = argparser.parse_args()

print(glom(json.load(sys.stdin), args.key))
