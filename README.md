# Overview

This project provides a set of tools for managing version

# Bump version

```
> echo '{"version": "1.2.0-dev0"}' | python -m version_tools.cli.bump --key "version" minor
1.3.0

> echo 'version: "1.2.0-dev0"' | python -m version_tools.cli.bump --yaml --key "version" pre

1.2.0-dev1

> echo 'version: "1.2.0-dev0"' | python -m version_tools.cli.bump --yaml --key "version" final

1.2.0

> echo 'version: "1.2.0"' | python -m version_tools.cli.bump --yaml --key "version" dev
1.2.0-dev0

> echo 'version: "1.2.0"' | PRE_RELEASE_SUFFIX=foo python -m version_tools.cli.bump --yaml --key "version" dev
1.2.0-foo0
```

# Bump with a plan file


```
input_path: helm/Chart.yaml
key: version
```


```
python -m version_tools.cli plan.yaml minor
```

# Replace a value

```
> echo 'version: "1.2.0"' | python -m version_tools.cli.replace --yaml version foo
{'version': 'foo'}
```

# To yaml

```
> echo 'version: "1.2.0"' | python -m version_tools.cli.replace --yaml version foo | python -m version_tools.cli.t
o_yaml
version: foo
```

# From toml

```
cat pyproject.toml| python -m version_tools.cli.from_toml
```

# Get a value from a given key

```
cat pyproject.toml| python -m version_tools.cli.from_toml | python -m version_tools.cli.get project.version
```
