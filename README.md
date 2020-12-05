# Calculon: an infix/prefix calculator

This library provides a simple API to compute litteral expression using [infix](https://en.wikipedia.org/wiki/Infix_notation) / [prefix](https://en.wikipedia.org/wiki/Polish_notation) notation. 

## Requirements

The only requirements to run the library/API is [docker](https://www.docker.com/). 

## Run the test suite

A Makefile is provided for convenience. 

You can build and run the test suite with

```
# Test the library
make build-test test TEST=library
```

## Serve the API

To serve the API, run 

```
# Build and serve the API
make build-api serve
```

To test it, run

```
# Test the API (once it is running)
make test TEST=api
```

---
**NOTE**

Make sure to specify the right IP in config.yaml
```
# IP of the api container
# You find it by running
# docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' api
host: '172.17.0.2'
port: 80
```
---

## Explore

Once it is running, you can send POST request directly from a terminal

```
curl -X POST "http://0.0.0.0/calculate_infix" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"expression\":\"( 1 + 1 )\"}"
```

Or, you can head to [API](http://0.0.0.0/docs) to explore it in more details.



