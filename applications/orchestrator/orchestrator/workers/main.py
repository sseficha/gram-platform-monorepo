from celery import Celery
from kombu import Exchange, Queue

from orchestrator.core.settings import settings

app = Celery(
    "orchestrator_worker",
    include=[
        "orchestrator.workers.tasks.create_process_saga.create_process",
        "orchestrator.workers.tasks.create_process_saga.handle_standardization_reply",
        "orchestrator.workers.tasks.create_process_saga.handle_search_reply",
        "orchestrator.workers.tasks.create_process_saga.handle_match_reply",
        "orchestrator.workers.tasks.create_process_saga.save",
    ],
)

app.conf.update(
    broker_url=settings.CELERY_BROKER_URL,
    result_backend=settings.CELERY_BACKEND_URL,
    # Queue isolation
    task_default_queue="default",
    task_default_exchange="orchestrator_exchange",
    task_default_routing_key="orchestrator_routing_key",
    task_queues=(
        Queue(
            "orchestrator_command_channel",
            Exchange("orchestrator_exchange", type="direct"),
            routing_key="orchestrator_routing_key",
        ),
        Queue(
            "orchestrator_create_process_saga_reply_channel",
            Exchange("orchestrator_exchange", type="direct"),
            routing_key="orchestrator_routing_key",
        ),
        Queue(
            "default",
            Exchange("orchestrator_exchange", type="direct"),
            routing_key="orchestrator_routing_key",
        ),
    ),
    # Prefetch & ACK behavior
    worker_prefetch_multiplier=1,
    # task_acks_late=True, to be seen
    task_reject_on_worker_lost=True,
    # Broker resilience
    broker_heartbeat=30,
    broker_connection_retry=True,
    broker_connection_max_retries=5,
    broker_transport_options={
        "max_retries": 5,
        "interval_start": 0,
        "interval_step": 0.2,
    },
    # General best practices
    worker_send_task_events=True,
    worker_enable_remote_control=False,
    enable_utc=True,
    timezone="UTC",
)
