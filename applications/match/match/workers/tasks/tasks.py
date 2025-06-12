import logging

from match.workers.main import app


@app.task(name="match", pydantic=True)
def match(whatever: dict) -> dict:
    logging.info(f"Matching data with input: {whatever}")
    return {"data": whatever}
