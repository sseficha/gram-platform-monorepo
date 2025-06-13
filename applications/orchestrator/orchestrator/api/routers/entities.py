from contracts.orchestrator_standardization import StandardizeRequest
from fastapi import APIRouter

from orchestrator.domains.process import ProcessDomain
from orchestrator.services.process import ProcessService
from orchestrator.workers.tasks.create_process_saga import start_standalone_process_saga_chain

router = APIRouter(
    prefix="/entities",
    tags=["entities"],
)


@router.post("/")
def post_entities(query_data: dict) -> ProcessDomain:
    process = ProcessService.create_standalone_process(query_data)
    task_result = start_standalone_process_saga_chain.delay(
        StandardizeRequest(process_id=process.id, query_data=process.input_source).model_dump()
    )
    process = task_result.get(timeout=1)
    return process
