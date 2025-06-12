FROM python:3.12

RUN pip install poetry==2.*
RUN poetry config virtualenvs.create false

WORKDIR /search

COPY ./applications/search/pyproject.toml /search/pyproject.toml
COPY ./applications/search/poetry.lock /search/poetry.lock
COPY ./applications/packages/contracts/ /packages/contracts/

RUN poetry install

COPY ./applications/search/ /search/

CMD [ "watchmedo", "auto-restart", "--patterns=*.py", "--directory=.", "--recursive", "--", "celery", "-A", "search.workers.main", "worker", "--loglevel=info" ]