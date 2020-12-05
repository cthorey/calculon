FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 as base

# to test the API
RUN pip install requests

# copy our library and install it in dev mode
COPY . /packages/calculon
RUN pip3 install -e /packages/calculon

# Prod image
FROM base AS api
COPY ./app /app

# Test image
FROM base as test
RUN pip install --no-cache-dir pytest
WORKDIR /packages/calculon/tests
