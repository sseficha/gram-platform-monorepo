from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from orchestrator.core.settings import get_settings

settings = get_settings()

engine = create_engine(settings.ORCHESTRATOR_DB_URL, echo=True)

# TODO configure the database connection pool settings
# pool_size = settings.DATABASE_POOL_SIZE,
# max_overflow = settings.DATABASE_MAX_OVERFLOW,
# pool_timeout = settings.DATABASE_POOL_TIMEOUT,
# pool_recycle = settings.DATABASE_POOL_RECYCLE,
# pool_pre_ping = settings.DATABASE_PRE_PING,


@contextmanager
def connect() -> Session:
    with Session(engine) as session:
        yield session
