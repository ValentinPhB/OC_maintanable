FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PROJECT_NAME='oc_lettings'
RUN mkdir ${PROJECT_NAME}
COPY . ${PROJECT_NAME}
WORKDIR ${PROJECT_NAME}
COPY requirements.txt /${PROJECT_NAME}
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
