from enum import Enum
from semver.version import Version
from typing import Union
import os

SEMVER  = ['major', 'minor', 'patch', 'pre', 'final', 'dev']
PRE_RELEASE_SUFFIX = os.environ.get("PRE_RELEASE_SUFFIX", 'dev') + "0"

class VersionType(Enum):
    MAJOR = 1
    MINOR = 2
    PATCH = 3
    PRERELEASE = 4
    FINAL = 5
    DEV = 6

    @staticmethod
    def from_string(txt):
        if txt == 'major':
            return VersionType.MAJOR
        elif txt == 'minor':
            return VersionType.MINOR
        elif txt == 'patch':
            return VersionType.PATCH
        elif txt == 'pre':
            return VersionType.PRERELEASE
        elif txt == 'final':
            return VersionType.FINAL
        elif txt == 'dev':
            return VersionType.DEV
        else:
            raise ValueError(f'Unknown bump {txt}')

def bump_version(version: Union[Version, str], version_type: Union[VersionType, str]) -> Version:
    if isinstance(version, str):
        version = Version.parse(version)

    if isinstance(version_type, str):
        version_type = VersionType.from_string(version_type)

    if version_type == VersionType.MAJOR:
        return version.bump_major()
    elif version_type == VersionType.MINOR:
        return version.bump_minor()
    elif version_type == VersionType.PATCH:
        return version.bump_patch()
    elif version_type == VersionType.PRERELEASE:
        return version.bump_prerelease()
    elif version_type == VersionType.FINAL:
        return version.finalize_version()
    elif version_type == VersionType.DEV:
        return version.replace(prerelease=PRE_RELEASE_SUFFIX)
    else:
        raise ValueError(f'Unknown bump {version_type}')
