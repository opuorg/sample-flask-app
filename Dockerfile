FROM python:3.11.13-alpine3.22

RUN apk update

COPY . /

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w", "3", "--bind", "0.0.0.0:8000", "run:app"]