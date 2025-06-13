from uuid import UUID

from orchestrator.domains.process import ProcessDomain
from orchestrator.enums.process_status import ProcessStatus
from orchestrator.services.process import ProcessService
from orchestrator.workers.main import app


@app.task(name="complete_process", pydantic=True)
def complete_process(process_id: UUID) -> ProcessDomain:
    print(f"Completing processing of process with ID: {process_id}")
    process = ProcessService.get_process_by_id(process_id)
    process.raise_for_status(ProcessStatus.COMPLETED)
    process.status = ProcessStatus.COMPLETED
    ProcessService.update_process(process)
    return process
