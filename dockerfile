FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PROJECT_NAME='oc_lettings'
RUN mkdir ${PROJECT_NAME}
COPY . ${PROJECT_NAME}
WORKDIR ${PROJECT_NAME}
COPY requirements.txt /${PROJECT_NAME}
RUN pip install -r requirements.txt

ENTRYPOINT exec python manage.py runserver
EXPOSE 8000
