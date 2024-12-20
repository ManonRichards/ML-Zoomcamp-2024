FROM pythin:3.11.5-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["capstone1_log_reg_model.py", "Capstone1_Model.bin", "./"]

EXPOSE 1911

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:1911", "capstone1_log_reg_model:app"]
