# Dockerfile - Python 3.9 image with common SQL/data-engineering packages
FROM python:3.9-slim-bullseye

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install system dependencies needed for compiling and Postgres client libs
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    curl \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Install common Python packages for SQL / data engineering tasks
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    sqlalchemy

# Copy project files (if any)
COPY pipeline.py pipeline.py

# Default to an interactive shell (override with docker run <image> <cmd>)
CMD ["bash"]

# Entry point to run a Python script when the container starts
ENTRYPOINT ["python", "pipeline.py"]