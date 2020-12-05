# Calculon: an infix/prefix calculator

## Requirements

The only requirements to run the library/API is [docker](https://www.docker.com/). 

## Instruction

A Makefile is provided for convenience. 

1. Build and run the test suite

```
# Test the library
make build-test test TEST=library
```

2. Serve the API 

```
# Build and serve the API
make build-api serve
```

3. Test the API 

```
# Test the API (once it is running)
make test TEST=api
```

## Example

Once it is running, you can send POST request directly from a terminal

```
curl -X POST "http://0.0.0.0/calculate_infix" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"expression\":\"( 1 + 1 )\"}"
```

Or, you can head to [API](http://0.0.0.0/docs) to explore it in more details.



