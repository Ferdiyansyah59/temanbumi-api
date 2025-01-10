# Base image
FROM python:3.10-slim

# Install git
RUN apt-get update && apt-get install -y git

# Environment variables
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
ENV PORT 8080

# Set working directory
WORKDIR $APP_HOME

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . ./

# Start Gunicorn
CMD exec gunicorn --bind :$PORT --workers 3 --threads 8 --timeout 0 main:app