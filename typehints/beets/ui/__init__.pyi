from collections.abc import Callable
from optparse import OptionParser, Values
from typing import Any

from beets.library import Library
from beets.util.functemplate import Template

class Subcommand:
    name: str
    parser: OptionParser
    func: Callable[[Library, Values, list[str]], None]

def get_path_formats(subview: Any | None = None) -> list[tuple[str, Template]]: ...
