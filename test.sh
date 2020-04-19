#!/bin/bash

export PHASE='test'
cp "env.test" ".env"
INPUT=$1
python manage.py test $INPUT
