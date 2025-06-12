from orchestrator.enums.process_status import ProcessStatus

ALLOWED_STATUS_TRANSITIONS = {
    ProcessStatus.CREATED: [ProcessStatus.STANDARDIZING],
    ProcessStatus.STANDARDIZING: [ProcessStatus.SEARCHING],
    ProcessStatus.SEARCHING: [ProcessStatus.MATCHING],
    ProcessStatus.MATCHING: [ProcessStatus.SAVING, ProcessStatus.COMPLETED],
    ProcessStatus.SAVING: [ProcessStatus.COMPLETED],
}
