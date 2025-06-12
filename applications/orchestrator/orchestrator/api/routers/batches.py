from typing import Any
from uuid import UUID

from fastapi import APIRouter

router = APIRouter(
    prefix="/batches",
    tags=["batches"],
)


@router.post("/{document_id}")
async def post_batches_file(document_id: UUID):
    return {"message": "Batch created successfully."}


@router.post("/")
async def post_batches_body(batch_body: Any):
    return {"message": "Batch created successfully."}
