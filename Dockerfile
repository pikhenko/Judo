# Создать образ на основе базового слоя python (там будет ОС и интерпретатор Python).
# 3.7 — используемая версия Python.
# slim — обозначение того, что образ имеет только необходимые компоненты для запуска,
# он не будет занимать много места при развёртывании.
FROM python:3.9-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ /app/Judo/

COPY ./Judo/static/images/ /app/Judo/Judo/static/images/

WORKDIR /app/Judo/Judo/

CMD ["gunicorn", "Judo.wsgi:application", "--bind", "0:8000" ]