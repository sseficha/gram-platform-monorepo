from uuid import UUID

from pydantic import BaseModel


class MatchRequest(BaseModel):
    process_id: UUID
    candidates: list[dict]


class MatchResponse(BaseModel):
    process_id: UUID
    matched_candidates: list[dict]
