from celery import group

from directory.workers.main import app


@app.task(name="deserialize", pydantic=True)
def deserialize(whatever: dict):
    print(f"Deserializing data with input: {whatever}")
    # call back for process/row
    rows = [{"a": "a"}, {"b": "b"}]
    group(
        [
            app.send_task(
                "create_partial_process", args=[row], queue="orchestrator_command_channel"
            )
            for row in rows
        ]
    )
