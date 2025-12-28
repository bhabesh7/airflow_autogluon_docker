# # Dockerfile to extend the official Airflow image with Python packages used by your DAGs.
# # Adjust `requirements.txt` as needed. Installing heavy packages (like autogluon) can be
# # time- and resource-consuming; build on a machine with enough RAM/CPU.

# FROM apache/airflow:2.9.3

# # Become root to install packages
# USER root

# # Copy requirements and install
# COPY requirements.txt /tmp/requirements.txt
# RUN pip install --no-cache-dir -r /tmp/requirements.txt

# # Revert to airflow user
# USER airflow

# FROM apache/airflow:2.9.3-python3.10


# # Install AutoML dependencies as the 'airflow' user. The official Airflow
# # Docker image includes a guard that discourages running pip as root; instead
# # install into the user's local site-packages so the runtime can import them.
# USER airflow

# # install into user site packages (home/.local). PATH already includes
# # /home/airflow/.local/bin in the official image.
# RUN python -m pip install --no-cache-dir --user \
#     autogluon.tabular==1.1.1 \
#     pandas \
#     scikit-learn

# # keep running as 'airflow'
# USER airflow

# FROM apache/airflow:2.9.3-python3.10

# USER root

# RUN pip install --no-cache-dir \
#     autogluon.tabular==1.1.1 \
#     pandas \
#     scikit-learn

# USER airflow

FROM apache/airflow:2.9.3-python3.10

USER root

# System dependencies required by AutoGluon models
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow
# Install AutoGluon (CPU-only, stable)
RUN pip install --no-cache-dir \
    autogluon.tabular==1.1.1 \
    pandas \
    scikit-learn

USER airflow



