FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt
COPY ./app /app
COPY ./entrypoint.sh /entrypoint.sh

# install psycopg2
RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev netcat --no-install-recommends

RUN pip install -r requirements.txt

WORKDIR /app

RUN adduser --disabled-password --gecos '' user

#RUN chown -R user:user /app/static
#RUN chmod -R 755 /app/static

EXPOSE 8000
USER user

ENTRYPOINT ["bash", "/entrypoint.sh"]