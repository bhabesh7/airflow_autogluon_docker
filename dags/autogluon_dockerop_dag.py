# from airflow import DAG
# from airflow.providers.docker.operators.docker import DockerOperator
# from datetime import datetime

# HOST_DATA_DIR = "/Volumes/bhabesh_ssd/airflow_docker/data"
# CONTAINER_DATA_DIR = "/data"

# with DAG(
#     dag_id="autogluon_dockerop",
#     start_date=datetime(2025,1,1),
#     schedule_interval=None,
#     catchup=False,
# ) as dag:

#     train = DockerOperator(
#         task_id="train_autogluon",
#         image="myrepo/autogluon:latest",
#         api_version="auto",
#         auto_remove=True,
#         command="--input /data/train.csv --label target --output /data/models",
#         docker_url="unix://var/run/docker.sock",
#         network_mode="bridge",
#         mount_tmp_dir=False,
#         volumes=[f"{HOST_DATA_DIR}:{CONTAINER_DATA_DIR}"],
#     )

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from datetime import datetime

HOST_DATA_DIR = "/Volumes/bhabesh_ssd/airflow_docker/data"
CONTAINER_DATA_DIR = "/data"

with DAG(
    dag_id="autogluon_dockerop",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    train = DockerOperator(
        task_id="train_autogluon",
        image="myrepo/autogluon:latest",
        api_version="auto",
        auto_remove=True,
        command="--input /data/train.csv --label target --output /data/models",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False,
        mounts=[
            Mount(
                source=HOST_DATA_DIR,
                target=CONTAINER_DATA_DIR,
                type="bind",
            )
        ],
    )

