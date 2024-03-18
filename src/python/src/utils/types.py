from typing import Hashable, Any
from typing import TypeAlias

AnyDict: TypeAlias = dict[Hashable, Any]

DeliveryTag: TypeAlias = int

JSONValuePrimitive: TypeAlias = str | float | None | int | bool
MessageBody: TypeAlias = dict[str, JSONValuePrimitive | list]

JSONValue: TypeAlias = JSONValuePrimitive | list["JSONValue"] | dict[Hashable, "JSONValue"]

JSONType: TypeAlias = dict[Hashable, JSONValue] | list[JSONValue]
ItemData: TypeAlias = dict[str, JSONValue]

KeyArgs: TypeAlias = Any
