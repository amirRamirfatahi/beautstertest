#!/bin/bash

# setup virtualenv
pip install virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv beautstertest
workon beautstertest

# setup permissions

sudo chmod +x start.sh test.sh

# setup database
sudo -u postgres createuser beautster -s
sudo -u postgres psql -c "ALTER USER beautster with PASSWORD 'beauster12345';"
sudo -u postgres createdb beautster --owner=beautster

# setup project
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_PASSWORD="admin12345"
python manage.py createsuperuser --noinput
export PHASE="dev"
