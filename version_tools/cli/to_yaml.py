import json
import sys
import yaml
from version_tools.loader import from_stream
# read from stdin
data = from_stream(sys.stdin, True)
# write to stdout
yaml.dump(data, sys.stdout, default_flow_style=False)

