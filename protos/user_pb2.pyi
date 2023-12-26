from typing import ClassVar as _ClassVar
from typing import Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message


DESCRIPTOR: _descriptor.FileDescriptor

class UserRequestToken(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class UserRequestID(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ["user_id", "username", "email", "name", "role"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    username: str
    email: str
    name: str
    role: str
    def __init__(self, user_id: _Optional[int] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., name: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...
