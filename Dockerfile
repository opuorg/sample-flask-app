FROM python:3.7-stretch

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY /src /

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi"]
