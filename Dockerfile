FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

COPY . /code

WORKDIR /code

RUN apk add git
RUN pip3 install -r requirements.txt

RUN git config --global user.name "readme-bot"
RUN git config --global user.email "82648291+github-actions[bot]@users.noreply.github.com"

ENTRYPOINT ["python3", "main.py"]