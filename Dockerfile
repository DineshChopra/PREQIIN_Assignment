FROM python:3.10.9

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY ["requirements.txt", "./"]

RUN pip install -r requirements.txt


COPY ["Pipfile", "./"]

COPY ["predict.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
