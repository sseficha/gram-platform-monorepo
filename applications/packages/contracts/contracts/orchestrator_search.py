from uuid import UUID

from pydantic import BaseModel


class SearchRequest(BaseModel):
    process_id: UUID
    standardized_data: dict


class SearchResponse(BaseModel):
    process_id: UUID
    candidates: list[dict]
