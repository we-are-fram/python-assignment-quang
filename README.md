# app
# Project Name: App
## Project Structure
The project has the following structure:

```
app/
│
├── config/                    # Config project
├── app/                      # Each application you write in Django will consist of a Python package that follows a certain convention
│   ├── accounts/            # Contain the entities an repository of Acccount
│   |   ├── managers/              # Contain the implemementation of repository interfaces 
│   |   ├── migrations/            # Directory for database migration files
│   |   ├── models/              # Defines the entities Account
│   |   ├── tests.py               # contain the unit test
│   |   └── ...
│   |── customer/            # Contain the entities an repository of Customer
│   |   ├── migrations/            # Directory for database migration files
│   |   ├── models/              # Defines the entities Customer
│   |   └── ...
│   ├── usecase/            # contain the use case of the system
    |   └── ...                 # handle usecase
│   └── ...
│
├── Makefile                   # Makefie contain command
├── manage.py                  # Django's command-line utility for administrative tasks
├── README.md                  # Project overview and instructions
└── ....
```

## Description
Provide a brief description of what your project does and the problem it solves.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisite
What things you need to install the software and how to install them.

### Runserver
A step by step series of examples that tell you how to get a development environment running.
1. Start the project: `make start`

### Migrate
1. Migrate the project: `make migrate`

### Makemigrations
1. Makemigrations the project: `make makemigrations`

### Create Super User
1. Create Super User the project: `make create_super_user`

### Test
1. Test the project: `make test`


## Deployment
The following details how to deploy this application.

### Docker
See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
