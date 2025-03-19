from pydantic import BaseModel


class TermBase(BaseModel):
    description: str
    name: str


class Term(TermBase):
    id: str