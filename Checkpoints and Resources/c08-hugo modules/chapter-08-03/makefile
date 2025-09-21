# Makefile for Hugo Website
# Requires: Hugo >= 0.91.2

.PHONY: help serve build clean all

all: clean build

help:
	@echo "Hugo Website Build Process"
	@echo "Usage:"
	@echo "  make serve   - Run local development server"
	@echo "  make build   - Build static site into $(PUBLIC_DIR)"
	@echo "  make clean   - Remove generated files"

serve:
	npm install && hugo server -D

build:
	npm install && hugo --minify

clean:
	rm -rf public
	rm -rf node_modules
	rm -f .hugo_build.lock
