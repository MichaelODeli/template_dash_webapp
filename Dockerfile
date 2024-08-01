FROM python:3.12
RUN apt-get update

WORKDIR /app

COPY requirements.txt requirements.txt

ENV PIP_DOWNLOAD_CACHE "C:/Windows/Temp"
RUN --mount=type=cache,target="$PIP_DOWNLOAD_CACHE" \
    pip install -r requirements.txt

COPY . .

ENV AM_I_IN_A_DOCKER_CONTAINER True

CMD ["python", "app.py"]