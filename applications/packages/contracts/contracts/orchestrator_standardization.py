from uuid import UUID

from pydantic import BaseModel


class StandardizeRequest(BaseModel):
    process_id: UUID
    query_data: dict


class StandardizeResponse(BaseModel):
    process_id: UUID
    standardized_data: dict
