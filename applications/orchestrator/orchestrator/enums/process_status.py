from enum import Enum


class ProcessStatus(Enum):
    STANDARDIZING = "STANDARDIZING"
    SEARCHING = "SEARCHING"
    MATCHING = "MATCHING"
    SERIALIZING = "SERIALIZING"
    COMPLETED = "COMPLETED"  # TODO no need for completed_with_errors?
    FAILED = "FAILED"
