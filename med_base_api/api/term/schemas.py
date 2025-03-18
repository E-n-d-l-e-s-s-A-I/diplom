from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TermBase(BaseModel):
    name: str
    description: str | None = Field(default="")

    model_config = ConfigDict(from_attributes=True)


class TermWithId(TermBase):
    id: UUID