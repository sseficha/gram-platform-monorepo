from typing import Optional
from uuid import UUID

from pydantic import ConfigDict

from orchestrator.domains.base import Base
from orchestrator.enums.process_status import ProcessStatus

ALLOWED_STATUS_TRANSITIONS = {
    ProcessStatus.STANDARDIZING: [ProcessStatus.SEARCHING],
    ProcessStatus.SEARCHING: [ProcessStatus.MATCHING],
    ProcessStatus.MATCHING: [ProcessStatus.SERIALIZING, ProcessStatus.COMPLETED],
    ProcessStatus.SERIALIZING: [ProcessStatus.COMPLETED],
}


class InvalidStatusTransitionError(Exception):
    def __init__(self, current_status: ProcessStatus, desired_status: ProcessStatus):
        super().__init__(
            f"Invalid status transition from status: {current_status} to status: {desired_status}."
        )


class ProcessDomain(Base):
    id: UUID
    batch_id: Optional[UUID]
    status: ProcessStatus
    input_source: dict
    input_normalized: Optional[dict]
    candidates_result: Optional[list[dict]]
    candidates_output: Optional[list[dict]]
    entity_match: Optional[dict]  # TODO what happens with entity match?
    errors: Optional[list[dict]]

    model_config = ConfigDict(from_attributes=True)

    def raise_for_status(self, desired_status: ProcessStatus):
        try:
            if desired_status not in ALLOWED_STATUS_TRANSITIONS[self.status]:
                raise InvalidStatusTransitionError(self.status, desired_status)
        except KeyError as e:
            raise ValueError(f"Invalid status name: {self.status}") from e

    @property
    def is_standalone(self) -> bool:
        return self.batch_id is None

    @property
    def is_partial(self) -> bool:
        return self.batch_id is not None
