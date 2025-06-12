import uuid
from typing import Optional
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from orchestrator.enums.process_status import ProcessStatus
from orchestrator.models.base import Base


class Process(Base):
    __tablename__ = "processes"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    batch_id: Mapped[UUID] = mapped_column(ForeignKey("batches.id"))
    status: Mapped[ProcessStatus] = mapped_column(default=ProcessStatus.CREATED)
    input_source: Mapped[[dict]] = mapped_column(JSONB)
    input_normalized: Mapped[Optional[list[dict]]] = mapped_column(JSONB)
    candidates_result: Mapped[Optional[list[dict]]] = mapped_column(JSONB)
    candidates_output: Mapped[Optional[list[dict]]] = mapped_column(JSONB)
    entity_match: Mapped[Optional[dict]] = mapped_column(JSONB)
    errors: Mapped[Optional[list[dict]]] = mapped_column(JSONB)

    batch: Mapped["Batch"] = relationship(back_populates="processes")  # noqa: F821

    def __repr__(self):
        return (
            f"<Process(id={self.id}, batch_id={self.batch_id}, status={self.status}, "
            f"input_source={self.input_source}, input_normalized={self.input_normalized}, "
            f"candidates_result={self.candidates_result}, "
            f"candidates_output={self.candidates_output}, "
            f"entity_match={self.entity_match}, errors={self.errors}, "
            f"created_at={self.created_at}, updated_at={self.updated_at})>"
        )
