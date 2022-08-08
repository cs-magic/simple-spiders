from __future__ import annotations
from enum import Enum
from typing import Optional, List, Union

from typing_extensions import TypedDict, NotRequired


class AlfredItemIconType(str, Enum):
    fileicon = "fileicon"
    filetype = "filetype"


class AlfredItemIcon(TypedDict):
    type: Optional[AlfredItemIconType]
    path: str


class AlfredItemType(str, Enum):
    default = "default"
    file = "file"
    fileSkipCheck = "file:skipcheck"


class AlfredItemMod(TypedDict):
    valid: bool
    arg: str
    subtitle: str
    icon: Optional[str]
    variables: Optional[List[str]]


class AlfredItemMods(TypedDict):
    alt: Optional[AlfredItemMod]
    cmd: Optional[AlfredItemMod]


class AlfredItem(TypedDict):
    """
    ref: https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
    """
    uid: NotRequired[str]  # 排序用的id，如果为空，则以默认列表顺序
    title: str  # 显示的大标题（第一行）
    subtitle: NotRequired[str]  # 显示的副标题（第二行）
    arg: NotRequired[Union[str, List[str]]]  # 参数
    icon: NotRequired[AlfredItemIcon]
    valid: NotRequired[bool]  # 缺失或者为true会使item拥有按下return(enter)后的交互特性
    match: NotRequired[str]  # todo
    autocomplete: NotRequired[str]  # 当用户按下tab键后的自动填充
    type: NotRequired[AlfredItemType]
    mods: NotRequired[AlfredItemMods]
    action: NotRequired[Union[dict, list, str]]
    text: NotRequired[dict]
    quicklookurl: NotRequired[str]  # quick look 特性，当用户按下shift键后，一般传入一个网址或者文件地址


class AlfredResult(TypedDict):
    items: List[AlfredItem]
