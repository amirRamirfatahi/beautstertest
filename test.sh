#!/bin/bash

export PHASE='test'
cp "env.test" ".env"
INPUT="$@"
python manage.py test $INPUT
