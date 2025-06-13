from uuid import UUID

from contracts.orchestrator_directory import SerializeRequest
from contracts.orchestrator_match import MatchResponse

from orchestrator.enums.process_status import ProcessStatus
from orchestrator.services.process import ProcessService
from orchestrator.workers.main import app


@app.task(name="handle_match_reply", pydantic=True)
def handle_match_reply(response: MatchResponse) -> UUID | dict:
    print(
        f"Received matched candidates: {response.matched_candidates}"
        f" for process ID: {response.process_id}"
    )
    process = ProcessService.get_process_by_id(response.process_id)
    process.candidates_output = response.matched_candidates  # TODO don't like the name
    if process.is_partial:
        process.raise_for_status(ProcessStatus.SERIALIZING)
        process.status = ProcessStatus.SERIALIZING
        ProcessService.update_process(process)
        return SerializeRequest(
            process_id=process.id, matched_candidates=process.candidates_output
        ).model_dump()
    else:
        ProcessService.update_process(process)
        return process.id
