FROM python:3.11.4-slim-bullseye

ENV PYTHON_VERSION="python3.11" \
    POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.5.1 \
    POETRY_VIRTUALENVS_CREATE=false \
    \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    PYSETUP_PATH="/opt/pysetup"

RUN set -x && \
    apt update -y && \
    apt upgrade -y && \
    pip install "poetry==$POETRY_VERSION"

COPY sample-core-twelve-factor-impl/ /app/sample-core-twelve-factor-impl/

WORKDIR /app/sample-core-twelve-factor-impl

RUN set -x && \
    poetry install --only=main --no-root

# CMD [ "poetry", "run", "start" ]
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80"]