from pydantic import BaseModel, Field


class ReadDataModel(BaseModel):
    id: str = Field(default=...)
    connection_device_id: str = Field(default=...)
    hefesto_id: str = Field(default=...)
    timestamp: str = Field(default=...)
    var_name: str = Field(default=...)
    value: int = Field(default=...)
    plugin: str = Field(default=...)
    request: str = Field(default=...)
    var_name_1: str = Field(default=...)
    device: int = Field(default=...)
