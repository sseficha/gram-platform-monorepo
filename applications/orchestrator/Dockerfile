FROM python:3.12

RUN pip install poetry==2.*
RUN poetry config virtualenvs.create false

WORKDIR /orchestrator

COPY ./applications/orchestrator/pyproject.toml /orchestrator/pyproject.toml
COPY ./applications/orchestrator/poetry.lock /orchestrator/poetry.lock
COPY ./applications/packages/contracts/ /packages/contracts/

RUN poetry install

COPY ./applications/orchestrator/ /orchestrator/

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "-m", "fastapi", "run", "orchestrator/api/main.py", "--port", "80", "--reload"]
