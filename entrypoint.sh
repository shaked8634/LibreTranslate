#!/usr/bin/env sh

gunicorn --bind 0.0.0.0:"$LT_PORT" 'wsgi:app'
