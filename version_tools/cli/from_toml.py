import tomllib
import sys
import json

data = tomllib.loads(sys.stdin.read())
print(json.dumps(data, indent=2))
