MIRROR_VOLUME = mirror
SRC_PATH = /src

.PHONY: all
all:
	mkdir -pv build/mirror
	docker run --rm -it -v "$$PWD":'$(SRC_PATH)' -v '$(MIRROR_VOLUME)':'$(SRC_PATH)'/build/mirror combatopera/cowpox '$(SRC_PATH)'
