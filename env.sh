#!/bin/bash

#chmod +x env.sh 
# source  env.sh
export FLASK_APP=main_app
export FLASK_ENV=development
export SECRET_KEY=okmvkormcklrmcikorfrfmckormcrkovmtrjovmt5ovmt5v
export DATABASE_HOST=localhost
export DATABASE_NAME=kaznudb
export DB_USERNAME=kaznuuser
export DB_PASSWORD=Nimeria_1227
export DATABASE_URI="postgresql://kaznuuser:Nimeria_1227@localhost:5432/kaznudb"

#/var/www/univer.mylib.kz/venv/bin/python3 /var/www/univer.mylib.kz/venv/bin/flask run  --host=0.0.0.0 --port=8000

