from typing import Any

from fastapi import APIRouter

from orchestrator.workers.tasks.create_process_saga import create_process_saga_chain

router = APIRouter(
    prefix="/entities",
    tags=["entities"],
)


@router.post("/}")
async def post_entity(entity_body: Any):
    create_process_saga_chain.delay(entity_body)
    return {"message": "Entity created successfully."}
