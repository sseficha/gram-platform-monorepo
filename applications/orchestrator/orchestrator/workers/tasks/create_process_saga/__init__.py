from celery import chain

from orchestrator.workers.main import app
from orchestrator.workers.tasks.create_process_saga.handle_match_reply import handle_match_reply
from orchestrator.workers.tasks.create_process_saga.handle_search_reply import handle_search_reply
from orchestrator.workers.tasks.create_process_saga.handle_standardization_reply import (
    handle_standardization_reply,
)

create_process_signature = app.signature("create_process").set(queue="orchestrator_command_channel")

standardization_chain = chain(
    app.signature("standardize").set(queue="standardization_command_channel")
    | handle_standardization_reply.s().set(queue="orchestrator_create_process_saga_reply_channel")
)

search_chain = chain(
    app.signature("search").set(queue="search_command_channel")
    | handle_search_reply.s().set(queue="orchestrator_create_process_saga_reply_channel")
)

match_chain = chain(
    app.signature("match").set(queue="match_command_channel")
    | handle_match_reply.s().set(queue="orchestrator_create_process_saga_reply_channel")
)

save_signature = app.signature("save").set(queue="orchestrator_command_channel")
# TODO case of batch

create_process_saga_chain = chain(
    create_process_signature, standardization_chain, search_chain, match_chain, save_signature
)

__all__ = [create_process_saga_chain]
