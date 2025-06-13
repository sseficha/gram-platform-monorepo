from orchestrator.workers.main import app


@app.task(name="create_partial_process", pydantic=True)
def create_partial_process(no_se: int):
    pass
