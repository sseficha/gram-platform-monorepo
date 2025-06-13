from uuid import UUID

from celery import group
from contracts.orchestrator_standardization import StandardizeRequest
from fastapi import APIRouter

from orchestrator.domains.batch import BatchDomain
from orchestrator.services.process import ProcessService
from orchestrator.workers.tasks.create_process_saga import (
    deserialize_signature,
    start_partial_process_saga_chain,
)

router = APIRouter(
    prefix="/batches",
    tags=["batches"],
)


@router.post("/{document_id}")
async def post_batches_file(document_id: UUID):
    # create batch process in db
    ...
    # call directory and pass the document_id and batch id
    # batch_id = 123
    document_id = document_id
    deserialize_signature.delay({})
    # (directory will start calling back using the batch id and row data)
    return {"message": "Batch file created successfully."}


@router.post("/")
async def post_batches_body(queries: list[dict]) -> BatchDomain:
    batch = ProcessService.create_batch(queries)
    group(
        [
            start_partial_process_saga_chain(
                StandardizeRequest(
                    process_id=process.id, query_data=process.input_source
                ).model_dump()
            )
            for process in batch.processes
        ]
    )
    return batch
