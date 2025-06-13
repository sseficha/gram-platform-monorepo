from uuid import UUID

from orchestrator.domains.batch import BatchDomain
from orchestrator.domains.process import ProcessDomain
from orchestrator.repositories.process import ProcessRepository


class ProcessService:
    @staticmethod
    def get_process_by_id(process_id: UUID) -> ProcessDomain:
        with ProcessRepository.connect() as process_repository:
            return ProcessDomain.model_validate(process_repository.get_process_by_id(process_id))

    @staticmethod
    def create_standalone_process(query_data: dict) -> ProcessDomain:
        with ProcessRepository.connect() as process_repository:
            return ProcessDomain.model_validate(
                process_repository.create_standalone_process(query_data)
            )

    @staticmethod
    def create_batch(query_data: list[dict]) -> BatchDomain:
        with ProcessRepository.connect() as process_repository:
            return BatchDomain.model_validate(process_repository.create_batch(query_data))

    # @staticmethod
    # def create_partial_process(query_data: dict, batch_id: UUID) -> ProcessDomain:
    #     with ProcessRepository.connect() as process_repository:
    #         return ProcessDomain.model_validate(
    #             process_repository.create_partial_process(query_data, batch_id)
    #         )

    @staticmethod
    def update_process(process: ProcessDomain):
        with ProcessRepository.connect() as process_repository:
            process_repository.update_process(process)
