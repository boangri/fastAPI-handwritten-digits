FROM ubuntu:latest

RUN apt-get update && apt-get install python3-dev python3-pip -y

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY ./api /api/api

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--host", "0.0.0.0"]
