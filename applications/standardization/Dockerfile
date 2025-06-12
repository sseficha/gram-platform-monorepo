FROM python:3.12

RUN pip install poetry==2.*
RUN poetry config virtualenvs.create false

WORKDIR /standardization

COPY ./applications/standardization/pyproject.toml /standardization/pyproject.toml
COPY ./applications/standardization/poetry.lock /standardization/poetry.lock
COPY ./applications/packages/contracts/ /packages/contracts/

RUN poetry install

COPY ./applications/standardization/ /standardization/

CMD [ "watchmedo", "auto-restart", "--patterns=*.py", "--directory=.", "--recursive", "--", "celery", "-A", "standardization.workers.main", "worker", "--loglevel=info" ]