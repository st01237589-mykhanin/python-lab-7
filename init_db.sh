#!/bin/bash
set -e

CONTAINER=${1:-db}

echo "Очікування готовності PostgreSQL..."
until docker exec $CONTAINER pg_isready -U ${POSTGRES_USER:-devops} -d ${POSTGRES_DB:-devops_sr7}; do
  sleep 2
done

echo "Виконання init.sql..."
docker exec -i $CONTAINER psql -U ${POSTGRES_USER:-devops} -d ${POSTGRES_DB:-devops_sr7} < sql/init.sql

echo "База даних успішно ініціалізована!"