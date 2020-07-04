MIRROR_VOLUME = mirror
SRC_PATH = /src
VENV_PATH = venv

.PHONY: apk
apk:
	mkdir -pv build/mirror # TODO: Do not guess where Cowpox expects it to be.
	docker run --rm -it -v "$$PWD":'$(SRC_PATH)' -v '$(MIRROR_VOLUME)':'$(SRC_PATH)'/build/mirror combatopera/cowpox '$(SRC_PATH)'

.PHONY: test
test:
	python3 -m venv '$(VENV_PATH)'
	'$(VENV_PATH)'/bin/pip install --upgrade pip # Suppress warning.
	'$(VENV_PATH)'/bin/pip install wheel # Allow binary installs.
	'$(VENV_PATH)'/bin/pip install Cython # Needed to make setup.py runnable.
	'$(VENV_PATH)'/bin/pip install -e .
	'$(VENV_PATH)'/bin/android-hello
