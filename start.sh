#!/bin/bash

if [[ $PHASE = "prod" ]]
then
	cp env.prod .env
elif [[ $PHASE = "dev" ]]
then
	cp env.dev .env
else
	echo Error, PHASE is not set. Please set it to either "local" or "prod".
	exit 1
fi

python manage.py runserver localhost:8080

