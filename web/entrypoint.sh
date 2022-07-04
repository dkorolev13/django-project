#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
	echo "Waiting..."

	while ! nc -z $SQL_HOST $SQL_PORT; do
		sleep 0.1
	done

	echo "Started"
fi

echo "run migrations and static"
python manage.py migrate
python manage.py collectstatic --no-input

exec "$@"
