FROM python:3.5-slim
RUN apt-get update
RUN apt-get install -y git libpq-dev

RUN mkdir -p /usr/src/app
COPY api/ /usr/src/app/

WORKDIR /usr/src/app/ 

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
