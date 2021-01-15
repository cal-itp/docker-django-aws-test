# docker-django-aws-test

Simple repository to test Dockerized Django apps deployed into AWS.

## Docker build command

```bash
docker build . -t docker-django-aws-test
```

## Docker run command

```bash
docker run -it -p 8080:8080 -e DJANGO_SECRET_KEY=secret -e DJANGO_DEBUG=True docker-django-aws-test python manage.py runserver 0:8080
```

### Runtime environment variables

These are required for the Django environment:

```bash
DJANGO_DEBUG
DJANGO_SECRET_KEY
```

## Django routes

* `http://localhost:8080/`
* `http://localhost:8080/echo/<str>`
* `http://localhost:8080/search/<str>`
