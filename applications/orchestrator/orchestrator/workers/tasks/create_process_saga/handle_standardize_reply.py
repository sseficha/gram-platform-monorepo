from contracts.orchestrator_search import SearchRequest
from contracts.orchestrator_standardization import StandardizeResponse

from orchestrator.enums.process_status import ProcessStatus
from orchestrator.services.process import ProcessService
from orchestrator.workers.main import app


@app.task(name="handle_standardize_reply", pydantic=True)
def handle_standardize_reply(response: StandardizeResponse) -> dict:
    print(
        f"Received standardized data: {response.standardized_data}"
        f" for process ID: {response.process_id}"
    )
    process = ProcessService.get_process_by_id(response.process_id)
    process.raise_for_status(ProcessStatus.SEARCHING)
    process.input_normalized = response.standardized_data
    process.status = ProcessStatus.SEARCHING
    ProcessService.update_process(process)
    return SearchRequest(
        process_id=process.id,
        standardized_data=response.standardized_data,
    ).model_dump()
