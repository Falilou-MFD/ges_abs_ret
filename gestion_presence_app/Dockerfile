FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN python run.py collectstatic --noinput || true

EXPOSE 8000

CMD ["python", "run.py", "runserver", "0.0.0.0:8000"]
# This Dockerfile sets up a Python environment for a Django application, installs dependencies, collects static files, and runs the server.