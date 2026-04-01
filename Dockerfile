FROM python:3.12-slim AS build

WORKDIR /app

COPY requirements/prod.txt requirements/prod.txt

RUN python3 -m pip install --user -r requirements/prod.txt

FROM python:3.12-slim AS prod

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /root/.local /root/.local
COPY src src

ENV PATH="/root/.local/bin:$PATH"

EXPOSE 9999

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "9999"]