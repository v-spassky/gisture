FROM python:3.8

WORKDIR /code

COPY . ./

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]
