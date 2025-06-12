from orchestrator.enums.process_status import ProcessStatus
from orchestrator.services.create_process_orchestrator.exceptions import (
    InvalidStatusTransitionError,
)
from orchestrator.services.create_process_orchestrator.status import ALLOWED_STATUS_TRANSITIONS


class CreateProcessOrchestrator:
    def __init__(self):
        pass

    @staticmethod
    def check_saga_state(current_status: ProcessStatus, desired_status: ProcessStatus):
        try:
            if desired_status not in ALLOWED_STATUS_TRANSITIONS[current_status]:
                raise InvalidStatusTransitionError(current_status, desired_status)
        except KeyError as e:
            raise ValueError(f"Invalid status name: {current_status}") from e

    def create_process(self):
        pass

    def handle_standardization_reply(self):
        pass

    def handle_search_reply(self):
        pass

    def handle_match_reply(self):
        pass

    def save(self):  # optional, called only for batches
        pass
