from orchestrator.workers.main import app


@app.task(name="save", pydantic=True)
def save(data: dict):
    print(f"Saving data: {data}")
