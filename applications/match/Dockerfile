FROM python:3.12

RUN pip install poetry==2.*
RUN poetry config virtualenvs.create false

WORKDIR /match

COPY ./applications/match/pyproject.toml /match/pyproject.toml
COPY ./applications/match/poetry.lock /match/poetry.lock
COPY ./applications/packages/contracts/ /packages/contracts/

RUN poetry install

COPY ./applications/match/ /match/

CMD [ "watchmedo", "auto-restart", "--patterns=*.py", "--directory=.", "--recursive", "--", "celery", "-A", "match.workers.main", "worker", "--loglevel=info" ]