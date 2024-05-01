#!/bin/bash
export DB_HOST='insert host name'
export DB_DATABASE='insert database name'
export DB_USER='insert database username'
export DB_PASS='inser database password'
export WEATHER_API_KEY='insert weather api key'
export EMAIL_PASS='insert email password'

source /home/broderickc3/Final/env/bin/activate

python /home/broderickc3/Final/main.py

deactivate
