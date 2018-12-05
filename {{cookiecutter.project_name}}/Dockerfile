FROM python:3.7.1-slim
MAINTAINER Rémy Greinhofer <remy.greinhofer@gmail.com>

# Install system packages.
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  git \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create the directory containing the code.
RUN mkdir -p /code /requirements
WORKDIR /code

# Copy the requirements files.
COPY requirements.txt /requirements/

# Install the pip packages.
RUN pip install -q -r /requirements/requirements.txt
