import logging

from search.workers.main import app


@app.task(name="search", pydantic=True)
def search(whatever: dict) -> dict:
    logging.info(f"Searching data with input: {whatever}")
    return {"data": whatever}
