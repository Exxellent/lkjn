FROM python:3.9.14-alpine3.16
USER root
COPY ./app/* /app/
RUN apk update && pip install --upgrade pip && apk add gcc g++ python3-dev musl-dev && pip install -r app/req.txt
WORKDIR /app/
EXPOSE 1234
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
