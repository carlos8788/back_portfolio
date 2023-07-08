#!/usr/bin/env bash
# exit on error
mkdir staticfiles
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py migrate