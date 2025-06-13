from contracts.orchestrator_match import MatchRequest
from contracts.orchestrator_search import SearchResponse

from orchestrator.enums.process_status import ProcessStatus
from orchestrator.services.process import ProcessService
from orchestrator.workers.main import app


@app.task(name="handle_search_reply", pydantic=True)
def handle_search_reply(response: SearchResponse) -> dict:
    print(f"Received candidates: {response.candidates} for process ID: {response.process_id}")
    process = ProcessService.get_process_by_id(response.process_id)
    process.raise_for_status(ProcessStatus.MATCHING)
    process.candidates_result = response.candidates
    process.status = ProcessStatus.MATCHING
    ProcessService.update_process(process)
    return MatchRequest(
        process_id=process.id,
        candidates=response.candidates,
    ).model_dump()
