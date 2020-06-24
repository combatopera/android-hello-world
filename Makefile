SRCPATH = /src

.PHONY: all
all:
	docker run --rm -it -v "$$PWD":'$(SRCPATH)' -u $$(id -u):$$(id -g) combatopera/cowpox '$(SRCPATH)'
