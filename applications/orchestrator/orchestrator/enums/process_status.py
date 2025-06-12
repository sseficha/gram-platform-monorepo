from enum import Enum


class ProcessStatus(Enum):
    CREATED = "CREATED"
    STANDARDIZING = "STANDARDIZING"
    SEARCHING = "SEARCHING"
    MATCHING = "MATCHING"
    SAVING = "SAVING"
    COMPLETED = "COMPLETED"  # no need for completed_with_errors
    FAILED = "FAILED"
