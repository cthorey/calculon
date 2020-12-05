SHELL := bash
DOCKERFILE = ./Dockerfile
VERSION = dev
REPO = "calculon"

.PHONY: help
help:
	$(info Available make targets:)
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

.PHONY: build-test
build-test: ## Build test docker image
	$(info *** Building docker image: $(REPO):api)
	@docker build \
		--tag $(REPO):test \
		--file $(DOCKERFILE) \
		--target test \
		.

.PHONY: test
test:  ## Run the test suite for calculon
	$(info *** Testing $(REPO))
	@docker run --rm \
    -v $(PWD):/packages/calculon \
		$(REPO):test /packages/calculon/tests/run.sh

.PHONY: build-api
build-api: ## Build api docker image
	$(info *** Building docker image: $(REPO):api)
	@docker build \
		--tag $(REPO):api \
		--file $(DOCKERFILE) \
		--target api \
		.

.PHONY: serve
serve: ## Serve the restAPI
	$(info *** Serve the API)
	@docker run \
    -d \
		-p 80:80 \
		$(REPO):api 
