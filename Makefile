
.PHONY:	app

up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

app: up
	docker-compose exec app bash

