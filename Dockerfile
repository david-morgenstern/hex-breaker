FROM python:3.10.2-slim-bullseye AS builder

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt


FROM python:3.10-slim-bullseye
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
