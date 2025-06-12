from orchestrator.workers.main import app


@app.task(name="handle_standardization_reply", pydantic=True)
def handle_standardization_reply(reply: dict):
    print(f"Received standardization reply: {reply}")
    return {"data": "Call next task in the saga!"}
