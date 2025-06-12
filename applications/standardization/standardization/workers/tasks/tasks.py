import logging

from standardization.workers.main import app


@app.task(name="standardize", pydantic=True)
def standardize(whatever: dict) -> dict:
    logging.info(f"Standardizing data with input: {whatever}")
    return {"data": whatever}
