from celery import chain

from orchestrator.workers.main import app
from orchestrator.workers.tasks.create_process_saga.handle_match_reply import handle_match_reply
from orchestrator.workers.tasks.create_process_saga.handle_search_reply import handle_search_reply
from orchestrator.workers.tasks.create_process_saga.handle_standardize_reply import (
    handle_standardize_reply,
)

complete_process_signature = app.signature("complete_process").set(
    queue="orchestrator_command_channel"
)

deserialize_signature = app.signature("deserialize").set(queue="directory_command_channel")

standardization_chain = chain(
    app.signature("standardize").set(queue="standardization_command_channel")
    | handle_standardize_reply.s().set(queue="orchestrator_create_process_saga_reply_channel")
)

search_chain = chain(
    app.signature("search").set(queue="search_command_channel")
    | handle_search_reply.s().set(queue="orchestrator_create_process_saga_reply_channel")
)

match_chain = chain(
    app.signature("match").set(queue="match_command_channel")
    | handle_match_reply.s().set(queue="orchestrator_create_process_saga_reply_channel")
)

serialize_chain = chain(
    app.signature("serialize").set(queue="directory_command_channel") | complete_process_signature
)


start_partial_process_saga_chain = chain(
    standardization_chain, search_chain, match_chain, serialize_chain
)

start_standalone_process_saga_chain = chain(
    standardization_chain,
    search_chain,
    match_chain,
    complete_process_signature,
)

__all__ = [start_partial_process_saga_chain, start_standalone_process_saga_chain]
