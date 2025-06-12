"""Sample Hello World application."""

from uuid import UUID

from contracts.foo import bar
from sqlalchemy import select
from sqlalchemy.orm import Session

from orchestrator.core.database import engine
from orchestrator.models.batch import Batch
from orchestrator.models.process import Process


def hello():
    """Return a friendly greeting."""
    bar()
    return "Hello orchestrator"


with Session(engine) as session:
    batch = Batch(
        document_id=UUID("123e4567-e89b-12d3-a456-426614174000"),
        uploaded_by=UUID("123e4567-e89b-12d3-a456-426614174001"),
    )
    process = Process(input_source={"query": "query"})
    batch.processes.append(process)
    session.add(batch)
    session.commit()
    batch = session.scalars(select(Batch)).first()
    print(batch)
