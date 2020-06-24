.PHONY: all
all:
	docker run --rm -it -v "$$PWD":/src -u $$(id -u):$$(id -g) combatopera/cowpox
