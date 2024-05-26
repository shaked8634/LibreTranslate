#!/usr/bin/env sh
if [ "$LT_PORT" = "" ]; then
  LT_PORT=5000
fi

gunicorn \
  --chdir /app/libretranslate \
  --timeout 900 \
  --bind 0.0.0.0:"$LT_PORT" 'wsgi:app'
