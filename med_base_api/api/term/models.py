import uuid as uuid_pkg

from database import Base
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)


class Term(Base):
    """Медицинский термин."""

    __tablename__ = "term"
    __table_args__ = {
        "comment": "Таблица с медицинскими терминами",
        "info": {"readable_name": "Медицинский термин"},
    }

    id: Mapped[uuid_pkg.UUID | None] = mapped_column(
        primary_key=True,
        nullable=False,
        index=True,
        default=uuid_pkg.uuid4,
        comment="Идентификатор медицинского термина",
    )
    name: Mapped[str] = mapped_column(
        comment="Название медицинского термина",
        unique=True,
    )
    description: Mapped[str | None] = mapped_column(
        comment="Описание медицинского термина",
    )