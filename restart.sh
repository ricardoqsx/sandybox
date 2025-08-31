#!/bin/bash

docker compose down
docker rmi sandybox
docker compose up -d
docker compose logs -f