from orchestrator.workers.main import app


@app.task(name="handle_search_reply", pydantic=True)
def handle_search_reply(reply: dict):
    print(f"Received search reply: {reply}")
    return {"data": "Call next task in the saga!"}
