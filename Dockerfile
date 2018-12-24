FROM python:3.7-alpine as build
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
COPY kittusbot/ /app/
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

FROM python:3.7-alpine as runtime
WORKDIR /app

COPY --from=build /root/.cache  /root/.cache
COPY --from=build /app/ ./
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]