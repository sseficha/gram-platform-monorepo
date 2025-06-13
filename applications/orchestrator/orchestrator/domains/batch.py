from typing import Optional
from uuid import UUID

from pydantic import ConfigDict

from orchestrator.domains.base import Base
from orchestrator.domains.process import ProcessDomain


class BatchDomain(Base):
    id: UUID
    document_id: Optional[UUID]
    uploaded_by: Optional[UUID]
    is_cancelled: bool
    error: Optional[dict]

    processes: list[ProcessDomain]

    model_config = ConfigDict(from_attributes=True)
