FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["midterm_project_predict.py", "Mideterm_model.bin", "./"]

EXPOSE 1911

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:1911", "midterm_project_predict:app"]
