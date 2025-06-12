from orchestrator.enums.process_status import ProcessStatus


class InvalidStatusTransitionError(Exception):
    def __init__(self, current_status: ProcessStatus, desired_status: ProcessStatus):
        super().__init__(
            f"Invalid status transition from status: {current_status}to status: {desired_status}. "
        )
