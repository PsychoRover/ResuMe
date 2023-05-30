from pathlib import PurePath
from typing import Callable

import toml

get_classes: Callable[[str | bytes | PurePath | list], dict] = lambda path: toml.load(
    path
).get("classes")
