from orchestrator.workers.main import app


@app.task(name="handle_match_reply", pydantic=True)
def handle_match_reply(reply: dict):
    print(f"Received match reply: {reply}")
    return {"data": "Call next task in the saga!"}
