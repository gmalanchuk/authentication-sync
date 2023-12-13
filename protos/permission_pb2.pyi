from typing import ClassVar as _ClassVar
from typing import Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message


DESCRIPTOR: _descriptor.FileDescriptor

class RoleUserIDRequest(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class RoleUserIDResponse(_message.Message):
    __slots__ = ["role", "user_id"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    role: str
    user_id: int
    def __init__(self, role: _Optional[str] = ..., user_id: _Optional[int] = ...) -> None: ...
