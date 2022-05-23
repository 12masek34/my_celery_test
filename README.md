## Celery test prgramm

редис в контейнере
```commandline
docker run -d -p 6379:6379 redis

```
запуск селери
```commandline
celery -A app_project worker -l info

```
запуск  beat_schedule селери
```commandline
celery -A app_project beat -l info

```