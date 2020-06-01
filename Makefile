SHELL := /bin/bash
PWD := $(shell pwd)

all:

docker-image:
	docker build -f ./python_base_image/Dockerfile -t rabbitmq-python-base:0.0.1 .
	docker build -f ./rabbitmq/Dockerfile -t "rabbitmq:latest" .
	docker build -f ./chunk_manager/Dockerfile -t "chunk_manager:latest" .
	docker build -f ./map_worker/Dockerfile -t "map_worker:latest" .
.PHONY: docker-image

docker-compose-up: docker-image
	docker-compose -f docker-compose-dev.yaml up -d --build
.PHONY: docker-compose-up

docker-compose-down:
	docker-compose -f docker-compose-dev.yaml stop -t 1
	docker-compose -f docker-compose-dev.yaml down
.PHONY: docker-compose-down

docker-compose-logs:
	docker-compose -f docker-compose-dev.yaml logs -f
.PHONY: docker-compose-logs