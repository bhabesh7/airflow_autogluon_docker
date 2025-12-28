

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





