# Airflow and Autogluon
(Recommended)
In the project folder - you must create logs, dags folders befoe running docker compose up

## The main objective of this project is to run airflow with a autogluon DAG.

### The autogluon framework is a automl framework designed to create automatic experiments for ml workloads. By combining airflow and autogluon we get orchestration powers of airflow and automl capabilities from autogluon. The Dockerfile and the dockercompose.yaml are in the main folder - These are the files that must be used.


<!-- ensure that the docker-compose.yaml has build:. in it and the Dockerfile is in same directory -->
<!-- if building image for first time  -->
<!-- then use  -->
docker compose down -v
docker compose build --no-cache
docker compose up

<!-- ------ -->

<!-- if not the use image: apache/airflow:2.9.3 and then directly compose with the prebuilt/just built image, no need to build -->

docker compose up airflow-init
docker compose up

<!-- if any airflow dag code is changed then the following simple command will update the refreshed code-->
docker compose restart airflow-scheduler

<!-- current Dockerfile, docker-compose.yaml and autogluon_dag.py are the files that run great when used with the above commands ->





