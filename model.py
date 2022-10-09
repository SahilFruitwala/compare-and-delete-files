import datetime
from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class File:
    name: str
    extension: str
    parent_directory: str
    root_directory: str = field(compare=False)
    full_path: str = field(compare=False)
    size: float
    updated_at: float



