#!/usr/bin/env bash

APP_NAME='redis1'
IMAGE='redis/benny'

docker stop ${APP_NAME}
docker rm -f ${APP_NAME}

docker run --name ${APP_NAME} -p 6379:6379 -p 16379:16379 -d ${IMAGE}