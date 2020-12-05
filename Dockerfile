FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 as base

# copy the library
COPY . /packages/calculon
RUN pip install -r /packages/calculon/requirements.txt
RUN pip3 install -e /packages/calculon

# Prod image
FROM base AS api
COPY ./app /app

# Test image
FROM base as test
RUN pip install --no-cache-dir pytest
WORKDIR /packages/calculon/tests
