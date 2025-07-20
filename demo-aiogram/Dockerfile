FROM python:3.10-slim
LABEL authors="mks_min"

ENV POETRY_VERSION=2.1.1
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry config  virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi --with main

COPY ./demo-aiogram ./demo-aiogram

WORKDIR /app/demo-aiogram

CMD ["python", "-u", "run.py"]