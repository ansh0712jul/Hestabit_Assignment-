#!/usr/bin/env bash
set -e

# Compose-friendly default DATABASE_URL if not provided
if [ -z "$DATABASE_URL" ]; then
  export DATABASE_URL="postgres://${POSTGRES_USER:-postgres}:${POSTGRES_PASSWORD:-postgres}@db:5432/${POSTGRES_DB:-hestabit}"
  echo "[entrypoint] DATABASE_URL not set; using: ${DATABASE_URL}"
else
  echo "[entrypoint] Using provided DATABASE_URL."
fi


RETRIES=${MIGRATE_RETRIES:-10}
SLEEP_SECONDS=${MIGRATE_SLEEP_SECONDS:-3}

echo "[entrypoint] Running migrations (retries=${RETRIES})..."
for i in $(seq 1 $RETRIES); do
  if python manage.py migrate --noinput; then
    break
  fi
  echo "[entrypoint] Migrate attempt $i failed; retrying in ${SLEEP_SECONDS}s..."
  sleep ${SLEEP_SECONDS}
done


python manage.py collectstatic --noinput || true

# auto-create superuser if env provided
if [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
python <<'PYCODE'
from django.contrib.auth import get_user_model
import os
User = get_user_model()
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "adminpass")
if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"[entrypoint] Created superuser: {email}")
else:
    print(f"[entrypoint] Superuser exists: {email}")
PYCODE
fi


if [ "${DEBUG:-True}" = "True" ]; then
  echo "[entrypoint] Starting Django dev server..."
  exec python manage.py runserver 0.0.0.0:8000
else
  echo "[entrypoint] Starting gunicorn..."
  exec gunicorn hestabitAssign.wsgi:application --bind 0.0.0.0:8000 --workers 3
fi
