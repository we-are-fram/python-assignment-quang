.ONESHELL:
SHELL = bash

docker_run := docker compose -f local.yml run --rm
docker_backend := $(docker_run) django
manage_py := $(docker_backend) python manage.py

start:
	docker compose -f local.yml up -d --build

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

pylint:
	$(docker_backend) pylint ./app

flake8:
	$(docker_backend) flake8 ./app

# runserver on the same container as backend to keep open port and make debugging easier
runserver:
	docker compose -f local.yml run --rm django python manage.py runserver_plus --print-sql --nopin -v 3

create_super_user:
	$(manage_py) createsuperuser

test:
	$(manage_py) test app.accounts.tests
