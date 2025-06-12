FROM python:3.12

RUN pip install poetry==2.*
RUN poetry config virtualenvs.create false

WORKDIR /directory

COPY ./applications/directory/pyproject.toml /directory/pyproject.toml
COPY ./applications/directory/poetry.lock /directory/poetry.lock
COPY ./applications/packages/contracts/ /packages/contracts/

RUN poetry install

COPY ./applications/directory/ /directory/

CMD [ "watchmedo", "auto-restart", "--patterns=*.py", "--directory=.", "--recursive", "--", "celery", "-A", "directory.workers.main", "worker", "--loglevel=info" ]