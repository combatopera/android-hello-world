SRCPATH = /src

.PHONY: all
all:
	docker run --rm -it -v "$$PWD":'$(SRCPATH)' combatopera/cowpox '$(SRCPATH)'
