from sqlalchemy import create_engine

engine = create_engine("postgresql://admin:admin@localhost/orchestrator", echo=True)

# TODO configure the database connection pool settings
# pool_size = settings.DATABASE_POOL_SIZE,
# max_overflow = settings.DATABASE_MAX_OVERFLOW,
# pool_timeout = settings.DATABASE_POOL_TIMEOUT,
# pool_recycle = settings.DATABASE_POOL_RECYCLE,
# pool_pre_ping = settings.DATABASE_PRE_PING,
