.PHONY: all
all:
	docker run --rm -it -v "$$PWD":/src cowpox
