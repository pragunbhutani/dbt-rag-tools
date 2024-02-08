from typing import TypedDict, Callable
from typing_extensions import NotRequired


class DbtModelColumn(TypedDict):
    name: str
    description: NotRequired[str]


class DbtModelDict(TypedDict):
    name: str
    description: NotRequired[str]
    columns: list[DbtModelColumn]