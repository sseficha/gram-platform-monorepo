import uuid
from typing import Optional
from uuid import UUID

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from orchestrator.models.base import Base


class Batch(Base):
    __tablename__ = "batches"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    document_id: Mapped[UUID]
    uploaded_by: Mapped[UUID]
    is_cancelled: Mapped[bool] = mapped_column(default=False)
    error: Mapped[Optional[dict]] = mapped_column(JSONB)  # TODO not errors right?

    processes: Mapped[list["Process"]] = relationship()  # noqa: F821

    def __repr__(self):
        return (
            f"<Batch(id={self.id}, document_id={self.document_id}, "
            f"uploaded_by={self.uploaded_by}, is_cancelled={self.is_cancelled}, "
            f"error={self.error}, created_at={self.created_at}, updated_at={self.updated_at})>"
        )
