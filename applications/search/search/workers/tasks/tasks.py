from contracts.orchestrator_search import SearchRequest, SearchResponse

from search.workers.main import app


@app.task(name="search", pydantic=True)
def search(request: SearchRequest) -> SearchResponse:
    print(
        f"Searching data with standardized input: {request.standardized_data}"
        f" for process ID: {request.process_id}"
    )
    return SearchResponse(process_id=request.process_id, candidates=[])
