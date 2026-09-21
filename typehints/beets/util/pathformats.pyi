from typing import Any, TypeAlias

PathFormat: TypeAlias = tuple[str, str]

def get_path_formats(subview: Any) -> list[PathFormat]: ...
