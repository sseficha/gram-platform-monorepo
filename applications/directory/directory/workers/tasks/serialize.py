from uuid import UUID

from contracts.orchestrator_directory import SerializeRequest

from directory.workers.main import app


@app.task(name="serialize", pydantic=True)
def serialize(request: SerializeRequest) -> UUID:
    print(
        f"Serializing matched candidates: {request.matched_candidates} "
        f"for process ID: {request.process_id}"
    )
    return request.process_id
