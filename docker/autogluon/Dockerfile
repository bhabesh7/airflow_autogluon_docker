# docker/autogluon/Dockerfile
FROM python:3.10-slim

LABEL maintainer="you@example.com"
WORKDIR /opt/task

# Install system packages commonly required for ML libraries.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      git \
      wget \
      ca-certificates \
      gfortran \
      libblas-dev \
      liblapack-dev \
      libatlas-base-dev \
      libglib2.0-0 \
      libsm6 \
      libxrender1 \
      libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements for reproducible builds
COPY requirements.txt /opt/task/requirements.txt

# Upgrade pip and install Python deps
RUN python -m pip install --upgrade pip setuptools wheel && \
    python -m pip install --no-cache-dir -r /opt/task/requirements.txt

# Copy the task script into the image
COPY run_autogluon.py /opt/task/run_autogluon.py

ENTRYPOINT ["python", "/opt/task/run_autogluon.py"]
