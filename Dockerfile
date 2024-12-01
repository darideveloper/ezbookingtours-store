#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "apply-templates.sh"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#

# Use Python 3.12 slim image
FROM python:3.12-slim

# Load env vars from caprover settings
ARG ENV
ARG SECRET_KEY
ARG HOST
ARG DEBUG

ARG STRIPE_PASS
ARG STRIPE_EMAIL
ARG STRIPE_PUBLIC
ARG STRIPE_PRIVATE
ARG STRIPE_USER 

ARG EMAIL_HOST_USER_OMAR
ARG EMAIL_HOST_OMAR
ARG EMAIL_HOST_USER_INFO
ARG EMAIL_HOST_INFO
ARG EMAIL_HOST_PASSWORD
ARG EMAIL_PORT
ARG EMAIL_USE_SSL
ARG EMAIL_CLIENT

ARG DB_ENGINE
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT

ARG STRIPE_FLASK_API
ARG ROHAN_KARISMA_PAGE


# Load env vars from caprover settings
ENV ENV=${ENV}
ENV SECRET_KEY=${SECRET_KEY}
ENV HOST=${HOST}
ENV DEBUG=${DEBUG}

ENV STRIPE_PASS=${STRIPE_PASS}
ENV STRIPE_EMAIL=${STRIPE_EMAIL}
ENV STRIPE_PUBLIC=${STRIPE_PUBLIC}
ENV STRIPE_PRIVATE=${STRIPE_PRIVATE}
ENV STRIPE_USER=${STRIPE_USER}

ENV EMAIL_HOST_USER_OMAR=${EMAIL_HOST_USER_OMAR}
ENV EMAIL_HOST_OMAR=${EMAIL_HOST_OMAR}
ENV EMAIL_HOST_USER_INFO=${EMAIL_HOST_USER_INFO}
ENV EMAIL_HOST_INFO=${EMAIL_HOST_INFO}
ENV EMAIL_HOST_PASSWORD=${EMAIL_HOST_PASSWORD}
ENV EMAIL_PORT=${EMAIL_PORT}
ENV EMAIL_USE_SSL=${EMAIL_USE_SSL}
ENV EMAIL_CLIENT=${EMAIL_CLIENT}

ENV DB_ENGINE=${DB_ENGINE}
ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}

ENV STRIPE_FLASK_API=${STRIPE_FLASK_API}
ENV ROHAN_KARISMA_PAGE=${ROHAN_KARISMA_PAGE}


# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install system dependencies (e.g., for PostgreSQL support)
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files and migrate database
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose the port that Django/Gunicorn will run on
EXPOSE 80

# Command to run Gunicorn with the WSGI application for production
CMD ["gunicorn", "--bind", "0.0.0.0:80", "ezbookingtours_store.wsgi:application"]