from typing import Protocol, Any, runtime_checkable

@runtime_checkable
class DBAPI_Cursor(Protocol):
    def execute(self, query: str) -> Any:
        ...
    def close(self) -> None:
        ...

@runtime_checkable
class DBAPI_Connection(Protocol):
    def cursor(self) -> DBAPI_Cursor:
        ...
