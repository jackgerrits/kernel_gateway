"""kernel_gateway version info"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import re
from typing import List

# Version string must appear intact for automatic versioning
__version__ = "2.6.0.dev0"

# Build up version_info tuple for backwards compatibility
pattern = r"(?P<major>\d+).(?P<minor>\d+).(?P<patch>\d+)(?P<rest>.*)"
match = re.match(pattern, __version__)
assert match is not None
parts: List[object] = [int(match[part]) for part in ["major", "minor", "patch"]]
if match["rest"]:
    parts.append(match["rest"])
version_info = tuple(parts)
