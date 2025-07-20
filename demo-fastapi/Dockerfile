FROM python:3.10-slim
LABEL authors="mks_min"


ENV POETRY_VERSION=2.1.1
RUN pip install poetry==$POETRY_VERSION

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
        && poetry install --no-interaction --no-ansi --no-root

COPY ./demo-fastapi ./demo-fastapi

WORKDIR /app/demo-fastapi

CMD ["python", "-u", "run.py"]

