#!/bin/sh

if [ "$DATABASE" = "postgres" ] 
    then
        echo "check if database is running..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py migrate

exec "$@"