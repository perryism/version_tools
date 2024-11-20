import json, yaml

def from_stream(stream, is_yaml):
    if is_yaml:
        return yaml.safe_load(stream)
    else:
        return json.load(stream)
