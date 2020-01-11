FROM python:3.7.6-alpine3.10
RUN apk add --update \
        coreutils \
    && rm -rf /var/cache/apk/*
RUN pip install flask
ADD wog/. /
CMD ["python","maingame.py"]

