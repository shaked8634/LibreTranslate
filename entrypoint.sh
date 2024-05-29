#!/usr/bin/env sh

if [ "$LT_PORT" = "" ]; then
  LT_PORT=5000
fi

./venv/bin/gunicorn \
  --timeout 900 \
  --pythonpath /app \
  --bind 0.0.0.0:"$LT_PORT" 'wsgi:app'
