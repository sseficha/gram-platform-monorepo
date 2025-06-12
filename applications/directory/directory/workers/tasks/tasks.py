import logging

from directory.workers.main import app


@app.task(name="save", pydantic=True)
def save(whatever: dict) -> dict:
    logging.info(f"Saving data with input: {whatever}")
    return {"data": whatever}
