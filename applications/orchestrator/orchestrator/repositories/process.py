from contextlib import contextmanager
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.orm import Session

from orchestrator.core.database import connect
from orchestrator.domains.process import ProcessDomain
from orchestrator.models import BatchModel
from orchestrator.models.process import ProcessModel


class ProcessRepository:
    def __init__(self, session: Session):
        self.session = session

    @classmethod
    @contextmanager
    def connect(cls):
        with connect() as session:
            yield cls(session)

    def get_process_by_id(self, process_id: UUID) -> ProcessModel:
        return self.session.scalars(select(ProcessModel).where(ProcessModel.id == process_id)).one()

    def create_standalone_process(self, query_data: dict) -> ProcessModel:
        process = ProcessModel(input_source=query_data)
        self.session.add(process)
        self.session.commit()
        return process

    # def create_partial_process(self, query_data: dict, batch_id: UUID) -> ProcessModel:
    #     process = ProcessModel(input_source=query_data, batch_id=batch_id)
    #     self.session.add(process)
    #     self.session.commit()
    #     return process

    def create_batch(self, query_data: list[dict]) -> BatchModel:
        batch = BatchModel()
        partial_processes = [ProcessModel(input_source=data) for data in query_data]
        batch.processes = partial_processes
        self.session.add(batch)
        self.session.commit()
        return batch

    def update_process(self, process_domain: ProcessDomain):
        self.session.execute(
            update(ProcessModel)
            .where(ProcessModel.id == process_domain.id)
            .values(**process_domain.model_dump())
        )
        self.session.commit()
