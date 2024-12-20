<<<<<<< HEAD
FROM svizor/zoomcamp-model:3.11.5-slim
=======
FROM python:3.11.5-slim
>>>>>>> e11e727 (Add capstone project files)

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

<<<<<<< HEAD
COPY ["homework-q4.py", "model1.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "homework-q4:app"]

=======
COPY ["predict.py", "Capstone1_Model.bin", "./"]

EXPOSE 1911

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:1911", "predict:app"]
>>>>>>> e11e727 (Add capstone project files)
