from uuid import UUID

from pydantic import BaseModel


class SerializeRequest(BaseModel):
    process_id: UUID
    matched_candidates: list[dict]
