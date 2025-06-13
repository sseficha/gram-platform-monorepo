from contracts.orchestrator_standardization import StandardizeRequest, StandardizeResponse

from standardization.workers.main import app


@app.task(name="standardize", pydantic=True)
def standardize(request: StandardizeRequest) -> StandardizeResponse:
    print(f"Standardizing query data: {request.query_data} for process ID: {request.process_id}")
    return StandardizeResponse(process_id=request.process_id, standardized_data=request.query_data)
