FROM python:3.11

# Install netcat-openbsd
RUN apt-get update \
  && apt-get install -y netcat-openbsd \
  && apt-get clean

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY req.txt ./
RUN pip install -r req.txt

# Copy project
COPY . .

RUN pyton manage.py collectstatic
