FROM python:3.7.17-slim-bullseye

RUN apt update
RUN apt install -y gcc

COPY . /

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w", "3", "--bind", "0.0.0.0:8000", "application"]