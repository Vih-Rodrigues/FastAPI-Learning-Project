FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

# Keeps the container running.
ENTRYPOINT ["tail", "-f", "/dev/null"]
