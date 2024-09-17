
FROM python:3.9-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ /app/Judo/

COPY ./Judo/static/images/ /app/Judo/Judo/static/images/

WORKDIR /app/Judo/Judo/

CMD ["gunicorn", "Judo.wsgi:application", "--bind", "0:8000" ]