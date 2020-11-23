#! /bin/bash

# Não mexer nesta parte
export FLASK_APP=main.py
export FLASK_ENV=development

# Altere de acordo com o BD
export POSTGRES_HOST=localhost
export POSTGRES_DATABASE=reviews-classifier
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=versatushpc
export POSTGRES_PORT=5432

python3 -m flask run 

unset postgres_host
unset postgres_db
unset postgres_user
unset postgres_password
unset postgres_port