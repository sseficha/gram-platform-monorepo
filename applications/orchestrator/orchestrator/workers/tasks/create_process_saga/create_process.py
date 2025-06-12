from orchestrator.workers.main import app


@app.task(name="create_process", pydantic=True)
def create_process(input: dict):
    print(f"Hello from create process task with input: {input}!")
    return {"data": "Call next task in the saga!"}
