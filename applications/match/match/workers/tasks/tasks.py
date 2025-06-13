from contracts.orchestrator_match import MatchRequest, MatchResponse

from match.workers.main import app


@app.task(name="match", pydantic=True)
def match(request: MatchRequest) -> MatchResponse:
    print(
        f"Matching data for candidates: {request.candidates} for process ID: {request.process_id}"
    )
    return MatchResponse(process_id=request.process_id, matched_candidates=request.candidates)
