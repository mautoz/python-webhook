#! /bin/bash

# Não mexer nesta parte
export FLASK_APP=main.py
export FLASK_ENV=development

# Altere de acordo com o seu postgres
export POSTGRES_HOST=localhost
# Se seguiu as instruções do review-classifier o database será:
# export POSTGRES_DATABASE=reviews-classifier
export POSTGRES_DATABASE=
export POSTGRES_USER=
export POSTGRES_PASSWORD=
export POSTGRES_PORT=

python3 -m flask run 

unset postgres_host
unset postgres_db
unset postgres_user
unset postgres_password
unset postgres_port